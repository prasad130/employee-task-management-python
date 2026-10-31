from db import *
from display import *
from find_employee_id import *

''' Admin Section '''

def view_by_status():
    
    connection = get_connection()
    cursor = connection.cursor()
    
    status = input('Enter status(pending/completed/in progress/on hold): ')
    query = 'select * from tasks where status = %s'
    values = (status,)
    cursor.execute(query,values)
    tasks = cursor.fetchall()
    
    if not tasks:
        print('Data not found')
    else:
        display_tasks(tasks)

    cursor.close()
    connection.close()

def view_by_priority():
    
    connection = get_connection()
    cursor = connection.cursor()
    
    priority = input('Enter priority(high/medium/low): ')
    query = 'select * from tasks where priority = %s'
    values = (priority,)
    cursor.execute(query,values)
    tasks = cursor.fetchall()

    if not tasks:
        print('Data not found')
    else:
        display_tasks(tasks)

    cursor.close()
    connection.close()

def view_by_dates():
    
    connection = get_connection()
    cursor = connection.cursor()
    
    start_date = input('Enter start date(yyyy-mm-dd): ')
    end_date = input('Enter end date(yyyy-mm-dd): ')
    query = 'select * from tasks where due_date between %s and %s'
    values = (start_date,end_date)
    cursor.execute(query,values)
    tasks = cursor.fetchall()

    display_tasks(tasks)

    cursor.close()
    connection.close()


def view_by_employee():
    
    connection = get_connection()
    cursor = connection.cursor()
    
    idx = int(input('Enter employee ID: '))
    query = '''select t.id, t.title, t.description, t.priority, t.due_date, t.status, t.created_at from
                tasks t join assigned_tasks a on t.id = a.task_id where a.employee_id = %s'''
    values = (idx,)
    cursor.execute(query,values)
    tasks = cursor.fetchall()
    
    if not tasks:
        print('Data not found')
    else:
        display_tasks(tasks)

    cursor.close()
    connection.close()
    
''' Employee Section '''

def filter_by_status(name,password):

    connection = get_connection()
    cursor = connection.cursor()

    idx = emp_id(name, password)

    status = input('Enter status: ')

    if status.lower() in ['completed', 'in progress', 'pending', 'on hold']:

        query = '''
                select t.* from employees e join assigned_tasks a on e.id = a.employee_id
                join tasks t ON t.id = a.task_id where e.id = %s and t.status = %s
                '''

        values = (idx, status.title())

        cursor.execute(query, values)

        tasks = cursor.fetchall()

        if not tasks:
            print('No tasks found.')
        else:
            display_tasks(tasks)

    else:
        print('Invalid Input')

    cursor.close()
    connection.close()

def filter_by_priority(name,password):

    connection = get_connection()
    cursor = connection.cursor()

    idx = emp_id(name,password)
    priority = input('Enter priority: ')

    if priority.lower() in ['low','high','medium']:
        query = '''
                select t.* from employees e join assigned_tasks a on e.id = a.employee_id join tasks t on t.id = a.task_id
                where e.id = %s and t.priority = %s
                '''
        values = (idx,priority)
        cursor.execute(query,values)
        tasks = cursor.fetchall()

        if not tasks:
            print('No tasks found.')
        else:
            display_tasks(tasks)

    else:
        print('Invalid Input')
        
    cursor.close()
    connection.close()
        
def view_completed_tasks(name,password):
    connection = get_connection()
    cursor = connection.cursor()

    idx = emp_id(name,password)

    query = '''
            select t.* from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
            '''
    values = (idx,'completed')

    cursor.execute(query,values)

    tasks = cursor.fetchall()

    if not tasks:
            print('No tasks found.')
    else:
        display_tasks(tasks)
    











