import sqlite3

def create_db():
    with sqlite3.connect('hiketrips.db') as conn:
        c = conn.cursor()
        c.execute(create_hike_table())
        c.execute(create_mountain_table())
    return True 

def create_hike_table():
    hike_table_query = '''create table hikes(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		hike_name NOT NULL,
		hike_date TEXT,
		mountain_id INTEGER,
		comment BLOB
	);'''
    return hike_table_query

def create_mountain_table():
    mountain_table_query = '''create table mountains(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		mountain TEXT NOT NULL,
		elevation REAL NOT NULL,
		country TEXT NOT NULL,
		state TEXT
	);'''
    return mountain_table_query

if __name__ == '__main__':
    create_db()
	