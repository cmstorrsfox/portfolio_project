import os
import glob
from flask import Flask
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from flask import render_template
from flask import flash, request, redirect
from flask.helpers import send_file
from werkzeug.utils import secure_filename
from functools import reduce
from datetime import datetime, date
from io import BytesIO

#get current path
path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'upload_folder')


#make directory if upload_folder doesn't exist
if not os.path.isdir(UPLOAD_FOLDER):
  os.mkdir(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {"csv", "xlsx"}


app = Flask(__name__)

app.secret_key = "key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#checks that file being uploaded is CSV
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#renders homepage for WISEFlow Web app
@app.route('/')
def wiseflow():
  return render_template('index.html')



#run the wiseflow app
@app.route('/', methods=["GET", "POST"])

def get_test_scores():
  if request.method == "POST":
    #gets input from filename input HTML form
    
    
    
    if 'files[]' not in request.files:
      return redirect(request.url)
    
    else:
      files = request.files.getlist('files[]')

      for file in files:
        if file and allowed_file(file.filename):
          filename = secure_filename(file.filename.lower())
          file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    #sets folder where app should look for files to process
    folder = UPLOAD_FOLDER
    output_filename = request.form.get("output_filename")
    output = BytesIO()
    output_filename = output_filename+".xlsx"
    writer = pd.ExcelWriter(output, engine="xlsxwriter")

    #import all the scores as csv
    listening_1_2_glob = glob.glob(folder+"/listening1_2*.csv")
    listening_3_glob = glob.glob(folder+"/listening3*.csv")
    reading_glob = glob.glob(folder+"/reading*.csv")
    writing_glob = glob.glob(folder+"/writing*.csv")

    #turn csv into dataframes and add to list
    def concat_exams(csv_list):
        dfs = []
        
        for csv in csv_list:
          df = pd.read_csv(csv)
          df.dropna(how="all", inplace=True)
          df.fillna(0, inplace=True)
          df.drop(columns = ["Unnamed: 0", "Submitted", "Submission date", "Final grade submitted"], inplace=True)
          if "_" in os.path.basename(csv):
            if os.path.basename(csv) != "listening1_2.csv":
              assessment_name = os.path.basename(csv).rsplit("_", 1)[0]
            else:
              assessment_name = os.path.basename(csv).rsplit(".", 1)[0]
          else:
              assessment_name = os.path.basename(csv).rsplit(".", 1)[0]
          
          df.rename({"First name(s)": "First name", "Grade": assessment_name}, inplace=True, axis=1)
          dfs.append(df)
        
        output = pd.concat(dfs, axis=0)
        return output

    #call the function to create the dfs
    listening_1_2 = concat_exams(listening_1_2_glob)
    listening_3 = concat_exams(listening_3_glob)
    reading = concat_exams(reading_glob)
    writing = concat_exams(writing_glob)

    #add dfs to a list and then reduce to merge into one dataframe
    dfs = [listening_1_2, listening_3, reading, writing]
    all_data = reduce(lambda left, right: pd.merge(left, right, on=["Student Number", "First name", "Last name", "Institution"], how="outer"), dfs)




    #calculate the listening total and then rearrange the columns
    all_data["listening_total"] = (((all_data["listening1_2"]/100)*12) + ((all_data["listening3"]/100)*28))/40 *100
    all_data["listening_total"] = round(all_data["listening_total"], 2)
    all_data = all_data[["Student Number", "First name", "Last name", "Institution", "listening1_2", "listening3", "listening_total", "reading", "writing"]]
    
    #defines columns for table
    columns = all_data.columns.tolist()




    #melt df then group for boxplot of results to visualise data
    melt = pd.melt(all_data[["Student Number", "listening_total", "reading", "writing"]], id_vars=["Student Number"], var_name="exam", value_name="score")
    melt.replace(0, np.nan, inplace=True)
    melt.dropna(subset=["score"], how="any", axis=0, inplace=True)

    #plot boxplot
    sns.boxplot(x=melt["exam"], y=melt["score"])
    plt.title("Boxplot of exam scores showing median,\n quartiles and min and max scores")
    plt.tight_layout()
    plt.savefig("boxplot.png")

    plt.clf()

    #plot histogram
    sns.histplot(data=melt, x="score", hue="exam", multiple="dodge", shrink=.8)
    plt.title("Histogram showing spread of scores from different exams")
    plt.tight_layout()
    plt.savefig("histplot.png")

    plt.clf()

    #drop the index column and then export to Excel file
    all_data.set_index("Student Number", inplace=True)
    all_data.to_excel(writer, sheet_name="Sheet1")

    #Get Excel file and sheet
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]

    #add worksheet for charts
    worksheet_two = workbook.add_worksheet('Charts')

    #add charts to worksheet
    worksheet_two.insert_image("A1", "boxplot.png")
    worksheet_two.insert_image("L1", "histplot.png")

    #Apply conditional formatting
    data_length = len(all_data)+1
    data_width = len(all_data.columns)
    a_j = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    letter_equiv = a_j[data_width]

    #add student data table
    worksheet.add_table("A1:{}{}".format(letter_equiv, data_length), {"header_row": True, "banded_columns": True, "columns": [{"header": column} for column in columns]})
    #formats
    duplicate_values = workbook.add_format({"bg_color": "#FFEB9C", "font_color": "#9C6500"})
    top_10 = workbook.add_format({"bg_color": "#C6EFCE", "font_color": "#006100"})
    fails = workbook.add_format({"bg_color": "#FFC7CE", "font_color": "#9C0006"})
    bold = workbook.add_format({"bold": True})
    #add legend table
    worksheet.set_column('L:L', 28)
    worksheet.set_column('M:M', 10)
    worksheet.write("L1", "Legend", bold)
    worksheet.write("L3", "Duplicate Entries")
    worksheet.write("L4", "Failing Grade")
    worksheet.write("L5", r"Top 10% for a given exam")
    worksheet.write("M3", "Yellow", duplicate_values)
    worksheet.write("M4", "Red", fails)
    worksheet.write("M5", "Green", top_10)
    worksheet.add_table("L2:M5", {"header_row": True, "columns": [{"header": "Colour"}, {"header": "Value"}]})
    #duplicates
    worksheet.conditional_format("A2:A{}".format(data_length), {"type": "duplicate","format": duplicate_values})
    #top-10 - listening
    worksheet.conditional_format("G2:G{}".format(data_length), {"type": "top", "value": 10, "criteria": "%", "format": top_10})
    #top-10 - reading
    worksheet.conditional_format("H2:H{}".format(data_length), {"type": "top", "value": 10, "criteria": "%", "format": top_10})
    #top-10 - writing
    worksheet.conditional_format("I2:I{}".format(data_length), {"type": "top", "value": 10, "criteria": "%", "format": top_10})
    #fails
    worksheet.conditional_format("G2:{}{}".format(letter_equiv, data_length), {"type": "cell", "criteria": "less than", "value": 40,"format": fails})

    #close excel file
    writer.close()
    os.remove("boxplot.png")
    os.remove("histplot.png")
    
    if os.path.isdir(folder):
      dir = os.listdir(folder)
      for f in dir:
        if f != "file.txt":
          path = os.path.join(folder, f)
          os.remove(path)

    #go back to the beginning of the stream
    output.seek(0)
    
    #return the file produced
    return send_file(output, attachment_filename=output_filename, as_attachment=True)


