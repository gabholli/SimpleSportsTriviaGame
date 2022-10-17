import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection


def create_table(connection, create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


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


def create_score_query(connection, score):
    sql = ''' INSERT INTO scores(name, score)
              VALUES(?, ?) '''
    current = connection.cursor()
    current.execute(sql, score)
    connection.commit()
    return current.lastrowid


def add_db_row(name, score):
    database = 'scores.db'

    connection = create_connection(database)
    with connection:
        score = (name, score)
        create_score_query(connection, score)


def retrieve_high_scores_query(connection):
    sql = ''' SELECT name, score FROM scores 
              WHERE score = (SELECT MAX(score) FROM scores);'''
    current = connection.cursor()
    current.execute(sql)
    records = current.fetchall()
    print("Current High Scores")
    print("-------------------")
    for row in records:
        print("Name = ", row[0])
        print("Score = ", row[1])


def retrieve_high_scores_with_names():
    database = 'scores.db'

    connection = create_connection(database)
    with connection:
        retrieve_high_scores_query(connection)
