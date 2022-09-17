import numpy as np
import pandas as pd
import io
import shutil
import os
import math


def split_csv(file):
  
  #delete existing zip file
  if(os.path.exists('static/zipped_split_files.zip')):
    os.remove(os.path.join('static/', 'zipped_split_files.zip'))

  #ensure upload folder is empty
  if len(os.listdir('static/split_files')) >=1:
    for item in os.listdir('static/split_files'):
      if not item.endswith('.txt'):
        os.remove(os.path.join('static/split_files', item))


  df = pd.read_csv(file, usecols=['company_number'])
  split_size = math.ceil(len(df) / 300)
  if len(df) > 300:
    split_arrs = np.array_split(df, split_size)
    
    for i in range(len(split_arrs)):
      split_arrs[i].to_csv(f'static/split_files/file_{i+1}.csv', index=False, header=False)
    
    return shutil.make_archive('static/zipped_split_files', 'zip', 'static/split_files')




