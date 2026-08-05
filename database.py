import mysql.connector

def connect_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aswinkumartn74",      # Put your MySQL password here if you have one
        database="placement"
    )
    return connection