#loads the listening calculator
@app.route('/listening-calculator')
def listening_calculator():
  return render_template("listening.html")


#runs the listening calculator  
@app.route('/listening-calculator', methods=['GET', 'POST'])

def get_listening_scores():
  if request.method == "POST":
    #gets input from filename input HTML form
    
    
    
    if 'files[]' not in request.files:
      return redirect(request.url)
    
    else:
      files = request.files.getlist('files[]')

      for file in files:
        if file and allowed_file(file.filename):
          filename = secure_filename(file.filename.lower())
          file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    #sets folder where app should look for files to process
    folder = UPLOAD_FOLDER
    output_filename = request.form.get("file-name")
    output = BytesIO()
    output_filename = output_filename+".xlsx"
    writer = pd.ExcelWriter(output, engine="xlsxwriter")

    #import all the scores as csv
    listening_1_2_glob = glob.glob(folder+"/listening1_2*.csv")
    listening_3_glob = glob.glob(folder+"/listening3*.csv")

    #turn csv into dataframes and add to list
    def concat_exams(csv_list):
        dfs = []
        
        for csv in csv_list:
          df = pd.read_csv(csv)
          df.dropna(how="all", inplace=True)
          df.fillna(0, inplace=True)
          df.drop(columns = ["Unnamed: 0", "Submitted", "Submission date", "Final grade submitted"], inplace=True)
          if "_" in os.path.basename(csv):
            if os.path.basename(csv) != "listening1_2.csv":
              assessment_name = os.path.basename(csv).rsplit("_", 1)[0]
            else:
              assessment_name = os.path.basename(csv).rsplit(".", 1)[0]
          else:
              assessment_name = os.path.basename(csv).rsplit(".", 1)[0]
          
          df.rename({"First name(s)": "First name", "Grade": assessment_name}, inplace=True, axis=1)
          dfs.append(df)
        
        output = pd.concat(dfs, axis=0)
        return output

    #call the function to create the dfs
    listening_1_2 = concat_exams(listening_1_2_glob)
    listening_3 = concat_exams(listening_3_glob)

    #add dfs to a list and then reduce to merge into one dataframe
    dfs = [listening_1_2, listening_3]
    all_data = reduce(lambda left, right: pd.merge(left, right, on=["Student Number", "First name", "Last name", "Institution"]), dfs)




    #calculate the listening total and then rearrange the columns
    all_data["listening_total"] = (((all_data["listening1_2"]/100)*12) + ((all_data["listening3"]/100)*28))/40 *100
    all_data["listening_total"] = round(all_data["listening_total"], 2)
    all_data = all_data[["Student Number", "First name", "Last name", "Institution", "listening1_2", "listening3", "listening_total"]]
    
    #defines columns for table
    columns = all_data.columns.tolist()


    #drop the index column and then export to Excel file
    all_data.set_index("Student Number", inplace=True)
    all_data.to_excel(writer, sheet_name="Sheet1")

    #Get Excel file and sheet
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]

    #Apply conditional formatting
    data_length = len(all_data)+1
    data_width = len(all_data.columns)
    a_j = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    letter_equiv = a_j[data_width]

    #add student data table
    worksheet.add_table("A1:{}{}".format(letter_equiv, data_length), {"header_row": True, "banded_columns": True, "columns": [{"header": column} for column in columns]})
    #formats
    duplicate_values = workbook.add_format({"bg_color": "#FFEB9C", "font_color": "#9C6500"})
    top_10 = workbook.add_format({"bg_color": "#C6EFCE", "font_color": "#006100"})
    fails = workbook.add_format({"bg_color": "#FFC7CE", "font_color": "#9C0006"})
    bold = workbook.add_format({"bold": True})
    #add legend table
    worksheet.set_column('L:L', 28)
    worksheet.set_column('M:M', 10)
    worksheet.write("L1", "Legend", bold)
    worksheet.write("L3", "Duplicate Entries")
    worksheet.write("L4", "Failing Grade")
    worksheet.write("L5", r"Top 10% for a given exam")
    worksheet.write("M3", "Yellow", duplicate_values)
    worksheet.write("M4", "Red", fails)
    worksheet.write("M5", "Green", top_10)
    worksheet.add_table("L2:M5", {"header_row": True, "columns": [{"header": "Colour"}, {"header": "Value"}]})
    #duplicates
    worksheet.conditional_format("A2:A{}".format(data_length), {"type": "duplicate","format": duplicate_values})
    #top-10 - listening
    worksheet.conditional_format("G2:G{}".format(data_length), {"type": "top", "value": 10, "criteria": "%", "format": top_10})
    #fails
    worksheet.conditional_format("G2:G{}".format(data_length), {"type": "cell", "criteria": "less than", "value": 40,"format": fails})

    #close excel file
    writer.close()
    
    if os.path.isdir(folder):
      dir = os.listdir(folder)
      for f in dir:
        if f != "file.txt":
          path = os.path.join(folder, f)
          os.remove(path)

    #go back to the beginning of the stream
    output.seek(0)
    
    #return the file produced
    return send_file(output, attachment_filename=output_filename, as_attachment=True)


