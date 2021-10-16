import gensim
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt

#load gensim model
new_model = gensim.models.Word2Vec.load("rpag_model")

similar = new_model.wv.most_similar("improve")

doesnt_match = new_model.wv.doesnt_match(["good", "great", "bad", "excellent"])

similar_by_word = new_model.wv.similar_by_word("tutors", topn=10)

df = pd.DataFrame(similar_by_word, columns=["word", "similarity"])

fig, ax = plt.subplots(1, figsize=(10,6))
ax.bar(x=df["word"], height=df["similarity"])
ax.set_ylim(0.9, 1)
ax.set_xticklabels(labels=df["word"], rotation=30, ha="right")
ax.set_title("Similarity Scores for 'English'")

#plt.show()

most_common_words = new_model.wv.index2word[-10:]

print(most_common_words)