# Original code: Function that performs a database query
import sqlite3

def connect_database(db):
    connection = sqlite3.connect(db)
    return connection

def query_database(sql, connection = None):
    if connection is None:
        raise TypeError("A valid database connection is required.")
    # connection - a live communication channel between the app and the database
    conn = connect_database('example.db')
    # cursor - used to traverse and manipulate results returned by a query
    cursor = conn.cursor()
    # we pass a string named 'sql' that contains our SQL query
    cursor.execute(sql)
    # fetchall - returns a list of tuples containing all rows of our result
    result = cursor.fetchall()
    conn.close()
    return result
