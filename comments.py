from find_employee_id import *
from display import *

def add_comments(name,password):

    connection = get_connection()
    cursor = connection.cursor()
    
    idx = emp_id(name,password)
    task_id = int(input('Enter task Id: '))
    comment = input('Enter comment: ')

    query = 'insert into comments (task_id,employee_id,comment) values (%s,%s,%s)'
    values = (task_id,idx,comment)

    cursor.execute(query,values)
    connection.commit()

    print('COMMENT ADDED SUCCESSFULLY...')

    cursor.close()
    connection.close()
    
def view_comments(name,password):

    connection = get_connection()
    cursor = connection.cursor()

    idx = emp_id(name,password)
    query = '''select t.id, t.title, c.comment from employees e join comments c on e.id = c.employee_id join
            tasks t on t.id = c.task_id where e.id = %s
            '''
    cursor.execute(query,(idx,))
    comments = cursor.fetchall()

    if not comments:
        print('Data not found')
    else:
        display_comments(comments)

    cursor.close()
    connection.close()
    
