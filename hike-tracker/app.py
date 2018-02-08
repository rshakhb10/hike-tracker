import json
import sqlite3
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/hikes', methods = ['GET', 'POST'])
def show_hikes():
    if request.method == 'GET':
        all_hikes = get_all_hikes()
        return json.dumps(all_hikes)
    elif request.method == 'POST':
        d = request.form
        res = add_hike(d['name'], d['hike_date'], d['mountain'], d['comment'])
        return jsonify(res)

@app.route('/hike/<hike_id>', methods = ['GET', 'PUT', 'DELETE'])
def show_hike(hike_id):
    if request.method == 'GET':
        hike = get_single_hike(hike_id)
        return json.dumps(hike)    

def add_hike(name, hike_date=None, mountain=None, comment=None):
    try:
        with sqlite3.connect('hiketrips.db') as conn:
            c = conn.cursor()
            query = '''insert into hikes (hike_name, hike_date, mountain_id, comment) 
            values (?,?,?,?);'''
            c.execute(query, (name, hike_date, mountain, comment,))
            res = {'status': 1, 'message': 'new hike added'}
    except:
        res = {'status': 0, 'message': 'error happened'}
    return res

def get_all_hikes():
    with sqlite3.connect('hiketrips.db') as conn:
        c = conn.cursor()
        query = '''select * from hikes'''
        c.execute(query)
        return c.fetchall()

def get_single_hike(hike_id):
    with sqlite3.connect('hiketrips.db') as conn:
        c = conn.cursor()
        query = 'select * from hikes where id = ?'
        c.execute(query, (hike_id,))
        return c.fetchone()

if __name__ == '__main__':
    app.debug = True
    app.run()

