import sqlite3
from flask import Flask, request, g, jsonify

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
    db = get_db()
    query = 'INSERT INTO measurement (sensor, value)'\
        ' VALUES ("' + sensor + '", ' + str(value) + ')'
    db.cursor().execute(query)
    db.commit()
    id_inserted = db.cursor().lastrowid
    db.cursor().close()
    return id_inserted


def select_all_db():
    db = get_db()
    query = 'SELECT * FROM measurement;'
    cur = db.cursor().execute(query)
    result = cur.fetchall()
    cur.close()
    return result


def serialize(result):
    d = []
    for id, sensor, value, timestamp in result:
        m = {}
        m["id"] = id
        m["sensor"] = sensor
        m["value"] = value
        m["timestamp"] = timestamp
        d.append(m)

    return d


@app.route("/insertData", methods=['GET', 'POST'])
def insert_data():
    data = request.get_json(force=True)
    insert_db('temp', data[u'temp'])
    insert_db('hum', data[u'hum'])
    return "Data inserted sucessfully!"


@app.route("/getData", methods=['GET', 'POST'])
def get_data():
    result = select_all_db()
    d = serialize(result)

    return jsonify(d)


@app.route("/")
def hello():
    init_db()
    return "Server is Running..."
