from db import *
from display import *

def task_status():
    
    connection = get_connection()
    cursor = connection.cursor()

    query = 'select * from tasks'
    cursor.execute(query)
    tasks = cursor.fetchall()

    if not tasks:
        print('Data not found')
    else:
        print('-'*31)
        print('task',16*' ','status',sep='')
        print('-'*31)
        for task in tasks:
            title = task[1]
            status = task[5]
            print(f'{title:<20}{status}')
        print('-'*31)
    
    cursor.close()
    connection.close()

def overdue_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    query = '''select * from tasks where due_date < curdate() and status != 'Completed' '''
    cursor.execute(query)

    tasks = cursor.fetchall()

    if not tasks:
        print('Data not found')
    else:
        display_tasks(tasks)

    cursor.close()
    connection.close()

def employee_performance():

    connection = get_connection()
    cursor = connection.cursor()

    query = 'select * from employees'
    cursor.execute(query)
    employees = cursor.fetchall()

    print('-'*91)
    print('Id',' '*2,'Name',' '*10,'Total Tasks ','Completed Tasks ','In Progress Tasks ','Pending Tasks ','On Hold Tasks',sep='')
    print('-'*91)
    for employee in employees:
        idx = employee[0]
        name = employee[1]

        query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
                join tasks t on t.id = a.task_id where e.id = %s
                '''
        cursor.execute(query,(idx,))
        total_tasks = cursor.fetchone()[0]

        query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
                join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
                '''
        cursor.execute(query,(idx,'completed'))
        completed_tasks = cursor.fetchone()[0]

        query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
                join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
                '''
        cursor.execute(query,(idx,'in progress'))
        progress_tasks = cursor.fetchone()[0]

        query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
                join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
                '''
        cursor.execute(query,(idx,'pending'))
        pending_tasks = cursor.fetchone()[0]

        query = '''select count(*) from employees e join assigned_tasks a on e.id = a.employee_id
                join tasks t on t.id = a.task_id where e.id = %s and t.status = %s
                '''
        cursor.execute(query,(idx,'on hold'))
        hold_tasks = cursor.fetchone()[0]

        print(f'{idx:<4}{name:<14}{total_tasks:<12}{completed_tasks:<16}{progress_tasks:<18}{pending_tasks:<14}{hold_tasks:<13}')
    print('-'*91)
        







