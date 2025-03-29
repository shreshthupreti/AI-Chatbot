import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Change if needed
        password="password",  # Change if needed
        database="learning_platform"
    )
