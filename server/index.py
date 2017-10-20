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

def insert_db(sensor, value):
	print(type(sensor))
	print(type(value))
	db = get_db()
	query = 'INSERT INTO measurement (sensor, value)'\
	' VALUES ("'+ sensor +'", '+ str(value) +')'

	print(query)
	db.cursor().execute(query)
	db.commit()
	id_inserted =  db.cursor().lastrowid
	db.cursor().close()
	return id_inserted


@app.route("/insertData", methods=['GET','POST'])
def insert_data():
    data = request.get_json(force=True)
    print(data[u'temp'])
    print(data[u'hum'])
    tmp1 = insert_db('temp', data[u'temp'])
    tmp2 = insert_db('hum', data[u'hum'])
    return "insert data" + str(tmp1) + str(tmp2)


@app.route("/")
def hello():
    init_db()
    cur = get_db().cursor()
    return "test flask"
