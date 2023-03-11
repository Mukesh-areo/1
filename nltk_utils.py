import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()
def tokenization(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence,all_words):
    pass

a="How long does shipping takes"
print(a)
a=tokenization(a)
print(a)

words=['organize','organizes','organiser']
s=[stem(w) for w in words]
print(s)