#loads the student overview tool
@app.route('/student-overview')
def student_overview():
  return render_template("student-overview.html")


@app.route('/student-overview', methods=["GET", "POST"])

def compile_student_data():
  if request.method == "POST":
  #gets input from filename input HTML form
    
    
    
    if 'files[]' not in request.files:
      return redirect(request.url)
    
    else:
      files = request.files.getlist('files[]')

      for file in files:
        if file and allowed_file(file.filename):
          filename = secure_filename(file.filename.lower())
          file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    #sets folder where app should look for files to process
    folder = UPLOAD_FOLDER
    output = BytesIO()
    #start of function
    #import data
    student_data_glob = glob.glob(folder+"/student_data.xlsx")
    results_glob = glob.glob(folder+"/*results.csv")
    class_glob = glob.glob(folder+"/class_data.csv")
    rpag_glob = glob.glob(folder+"/rpag_data.csv")

    #loop through and concatenate
    def create_dfs(file_list, header_no):
        dfs = []
        for file in file_list:
            if file.endswith(".xlsx"):
                df = pd.read_excel(file)
                df.dropna(subset=["Requirement - AES %"], inplace=True)
            else:
                df = pd.read_csv(file, header=header_no, skip_blank_lines=True)
                df.fillna(0, inplace=True)
              

            dfs.append(df)
        
        if len(dfs)>0:
            output = pd.concat(dfs, axis=0)
        else:
            output = dfs
        
        return output
    
    #create dfs
    student_data_df = create_dfs(student_data_glob, 0)
    results_df = create_dfs(results_glob, 1)
    class_df = create_dfs(class_glob, 0)
    rpag_df = create_dfs(rpag_glob, 2)

    #create results df
    results_df.rename({"Unnamed: 0": "Student ID", "Unnamed: 1": "Name"}, inplace=True, axis=1)
    results_df.drop(["Admin Code", "Term", "Name", "Comments", "Man. Override"], axis=1, inplace=True)
    results_df = results_df[[column for column in results_df.columns[0:23]]]
    results_df.set_index("Student ID", inplace=True)
    

    #create student data df
    #convert dob to age
    def age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    student_data_df["Age"] = student_data_df["Date of Birth"].apply(age)
    student_data_df[["Listening Requirement", "Reading Requirement", "Writing Requirement", "Speaking Requirement"]] = student_data_df["Requirements - AES LRWS %"].str.split(";", expand=True).astype("int64")
    student_data_df["Full Name"] = student_data_df["Forename"] + " " + student_data_df["Surname"]
    student_data_df = student_data_df[["Learner Code", "Full Name", "Status", "Reg Grp", "M/F", "Age", "First Nationality", "Initial Test Result (English)", "Requirement - AES %", "Listening Requirement", "Reading Requirement", "Writing Requirement", "Speaking Requirement"]]
    student_data_df.rename({"Learner Code": "Student ID"}, inplace=True, axis=1)
    student_data_df["Student ID"] = student_data_df["Student ID"].astype("int64")
    #student_data_df.set_index("Student ID", inplace=True)
    

    #create class df
    class_df = class_df[["Learner_Code", "CurrentRegistrationGroupName"]]
    class_df.rename({"CurrentRegistrationGroupName": "Class", "Learner_Code": "Student ID"}, inplace=True, axis=1)
    class_df.set_index("Student ID", inplace=True)

    #create RPAG and attendance df
    cols = ["RPAG_period", "Subject", "Student ID", "Last Name", "First Name", "Status", "Entry Date", "Reg Group", "Attendance", "Subject RPAG", "Overall RPAG for period"]
    rpag_df.drop(columns=["Textbox132","Textbox29", "Textbox41", "Textbox146"], inplace=True)
    rpag_df.columns = cols
    rpag_df = rpag_df[rpag_df["Subject"] == "Academic English Skills"]
    rpag_df = rpag_df[rpag_df["Status"] == "Active"]
    rpag_df.drop(columns=["Overall RPAG for period"], inplace=True)
    rpag_cats = ["R", "P", "A", "G"]
    rpag_df["Subject RPAG"] = pd.Categorical(rpag_df["Subject RPAG"], categories=rpag_cats, ordered=True)
    rpag_df["RPAG Code"] = rpag_df["Subject RPAG"].cat.codes
    rpag_df["RPAG Code"] = rpag_df["RPAG Code"] + 1
    rpag_df.reset_index(drop=True, inplace=True)
    rpag_df.dropna(subset=["Subject RPAG"], inplace=True)
    rpag_data = rpag_df.pivot(index=["Student ID"], columns=["RPAG_period"], values="RPAG Code")
    attendance_data = rpag_df[["Student ID", "Attendance"]].groupby("Student ID").mean()



    new_df = reduce(lambda left, right: pd.merge(left, right, on="Student ID"), [student_data_df, class_df, results_df, attendance_data, rpag_data])

    cols = list(student_data_df.columns) + list(class_df) + list(attendance_data.columns) + list(results_df.columns) + list(rpag_data.columns)

    new_df = new_df[cols]

    new_df.fillna(0, axis=1, inplace=True)

    #add calculated columns for overall progress
    def calculate_status(row):
      if row["Module Total"] >= (row["Requirement - AES %"]*0.9):
        val = "Green"
      elif (row["Module Total"] < row["Requirement - AES %"]) and (row["Module Total"] >= (row["Requirement - AES %"]*0.7)):
        val = "Amber"
      elif (row["Module Total"] < row["Requirement - AES %"]) and (row["Module Total"] >= (row["Requirement - AES %"]*0.5)):
        val = "Pink"
      else:
        val = "Red"
      return val

    new_df["Current Progression Status"] = new_df.apply(calculate_status, axis=1)
    
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    new_df.to_excel(writer, sheet_name="all_data", index=False)

    ##add formatting to table
    workbook = writer.book
    worksheet = writer.sheets["all_data"]

    ##add table
    
    columns = new_df.columns.tolist()
    (max_row, max_col) = new_df.shape
    worksheet.add_table(0, 0, max_row, max_col-1, {"header_row": True, "banded_columns": True, "columns": [{"header": column} for column in columns]})
    #writer.save()

    #close excel file
    writer.close()
    
    if os.path.isdir(folder):
      dir = os.listdir(folder)
      for f in dir:
        if f != "file.txt":
          path = os.path.join(folder, f)
          os.remove(path)

    #go back to the beginning of the stream
    output.seek(0)
    
    #return the file produced
    return send_file(output, attachment_filename="Student Data Sheet.xlsx", as_attachment=True)


#runs app
#if __name__ == "__main__":
#  app.run(host="127.0.0.1", port=5000, debug=False, )

