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

#remove names, numbers and other special character (bit blunt - needs work)
comments_18_21["comment"] = comments_18_21["comment"].str.replace("([A-Z]\w+('s)?)(\s[A-Z]\w+('s)?)?|[^\w\s]+|[\d]", "")

#stopwords
stopwords = stopwords.words("english")


#apply tokenization to each comment
def tokenize_and_pos_tag(comment):
  sent_tokens = sent_tokenize(comment.strip())
  word_tokens = [word_tokenize(word) for word in sent_tokens]
  pos_tagged = [pos_tag(token) for token in word_tokens]
  flattened = [val for sublist in pos_tagged for val in sublist]
  stopwords_gone = [(word, pos) for (word, pos) in flattened if word not in stopwords]
  return stopwords_gone

comments_18_21["tokens"] = comments_18_21["comment"].apply(tokenize_and_pos_tag)

print(comments_18_21["tokens"])