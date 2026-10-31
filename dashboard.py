from db import *
from display import *
from find_employee_id import *

''' Admin Section '''

def tasks():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('select * from tasks')
    tasks = cursor.fetchall()
    display_tasks(tasks)
    
    cursor.close()
    connection.close()

def employees():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('select * from employees')
    employees = cursor.fetchall()
    display_employees(employees)

    cursor.close()
    connection.close()

def completed_tasks():
    connection = get_connection()
    cursor = connection.cursor()
    
    query = 'select * from tasks where status = %s'
    cursor.execute(query,('completed',))
    tasks = cursor.fetchall()

    if not tasks:
        print('Data not found')
    else:
        display_tasks(tasks)

    cursor.close()
    connection.close()

def pending_tasks():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('select * from tasks where status = %s', ('pending',))
    tasks = cursor.fetchall()
    if not tasks:
        print('Data not found')
    else:
        display_tasks(tasks)

    cursor.close()
    connection.close()

''' Employee Section '''

def tasks_assigned_to_me(name,password):

    connection = get_connection()
    cursor = connection.cursor()

    idx = emp_id(name,password)
    
    query = '''
            select t.* from employees e join assigned_tasks a
            on e.id = a.employee_id join tasks t on t.id = a.task_id where e.id = %s
            order by t.id
            '''
    values = (idx,)
    cursor.execute(query,values)
    tasks = cursor.fetchall()
    display_tasks(tasks)

    cursor.close()
    connection.close()

def my_progress_summary(name,password):

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

    print('Completed tasks')
    if not tasks:
        print('-'*30)
        print('No data found')
        print('-'*30)
    else:
        display_tasks(tasks)

    query = '''
            select t.* from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
            '''
    values = (idx,'In Progress')
    cursor.execute(query,values)
    tasks = cursor.fetchall()

    print('In Progress tasks')
    if not tasks:
        print('-'*30)
        print('No data found')
        print('-'*30)
    else:
        display_tasks(tasks)

    query = '''
            select t.* from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
            '''
    values = (idx,'Pending')
    cursor.execute(query,values)
    tasks = cursor.fetchall()

    print('Pending tasks')
    if not tasks:
        print('-'*30)
        print('No data found')
        print('-'*30)
    else:
        display_tasks(tasks)

    query = '''
            select t.* from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
            '''
    values = (idx,'On Hold')
    cursor.execute(query,values)
    tasks = cursor.fetchall()

    print('On Hold tasks')
    if not tasks:
        print('-'*30)
        print('No data found')
        print('-'*30)
    else:
        display_tasks(tasks)
        
    cursor.close()
    connection.close()









    
