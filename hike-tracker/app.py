from flask import Flask
app = Flask(__name__)


@app.route('/hikes', methods = ['GET', 'POST'])
def get_all_hikes():
	pass

@app.route('/hike/<hike_id>', methods = ['GET', 'PUT', 'DELETE'])
def get_single_hike():
	pass

if __name__ = '__main__':
	app.run()



