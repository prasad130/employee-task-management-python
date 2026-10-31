from db import *

def create_task():
    connection = get_connection()
    cursor = connection.cursor()
    
    title = input('Enter task title: ')
    description = input('Enter task description: ')
    priority = input('Enter task priority: ')
    due_date = input('Enter task due date(yyyy-mm-dd): ')
    status = input('Enter task status: ')
    query = 'insert into tasks (title,description,priority,due_date,status) values (%s,%s,%s,%s,%s)'
    values = (title,description,priority,due_date,status)
    cursor.execute(query,values)
    connection.commit()
    print('TASK CREATED SUCCESSFULLY...')

    cursor.close()
    connection.close()
