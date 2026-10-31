from db import *

def emp_id(name,password):
    connection = get_connection()
    cursor = connection.cursor()

    query = 'select id from employees where name = %s and password = %s'
    values = (name,password)

    cursor.execute(query,values)
    return cursor.fetchone()[0]
