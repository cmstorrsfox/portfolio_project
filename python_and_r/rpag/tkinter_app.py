#import packages
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd


#rpag function
def get_rpag_subject_data(rpag_file, subject, output):
  df = pd.read_csv(rpag_file)

  df = df[[df.columns[0], df.columns[1], df.columns[3], df.columns[17], df.columns[18], df.columns[20]]].reset_index(drop=True)

  df.rename({df.columns[0]: "Student ID", df.columns[1]: "Full Name", df.columns[2]: "Pathway", df.columns[3]: "RPAG Period", df.columns[4]: "Subject", df.columns[5]: "Rating"}, axis=1, inplace=True)

  df = df[df["Subject"] == subject]

  
  df = df.pivot(index=["Student ID", "Full Name", "Pathway"], columns="RPAG Period", values="Rating")
  
  df.to_excel(output+"/RPAG information for {}.xlsx".format(subject))
  return df

#get subject list
def get_subjects():
  df = pd.read_csv(rpag_file.get())
  subject_list = [x for x in df.SubjectName.dropna().unique()]
  return subject_list



#output function
def output_path():
  path = filedialog.askdirectory()
  output.set(path)


#input function & subject list
def input_path():
  path = filedialog.askopenfilename(filetypes=(("csv files", "*.csv"), ("All files", "'*.*")))
  rpag_file.set(path)
  subject_entry["values"] = get_subjects()



#process function
def process():
  get_rpag_subject_data(rpag_file.get(), subject.get(), output.get())
  root.destroy()

#tkinter
root = Tk()

root.title("RPAG and Attendance Report Processor")

#window
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#variables
rpag_file = StringVar()
subject = StringVar()
output = StringVar()


#text and labels
rpag_label = ttk.Label(mainframe, text="RPAG filepath").grid(column=1, row=1, sticky=(W,E))
rpag_entry = ttk.Entry(mainframe, width=30, textvariable=rpag_file)
rpag_entry.grid(column=2, row=1, sticky=(W,E))
ttk.Button(mainframe, text="Find file", command=input_path).grid(column=3, row=1, sticky=(W,E))
subject_label = ttk.Label(mainframe, text="Subject").grid(column=1, row=2, sticky=(W,E))
subject_entry = ttk.Combobox(mainframe, width=30, textvariable=subject)
subject_entry.grid(column=2, row=2, sticky=(W,E))
output_label = ttk.Label(mainframe, text="Save location").grid(column=1, row=3, sticky=(W,E))
output_entry = ttk.Entry(mainframe, width=30, textvariable=output)
output_entry.grid(column=2, row=3, sticky=(W,E))
ttk.Button(mainframe, text="Choose folder", command=output_path).grid(column=3, row=3, sticky=(W,E))


ttk.Button(mainframe, text="Process RPAGs", command=lambda: process()).grid(column=2, row=4, stick=(W,E))

subject_entry.current()
root.mainloop()
