#import packages
import pandas as pd
import numpy as np


#get RPAG data from csv

def get_rpag_subject_data(filepath, subject):
  df = pd.read_csv(filepath)

  df = df[[df.columns[0], df.columns[1], df.columns[3], df.columns[17], df.columns[18], df.columns[20]]].reset_index(drop=True)

  df.rename({df.columns[0]: "Student ID", df.columns[1]: "Full Name", df.columns[2]: "Pathway", df.columns[3]: "RPAG Period", df.columns[4]: "Subject", df.columns[5]: "Rating"}, axis=1, inplace=True)

  df = df[df["Subject"] == subject]

  
  df = df.pivot(index=["Student ID", "Full Name", "Pathway"], columns="RPAG Period", values="Rating")
  
  df.to_excel("RPAG information for {}.xlsx".format(subject))

  return df


#get_rpag_subject_data("rpag.csv", "Academic English Skills")



def get_attendance_by_subject(subject):
  df = pd.read_csv("attendance.csv")

  df = df[[df.columns[1], df.columns[0], "Subject", df.columns[39]]]

  df.rename({df.columns[0]: "Student ID", df.columns[1]: "Full Name", df.columns[3]: "Attendance"}, axis=1, inplace=True)

  def fix_name(row):
    names = row.split(',')
    full_name = "{} {}".format(names[1], names[0])
    return full_name
  
  df["Full Name"] = df["Full Name"].apply(fix_name)

  df.dropna(how="any", axis=0, inplace=True)

  df = df[df["Subject"] == subject].reset_index(drop=True)

  df.to_excel("Attendance information for {}.xlsx".format(subject), index=False)

  return df

get_attendance_by_subject("Academic English Skills")


