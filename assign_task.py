from db import *

def assign_task():
    connection = get_connection()
    cursor = connection.cursor()
    
    employee_id = input('Enter employee ID: ')
    query = 'select * from employees where id = %s'
    cursor.execute(query,(employee_id,))
    res = cursor.fetchone()
    if res is None:
        print(f'Employee Id {employee_id} is not present')
        return
    
    task_id = input('Enter task ID: ')
    query = 'select * from tasks where id = %s'
    cursor.execute(query,(task_id,))
    res = cursor.fetchone()
    if res is None:
        print(f'Task Id {task_id} is not present')
        return

    query = 'insert into assigned_tasks (employee_id,task_id) values (%s,%s)'
    values = (employee_id,task_id)

    cursor.execute(query,values)
    connection.commit()
    print(f'Task Id: {task_id} assigned to employee Id: {employee_id}')

    cursor.close()
    connection.close()
    
