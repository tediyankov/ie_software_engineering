import pytest
import sqlite3
from pathlib import Path
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from inflammation.sqlite_example import connect_database, query_database

@pytest.fixture()
def database_fn_fixture(tmp_path_factory):
    yield tmp_path_factory.mktemp("data") / "test.db"

@pytest.fixture()
def database_connection():
    """Fixture that provides a clean database connection."""
    db_path = 'test.db'
    # remove existing test database if it exists
    if Path(db_path).exists():
        Path(db_path).unlink()
    
    # making connection using connect_database function
    conn = connect_database(db_path)
    
    yield conn
    
    # teardown: close connection and delete test database file
    conn.close()
    if Path(db_path).exists():
        Path(db_path).unlink()

@pytest.fixture()
def setup_database(database_connection):
    """Fixture that provides a database connection with populated data."""
    conn = database_connection
    
    # populating the database with test data
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Animals(Name, Species, Age)")
    cursor.execute("INSERT INTO Animals VALUES ('Bugs', 'Rabbit', 6)")
    cursor.execute("INSERT INTO Animals VALUES ('Tweety', 'Bird', 3)")
    cursor.execute("INSERT INTO Animals VALUES ('Sylvester', 'Cat', 5)")
    
    # returning the connection with populated data
    return conn

def test_connect_to_db_type():
    """
    Test that connect_to_database function returns sqlite3.Connection
    """
    conn = connect_database('test.db')
    assert isinstance(conn, sqlite3.Connection)
    conn.close()

def test_connect_to_db_name():
    """
    Test that connect_to_database function connects to correct DB file
    """
    conn = connect_database('test.db')
    cur = conn.cursor()
    # List current databases https://www.sqlite.org/pragma.html#pragma_database_list
    cur.execute('PRAGMA database_list;')
    # Unpack the three parameters returned
    db_index, db_type, db_filepath = cur.fetchone()
    # Extract just the filename from the full filepath
    db_filename = Path(db_filepath).name
    assert db_filename == 'test.db'
    conn.close()

def test_query_database(setup_database):
    """
    Test that query_database retrieves the correct data
    """
    # using the connection from the fixture
    conn = setup_database
    
    # creating table and insert data using the fixture connection
    cur = conn.cursor()
    cur.execute("CREATE TABLE Animals(Name, Species, Age)")
    cur.execute("INSERT INTO Animals VALUES ('Bugs', 'Rabbit', 6)")
    
    # using query_database to retrieve data
    sql = "SELECT * FROM Animals"
    result = query_database(sql, connection=conn)
    
    # Result returned is a list (cursor.fetchall)
    assert isinstance(result, list)
    # There should just be one record
    assert len(result) == 1
    # That record should be the data we added
    assert result[0] == ("Bugs", "Rabbit", 6)

def test_query_database_without_connection():
    """
    Test the `query_database` function without a provided connection
    """
    sql = 'SELECT * FROM Animals'
    # ensure that we get a TypeError
    with pytest.raises(TypeError):
        query_database(sql)
