import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '0103',
        database = 'task_management_system'
    )
    return connection
