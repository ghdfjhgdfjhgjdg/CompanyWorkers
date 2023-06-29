employees = {
    "Jonh": {
        "position": "developer",
        "salary": 25000,
        "start_date": "2023-01-01"
    },
    "Alex": {
        "position": "manager",
        "salary": 15000,
        "start_date": "2023-01-01"
    },
    "Cat": {
        "position": "manager",
        "salary": 15000,
        "start_date": "2023-01-01"
    },
    "Fredo": {
        "position": "cleaner",
        "salary": 6000,
        "start_date": "2023-01-01"
    },
    "Merphy": {
        "position": "doctor",
        "salary": 10000,
        "start_date": "2023-01-01"
    }
}

while True:
    get_info = input('Введіть команду: ')
    if get_info == 'add':

        add_worker_name = input("Введіть ім'я: ")
        if add_worker_name == '' or add_worker_name == 'quit':
            break
        add_worker_position = input("Введіть позицію вашого працівника: ")
        add_worker_salary = input("Введіть зарплату вашого працівника: ")
        add_worker_start_date = input("Введіть дату початку роботи вашого працівника: ")
        employees[add_worker_name] = {
            'position': add_worker_position,
            'salary': add_worker_salary,
            'start_date': add_worker_start_date
        }

    if get_info == 'remove':
        while True:
            del_item_name = input('Введіть імя для видалення: ')
            if del_item_name in employees:
                del employees[del_item_name]
                print('Користувача не знайдено!')
                break
    print(employees)









