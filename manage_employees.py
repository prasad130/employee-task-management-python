from db import *

def add_employee():
    connection = get_connection()
    cursor = connection.cursor()
    
    name = input('Enter employee name: ')
    role = input('Enter employee role: ')
    email = input('Enter employee email: ')
    password = input('Enter employee password: ')
    query = 'insert into employees (name,role,email,password) values (%s,%s,%s,%s)'
    values = (name,role,email,password)
    cursor.execute(query,values)
    connection.commit()

    cursor.close()
    connection.close()

def update_employee():
    connection = get_connection()
    cursor = connection.cursor()
    
    idx = int(input('Enter employee ID: '))

    query = 'select * from employees where id = %s'
    cursor.execute(query,(idx,))
    employee = cursor.fetchone()
    if employee is None:
        print(f'With Id No: {idx} employee not exist')
    else:
        select = input('What should you update(name/role/email/password): ')
        if select == 'name':
            change = input(f'Enter new {select}: ')
            query = 'update employees set name = %s where id = %s'
            values = (change,idx)

            cursor.execute(query,values)
            connection.commit()
        elif select == 'role':
            change = input(f'Enter new {select}: ')
            query = 'update employees set role = %s where id = %s'
            values = (change,idx)

            cursor.execute(query,values)
            connection.commit()
        elif select == 'email':
            change = input(f'Enter new {select}: ')
            query = 'update employees set email = %s where id = %s'
            values = (change,idx)

            cursor.execute(query,values)
            connection.commit()
        elif select == 'password':
            change = input(f'Enter new {select}: ')
            query = 'update employees set email = %s where id = %s'
            values = (change,idx)
            
            cursor.execute(query,values)
            connection.commit()
            print('EMPLOYEE UPDATED SUCCESSFULLY...')

    cursor.close()
    connection.close()

def delete_emplyee():
    connection = get_connection()
    cursor = connection.cursor()
    
    idx = int(input('Enter employee ID: '))

    query = 'select * from employees where id = %s'
    cursor.execute(query,(idx,))
    employee = cursor.fetchone()
    if employee is None:
        print(f'With Id No: {idx} employee not exist')
    else:
        query = 'delete from employees where id = %s'
        values = (idx,)
        cursor.execute(query,values)
        connection.commit()
        print('EMPLOYEE DELETED SUCCESSFULLY...')

    cursor.close()
    connection.close()

