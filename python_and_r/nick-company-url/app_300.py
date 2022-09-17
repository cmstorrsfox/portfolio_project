from flask import Flask
from flask import render_template, request, flash, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import pandas as pd;
import requests;
from requests.auth import HTTPBasicAuth
import io
from users import users
from splitter import split_csv
import os
import glob

#create instance of app
app = Flask(__name__)

app.secret_key = "nick_app"


#variables to handle file upload
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#check extension is valid function
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/split", methods=['GET', 'POST'])
def split_file():
  if request.method == 'POST':
    file = request.files['file']

    zip_splits = split_csv(file)

    return send_file(zip_splits, as_attachment=True, download_name='split_files.zip')


#get file content
@app.route("/", methods=["GET", "POST"])
def upload_file():
  if request.method == "POST":
    if 'file' not in request.files:
      flash('no file part', "error")
      return redirect(request.url)
    
    file = request.files['file']
    selected_user = request.form.get('user')
    print(selected_user)
    #if file.filename == '':
    #  flash('no selected file', "error")
    #  return redirect(request.url)
    
    if file:
      filename = secure_filename(file.filename)
      #functions to process the data
        #main function
      try:
        #input
        #buffer = io.BytesIO()
        #writer = pd.ExcelWriter(buffer, engine='xlsxwriter')
        data = pd.read_csv(file, names=['id'])

        if len(data) > 300:
          flash("Too many companies. Only 300 at a time", "error")
          return redirect(request.url)

        #endole urls
        company_url = 'https://api.endole.co.uk/company/'


        #functions to get company size and add url

        session = requests.Session()



        user_selected = users.get(selected_user)      

        def get_company_size(row):
          try:
            company_number = row
            request = session.get(company_url+str(company_number), auth=HTTPBasicAuth(user_selected['id'], user_selected['key']))
            print(f"status code: {request.status_code}")
            json_request = request.json()
            size_info = json_request['company_size']
            return size_info
          except Exception as e:
            print(e)
            
          
        def add_url(row):
          try:
            company_number = row
            url = f'https://app.creditsafe.com/companies/GB-0-0{company_number} '
            return url
          except:
            return 'url info not found'


        #data for processing
        info = data


        #function to add data to processed info
        def process_data(input):
          input['size'] = input['id'].apply(get_company_size)
          input['creditsafe_url']  = input['id'].apply(add_url)
          return input


        output = process_data(info)

        output = output[~output['size'].isin(['micro', 'Unreported', ''])]

        output.to_csv(os.path.join(app.config['UPLOAD_FOLDER'], f'{selected_user}_{filename}'), index=False)
        #writer.save()
        #buffer.seek(0)


      except Exception as e:
        print(e)


  uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])


  return render_template('index.html', file_list=uploaded_files)

#download file
@app.route("/download", methods=['GET', 'POST'])
def download_file():
  buffer = io.BytesIO()
  writer = pd.ExcelWriter(buffer, engine='xlsxwriter')
  files = glob.glob("static/uploads/*.csv")

  if len(files) == 0:
    flash('no files in upload folder', 'error')
    return redirect(request.url)
  else:

    df = pd.concat(map(pd.read_csv, files))



    df.to_excel(writer, sheet_name='Sheet1', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    worksheet.set_column(1,4, 55)

    writer.save()
    buffer.seek(0)

    for file in os.listdir(app.config['UPLOAD_FOLDER']):
      if file.endswith('.csv'):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))


    return send_file(buffer, as_attachment=True, download_name="results.xlsx")

  



if __name__ == "__main__":
  app.run(debug=True)