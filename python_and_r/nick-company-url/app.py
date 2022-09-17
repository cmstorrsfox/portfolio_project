from flask import Flask, send_file
from flask import render_template, request, flash, redirect, url_for, send_from_directory
import os
import pandas as pd;
import requests;
from requests.auth import HTTPBasicAuth
import random
import io

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


#get file content
@app.route("/", methods=["GET", "POST"])
def upload_file():
  if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], 'results.xlsx')):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], 'results.xlsx'))


  if request.method == "POST":
    if 'file' not in request.files:
      flash('no file part')
      return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
      flash('no selected file')
      return redirect(request.url)
    
    if file:
      #functions to process the data

      #function to split df
      def splitter(df):
        split_size = round(len(df) / 300)
        if len(df) > 300:
          split_data = np.array_split(df, split_size)
          return split_data
        else:
          return df

      #main function
      try:
        #input
        buffer = io.BytesIO()
        writer = pd.ExcelWriter(buffer, engine='xlsxwriter')
        data = pd.read_csv(file, names=['id'])


        #endole users
        user1 = {
          'id': '21588', 
          'key': 'cGBOj2iS8EGyT2rc40PgPUpez1Eh5gNM'
          }
          
        user2 = {
            'id': '21744',
            'key': '8Tsfxr3BnfX45E74sfESATH7bumqhQiu'
          }

        user3 = {
          'id': '21745',
          'key': 'r8K3Da4rpFonR2Hud2Xkxsea5LU3p0Uu'
          }

        user4 = {
          'id': '21746',
          'key': '8z69agfB0Et0IuntUmuXeiLkGgmxMTnq'
        }

        users = [user1, user2, user3, user4]

        #endole urls
        company_url = 'https://api.endole.co.uk/company/'


        #functions to get company size and add url

        session = requests.Session()

        def get_company_size(row, user):
          try:
            company_number = row
            request = session.get(company_url+str(company_number), auth=HTTPBasicAuth(user['id'], user['key']))
            print(request.status_code)
            json_request = request.json()
            size_info = json_request['company_size']
            return size_info
          except:
            pass
            
          
        def add_url(row):
          try:
            company_number = row
            url = f'https://app.creditsafe.com/companies/GB-0-0{company_number} '
            return url
          except:
            return 'url info not found'


        #data for processing
        info = splitter(data)


        #function to add data to processed info
        def process_data(input):
          random.shuffle(users)
          df_num = 0
          if isinstance(input, list) and len(input) > 4:
            print('Too many requests. Limit your search to 1200 company numbers in a 5 minute period')
          elif isinstance(input, list) and len(input) > 1:
            frames = []
            for df in input:
              print(users[df_num])
              df['size'] = df['id'].apply(get_company_size, args=(users[df_num],))
              df['creditsafe_url']  = df['id'].apply(add_url)
              df_num +=1
              frames.append(df)
            
            final_df = pd.concat(frames)
            return final_df
          else:
            input['size'] = input['id'].apply(get_company_size, args=(users[df_num],))
            input['creditsafe_url']  = input['id'].apply(add_url)
            return input


        output = process_data(info)

        output = output[~output['size'].isin(['micro', 'Unreported', ''])]

        output.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.save()
        buffer.seek(0)
        return send_file(buffer, attachment_filename='output.xlsx', as_attachment=True)

      except Exception as e:
        return redirect(url_for('report_error', e=e))



      #call functions to process data
      #result = q.enqueue(get_data, file)
     

  return render_template('index.html')

#download document
@app.route('/uploads/<name>')
def download_file(name): 
  return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/error/<e>')
def report_error(e):
  return render_template('error.html', e)