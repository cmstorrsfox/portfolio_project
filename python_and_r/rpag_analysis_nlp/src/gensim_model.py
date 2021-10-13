#import the dataset
from bow import greens, ambers, pinks, reds
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec 
import tempfile


#print(comments_18_21["comment"].head())

#stopwords
stopwords = stopwords.words("english")

#list of comments, tokenized
green_tokens = [word_tokenize(word) for word in greens if word not in stopwords]

amber_tokens = [word_tokenize(word) for word in ambers if word not in stopwords]

pink_tokens = [word_tokenize(word) for word in pinks if word not in stopwords]

red_tokens = [word_tokenize(word) for word in reds if word not in stopwords]

comments = green_tokens + amber_tokens + pink_tokens + red_tokens

model = Word2Vec(sentences=comments, size=100)


model.save("rpag_model")