from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route("/insertData", methods=['GET', 'POST'])
def insert_data():
    print(request)
    if request.method == POST:
        data = request.get_json(force=True)
        print(data[u'temp'])
        print(data[u'hum'])

    return "insert data"


@app.route("/")
def hello():
    return "test flask"

