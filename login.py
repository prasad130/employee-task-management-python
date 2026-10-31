from db import *

def login(name,password):
    connection = get_connection()
    cursor = connection.cursor()

    query = 'select * from employees where name = %s and password = %s'
    cursor.execute(query,(name,password))
    employee = cursor.fetchone()

    if employee is None:
        return False
    return True
