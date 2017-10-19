import json
import sqlite3
from flask import Flask, request, g

app = Flask(__name__)

DATABASE = 'sensor_data.db'


def get_db():
    db = getattr(g, 'sensor_data', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'sensor_data', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route("/insertData", methods=['GET','POST'])
def insert_data():
    data = request.get_json(force=True)
    print(data[u'temp'])
    print(data[u'hum'])

    return "insert data"


@app.route("/")
def hello():
    init_db()
    cur = get_db().cursor()
    return "test flask"
