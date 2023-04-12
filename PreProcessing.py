import nltk
import re
import gensim
from nltk.stem import SnowballStemmer
from nltk.stem import PorterStemmer
from gensim.parsing.preprocessing import remove_stopwords
from nltk.stem import WordNetLemmatizer
from string import punctuation
from autocorrect import Speller


class PreProcessor:

    def __init__(self, json_file):
        self.json = json_file
        self.final_data = self.Build()

    def Build(self):
        final = list()
        for i in self.json:
            temp = i.keys()
            res = dict()
            for j in temp:
                res1 = i[j]
                res1 = self.decontracted(res1)
                res1 = self.remove_punct(res1)
                s = self.RemoveStopWords(
                    self.LemmatizeWords(self.StemWords(res1)))
                res[j] = s
            final.append(res)
        return final

    def StemWords(self, string):
        ps = SnowballStemmer('english')
        string = nltk.word_tokenize(string)
        l = []
        for w in string:
            s = ps.stem(w)
            l.append(s)
        return ' '.join(str(ele).lower() for ele in l)

    def LemmatizeWords(self, string):
        lm = WordNetLemmatizer()
        string = nltk.word_tokenize(string)
        l = []
        for w in string:
            s = lm.lemmatize(w)
            l.append(s)
        return ' '.join(str(ele).lower() for ele in l)

    def RemoveStopWords(slef, string):
        return remove_stopwords(string)

    def decontracted(self, phrase):
        phrase = re.sub(r"won\'t", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)
        phrase = re.sub(r"n\'t", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)
        return phrase

    def remove_punct(self, text):
        return ''.join(c for c in text if c not in punctuation)
