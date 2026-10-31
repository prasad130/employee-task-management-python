from db import *
from find_employee_id import *

def update_task():
    
    connection = get_connection()
    cursor = connection.cursor()

    idx = int(input('Enter task ID: '))
    query = 'select * from tasks where id = %s'
    cursor.execute(query,(idx,))
    task = cursor.fetchone()
    if task is None:
        print(f'With Id No: {idx} task not exist')

    else:
        select = input('What should you update(title/description/priority/due_date/status): ')

        if select.lower() == 'title':
            update = input(f'Enter new {select}: ')
            query = 'update tasks set title = %s where id = %s'
            values = (update,idx)
            cursor.execute(query,values)
            connection.commit()
            print(f'{select} UPDATED SUCCESSFULLY...')
        
        elif select.lower() == 'description':
            update = input(f'Enter new {select}: ')
            query = 'update tasks set description = %s where id = %s'
            values = (update,idx)
            cursor.execute(query,values)
            connection.commit()
            print(f'{select} UPDATED SUCCESSFULLY...')
            
        elif select.lower() == 'priority':
            update = input(f'Enter new {select}: ')
            query = 'update tasks set priority = %s where id = %s'
            values = (update,idx)
            cursor.execute(query,values)
            connection.commit()
            print(f'{select} UPDATED SUCCESSFULLY...')
            
        elif select.lower() == 'due_date':
            update = input(f'Enter new {select}: ')
            query = 'update tasks set due_date = %s where id = %s'
            values = (update,idx)
            cursor.execute(query,values)
            connection.commit()
            print(f'{select} UPDATED SUCCESSFULLY...')
            
        elif select.lower() == 'status':
            update = input(f'Enter new {select}: ')
            query = 'update tasks set status = %s where id = %s'
            values = (update,idx)
            cursor.execute(query,values)
            connection.commit()
            print(f'{select} UPDATED SUCCESSFULLY...')
    
    cursor.close()
    connection.close()

def delete_task():

    connection = get_connection()
    cursor = connection.cursor()

    idx = int(input('Enter task ID: '))
    query = 'select * from tasks where id = %s'
    cursor.execute(query,(idx,))
    task = cursor.fetchone()
    if task is None:
        print(f'With Id No: {idx} task not exist')

    else:
        query = 'delete from tasks where id = %s'
        values = (idx,)
        cursor.execute(query,values)
        connection.commit()
        print(f'Id No: {idx} TASK DELETED SUCCESSFULLY')

    cursor.close()
    connection.close()

def update_task_status(name, password):

    connection = get_connection()
    cursor = connection.cursor()

    idx = emp_id(name,password)

    option = int(input('Enter task id: '))
    query = 'select * from tasks where id = %s'
    cursor.execute(query,(option,))
    task = cursor.fetchone()

    if task is None:
        print(f'With Id No: {option} task not exist')

    else:
        update = input('Enter new status: ')
        query = 'update tasks set status = %s where id = %s'
        values = (update,option)
        cursor.execute(query,values)
        connection.commit()
        print('UPDATED SUCCESSFULLY...')

    cursor.close()
    connection.close()
    



    
