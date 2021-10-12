#import packages for processing text
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import RegexpParser
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
import re
import pandas as pd
import glob
from IPython.display import display

#import texts
comments_18_21 = [pd.read_csv(csv) for csv in glob.glob("raw_data/*.csv")]

#create dataframe
comments_18_21 = pd.concat(comments_18_21)

#remove na values
comments_18_21 = comments_18_21.dropna(how="any", axis=0)




