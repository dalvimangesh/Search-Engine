from elasticsearch import Elasticsearch
from PreProcessing import PreProcessor
import json
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class BM25:

    def __init__(self, es, index_name, IndexOriginal) -> None:
        print("Creating Model BM25 ... \n")
        self.es = es
        self.index_name = index_name
        self.original = IndexOriginal
        print('END\n')

    def GetResult(self, index_name, query, number):

        res1 = self.es.search(index=index_name, body=query)

        result = list()

        for i in range(min(number, len(res1['hits']['hits']))):
            result.append(self.es.get(
                index=self.original, id=res1['hits']['hits'][i]['_source']['id'])['_source'])
        return result

    def MakeQuery(self, query, number):

        q = query

        body = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "match": {
                                "Title": {
                                    "boost": 4,
                                    "query": q
                                }
                            }
                        },
                        {
                            "match": {
                                "Summary": {
                                    "boost": 2,
                                    "query": q
                                }
                            }
                        },
                        {
                            "match": {
                                "Text": {
                                    "query": q
                                }
                            }
                        }
                    ]
                }
            }
        }
        return self.GetResult(self.index_name, body, number)


class TF_IDF:

    def __init__(self, es, index_name, number, IndexOriginal) -> None:
        print("Creating Model TF-IDF ... \n")
        self.original = IndexOriginal
        self.data = list()
        self.index_name = index_name
        for i in range(1, number+1):
            self.data.append(es.get(index=index_name, id=str(i))['_source'])
        self.df = pd.DataFrame.from_dict(self.data)
        self.vectorizer = TfidfVectorizer()
        self.es = es
        self.X = self.vectorizer.fit_transform(
            self.df['Text']+self.df['Title']+self.df['Summary'])
        print('END\n')

    def MakeQuery(self, query, number):
        query_vec = self.vectorizer.transform([query])
        results = cosine_similarity(self.X, query_vec)

        temp = list()

        cnt = 0

        for i in results:
            temp.append([float(i[0]), cnt])
            cnt += 1

        temp.sort(reverse=True)

        matches = list()

        for i in temp[: min(number, len(temp))]:
            matches.append(self.es.get(
                index=self.original, id=self.data[i[1]]['id'])['_source'])
        return matches
