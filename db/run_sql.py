# using postgres
import sys
import psycopg2  
import psycopg2.extras as ext

def run_sql2(sql, values = None):
    conn = None
    results = []
    
    try:
        conn=psycopg2.connect("dbname='soloproject' user=postgres password=password")
        cur = conn.cursor(cursor_factory=ext.DictCursor)   # ensures the results are placed into a dict with the column names as the key
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results


# psycopg2 returns psql.DATETIME as datetime.date
# psycopg2 returns psql.TIMESTAMP as datetime.datetime


#############################################################################
# using sqlite
import sqlite3, os.path


# need to be careful with the path to the db file!
# if it doesn't exist sqlite will not give a warning
# and instead just create a temporary db with the same name.
# your commands will try to execute as normal and the first warning will be that
# the given table doesn't exist. check if the db file exists before creating the connection

# notes:
# had to remove the explicit conn.commit(). sqlite uses autocommit
# in cur.execute(), the string placeholder '%s' has to be changed to '?'
# in cur.execute(), the values needs to be a tuple instead of a list

db_path = r"db\sqlite_soloproject.db"
assert os.path.exists(db_path) and os.path.isfile(db_path)

def run_sql(sql, values = None):
	results = []
	sql = sql.replace("%s", "?")
	if values is None:
		values = []
	values = tuple(values)
	
	with sqlite3.connect(db_path) as con:
		con.row_factory = sqlite3.Row	# ensures the results are placed into a dict with the column names as the key. without this
		cur = con.cursor()				# the results are just a list of values with no indication what column they relate to
		cur.execute(sql, values)
		results = cur.fetchall()
	return results