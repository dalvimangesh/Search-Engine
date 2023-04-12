from flask import Flask, redirect, url_for, render_template, request
from final import modeltfidf
from final import modelbm25
import os
modeltfidf = modeltfidf
modelbm25 = modelbm25

app = Flask(__name__)

pic = os.path.join('static')


@app.route('/')
def welcome():
    pic1 = os.path.join(pic, 'photo2.jpg')
    return render_template('index.html', result={}, query="", queries=5, model="BM25", user=pic1)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    res = list()
    q = ""
    num = 10
    modelName = "BM25"
    if request.method == 'POST':
        query = request.form['SearchBar']
        modelname = request.form['model']
        queries = request.form['Results']
        num = queries
        q = query
        x = int(queries)
        if (modelname == "BM25"):
            res = modelbm25.MakeQuery(query, x)
        else:
            modelName = "TFIDF"
            res = modeltfidf.MakeQuery(query, x)

    toSubmit = res
    pic1 = os.path.join(pic, 'photo3.jpg')
    return render_template('index.html', result=toSubmit, query=q, queries=num, model=modelName, user=pic1)


if __name__ == '__main__':
    app.run(debug=True)
