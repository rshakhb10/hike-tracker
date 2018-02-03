import sqlite3
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/hikes', methods = ['GET', 'POST'])
def get_all_hikes():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        d = request.form
        res = add_hike(d['name'], d['hike_date'], d['mountain'], d['comment'])
        return jsonify(res)

@app.route('/hike/<hike_id>', methods = ['GET', 'PUT', 'DELETE'])
def get_single_hike():
    pass


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

if __name__ == '__main__':
    app.debug = True
    app.run()



