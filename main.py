from dashboard import *
from manage_employees import *
from create_task import *
from assign_task import *
from view_tasks_with_filters import *
from reports import *
from modify import *
from display import *
from login import *
from comments import *
from profile import *

while True:
    login_type = input('Enter Login Type(admin/employee): ')
    if login_type.lower() == 'admin':
        while True:
            print('='*30)
            print('1. Dashboard\n2. Manage Employees\n3. Create Task\n4. Assign Task\n5. View All Tasks By Filters'
                  '\n6. Reports & Analytics\n7. Task Update/Delete\n8. Logout')
            print('='*30)
            option = int(input('Enter your choice: '))
            print('='*30)
            match (option):
                case 1:
                    print('1. View Tasks\n2. View Employees\n3. View Completed Tasks\n4. View Pending Tasks')
                    print('='*30)
                    option = int(input('Enter your choice: '))
                    print('='*30)
                    if option == 1:
                        tasks()
                    elif option == 2:
                        employees()
                    elif option == 3:
                        completed_tasks()
                    elif option == 4:
                        pending_tasks()
                    else:
                        print('Invalid Input')
                case 2:
                    print('1. Add Employee\n2. Update Employee\n3. Delete Employee\n4. View Employee List')
                    print('='*30)
                    option = int(input('Enter your choice: '))
                    print('='*30)
                    if option == 1:
                        add_employee()
                    elif option == 2:
                        update_employee()
                    elif option == 3:
                        delete_emplyee()
                    elif option == 4:
                        employees()
                    else:
                        print('Invalid Input')
                case 3:
                    create_task()
                case 4:
                    assign_task()
                case 5:
                    print('1. View tasks by status\n2. View tasks by priority\n3. view task by dates\n4. view task by employee')
                    print('='*30)
                    select = int(input('Enter your choice: '))
                    print('='*30)
                    if select == 1:
                        view_by_status()
                    elif select == 2:
                        view_by_priority()
                    elif select == 3:
                        view_by_dates()
                    elif select == 4:
                        employees()
                        view_by_employee()
                    else:
                        print('Invalid Input')
                case 6:
                    print('1. Task status report\n2. Employee performance report\n3. Overdue tasks')
                    print('='*30)
                    select = int(input('Enter your choice: '))
                    print('='*30)
                    if select == 1:
                        task_status()
                    elif select == 2:
                        employee_performance()
                    elif select == 3:
                        overdue_tasks()
                    else:
                        print('Invalid Input')
                case 7:
                    print('1. Update The Task\n2. Delete The Task')
                    print('='*30)
                    option = int(input('Enter your choice: '))
                    print('='*30)
                    if option == 1:
                        tasks()
                        update_task()
                    elif option == 2:
                        tasks()
                        delete_task()
                    else:
                        print('Invalid Input')
                case 8:
                    print('Logout SUCCESSFULLY...')
                    break
                case _ :
                    print('Invalid Input')
    elif login_type.lower() == 'employee':
        print('='*30)
        name = input('Enter your name: ')
        password = input('Enter your password: ')
        if login(name,password):
            while True:
                print('='*30)
                print('1. Dashboard\n2. My Tasks\n3. Task Details\n4. Update Task Status\n5. Comments\n'
                      '6. View Completed Tasks\n7. Profile\n8. Logout''')
                print('='*30)
                option = int(input('Enter your choice: '))
                print('='*30)
                match (option):
                    case 1:
                        print('1. View tasks assinged to me\n2. View summary of my progress')
                        print('='*30)
                        option = int(input('Enter your choice: '))
                        print('='*30)
                        if option == 1:
                            tasks_assigned_to_me(name,password)
                        elif option == 2:
                            my_progress_summary(name,password)
                        else:
                            print('Invalid Input')
                    case 2:
                        print('1. List of tasks assigned\n2. Filter by status\n3. Filter by priority')
                        print('='*30)
                        option = int(input('Enter your choice: '))
                        print('='*30)
                        if option == 1:
                            tasks_assigned_to_me(name,password)
                        elif option == 2:
                            filter_by_status(name,password)
                        elif option == 3:
                            filter_by_priority(name,password)
                        else:
                            print('Invalid Input')
                    case 3:
                        tasks()
                    case 4:
                        tasks_assigned_to_me(name,password)
                        update_task_status(name,password)
                    case 5:
                        print('1. Add Comments\n2. View Comments')
                        print('='*30)
                        option = int(input('Enter your choice: '))
                        print('='*30)
                        if option == 1:
                            tasks_assigned_to_me(name,password)
                            add_comments(name,password)
                        elif option == 2:
                            view_comments(name,password)
                        else:
                            print('Invalid Input')
                    case 6:
                        view_completed_tasks(name,password)
                    case 7:
                        my_profile(name,password)
                    case 8:
                        print('Logout SUCCESSFULLY...')
                        break
        else:
            print('User not found')
    elif login_type.lower() == 'done':
        break
    else:
        print('Invalid input')
