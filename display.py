def display_tasks(tasks):

    print('-'*92)
    print('Id',' '*2,'Title',' '*10,'Description',' '*5,'Priority',' '*5,'Due Date',' '*5,'Status',' '*6,'Created at',' '*10,sep='')
    print('-'*92)
    for task in tasks:
        print(f'{task[0]: <4}{task[1]: <15}{task[2]: <16}{task[3]: <13}{str(task[4]): <13}{task[5]: <12}{str(task[6]): <20}')
    print('-'*92)

def display_employees(employees):

    print('-'*88)
    print('Id',' '*2,'Name',' '*10,'Role',' '*15,'email',' '*15,'Password',' '*5,'Created Date',sep='')
    print('-'*88)
    for employee in employees:
        print(f'{employee[0]: <4}{employee[1]: <14}{employee[2]: <19}{employee[3]: <20}{employee[4]: <13}{str(employee[5]): <18}')
    print('-'*88)

def display_comments(comments):

    print('-'*50)
    print('Id',' '*2,'Title',' '*10,'Comment',sep='')
    print('-'*50)
    for comment in comments:
        print(f'{comment[0]:<4}{comment[1]:<15}{comment[2]}')
    print('-'*50)

    
