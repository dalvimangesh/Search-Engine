from model import TF_IDF
from model import BM25
from elasticsearch import Elasticsearch
from PreProcessing import PreProcessor

import json

es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()


def InsertData(data, index_name):
    for i in data:
        es.index(index=index_name, id=i['id'], body=i)


def DeleteIndex(index_name):
    es.indices.delete(index=index_name)


# f = open('dataset.json')
# data = json.load(f)

# InsertData(data=data, index_name="originaldata")

# data = PreProcessor(data).final_data

# InsertData(data, "dataset")

modelbm25 = BM25(es, "dataset", "originaldata")

modeltfidf = TF_IDF(es, "dataset", 8830, "originaldata")
