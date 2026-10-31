from db import *
from find_employee_id import *

def my_profile(name,password):

    connection = get_connection()
    cursor = connection.cursor()

    idx = emp_id(name,password)
    query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s
            '''
    cursor.execute(query,(idx,))
    total_tasks = cursor.fetchone()

    query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
            '''
    cursor.execute(query,(idx,'completed'))
    completed_tasks = cursor.fetchone()

    query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
            '''
    cursor.execute(query,(idx,'in progress'))
    progress_tasks = cursor.fetchone()

    query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
            '''
    cursor.execute(query,(idx,'pending'))
    pending_tasks = cursor.fetchone()

    query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
            join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
            '''
    cursor.execute(query,(idx,'on hold'))
    hold_tasks = cursor.fetchone()
    
    print('Name: ',name,' '*5,'Password: ',password,sep='')
    print('Total Tasks: ', total_tasks[0],sep='')
    print('Completed Tasks: ',completed_tasks[0],sep='')
    print('In Progress Tasks: ',progress_tasks[0],sep='')
    print('Pending Tasks: ',pending_tasks[0],sep='')
    print('On Hold Tasks: ',hold_tasks[0],sep='')

    cursor.close()
    connection.close()
               
