import sqlite3
from sqlite3 import Error

# This function establishes connection to the SQLLite database
def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection

# Creates a table within the database to hold information
def create_table(connection, create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# Contains the SQL query used to create the specific entity and record names
def create_table_queries():
    database = "scores.db"
    sql_create_scores_table = """ CREATE TABLE IF NOT EXISTS scores (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    score integer NOT NULL
                                    ); """
    connection = create_connection(database)

    if connection is not None:

        create_table(connection, sql_create_scores_table)

    else:

        print("Error! Cannot create the database connection.")

# Returns the last row ID after using a query to insert current score into table
def create_score_query(connection, score):
    sql = ''' INSERT INTO scores(name, score)
              VALUES(?, ?) '''
    current = connection.cursor()
    current.execute(sql, score)
    connection.commit()
    return current.lastrowid

# Adds an additional row of information in the table
def add_db_row(name, score):
    database = 'scores.db'

    connection = create_connection(database)
    with connection:
        score = (name, score)
        create_score_query(connection, score)

# Retrieves the high score for all users at end of game
def retrieve_high_scores_query(connection):
    sql = ''' SELECT DISTINCT name, score FROM scores 
              WHERE score = (SELECT MAX(score) FROM scores);'''
    current = connection.cursor()
    current.execute(sql)
    records = current.fetchall()
    print("Overall High Scores")
    print("-------------------")
    for row in records:
        print("Name = ", row[0])
        print("Score = ", row[1])
        print("")

# Creates a connection to database file and runs the current high score retrieval
def retrieve_high_scores_with_names():
    database = 'scores.db'

    connection = create_connection(database)
    with connection:
        retrieve_high_scores_query(connection)

# Retrieves the current high score for the specific player playing the game
def retrieve_current_high_score_by_name_query(connection, name):
    sql = ''' SELECT MAX(score) from scores WHERE name = ?; '''
    current = connection.cursor()
    current.execute(sql, (name, ))
    records = current.fetchall()
    print("Your Current High Score")
    print("-----------------------")
    for row in records:
        print("Name = ", name)
        print("Score = ", row[0])
    print("")

# Connects with database file and obtains the current, specific player's high score
def retrieve_current_high_score_by_name(name):
    database = 'scores.db'

    connection = create_connection(database)
    with connection:
        retrieve_current_high_score_by_name_query(connection, name)
