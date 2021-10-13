from pos_tokens import comments_18_21
from sklearn.feature_extraction.text import CountVectorizer



#re-join comment tokens
def rejoin_tokens(row):
  words = []
  for (word, pos) in row:
    words.append(word)
  return " ".join(words)


comments_18_21["cleaned"] = comments_18_21["tokens"].apply(rejoin_tokens)

#vectorize the words
bow_vectorizer = CountVectorizer()

#group comments by color
greens = comments_18_21["cleaned"][comments_18_21["rating"]=="Green"].tolist()
ambers = comments_18_21["cleaned"][comments_18_21["rating"]=="Amber"].tolist()
pinks = comments_18_21["cleaned"][comments_18_21["rating"]=="Pink"].tolist()
reds = comments_18_21["cleaned"][comments_18_21["rating"]=="Red"].tolist()


all_comments = greens + ambers + pinks + reds

#create labels
labels = ["green"] * len(greens) + ["amber"] * len(ambers) + ["pink"] * len(pinks) + ["red"] * len(reds)


#create test comment
unclassified_rpag = "John should try much harder in his next assignment. The work submitted so far is poor."

#create vectors
comments_vectors = bow_vectorizer.fit_transform(all_comments)





