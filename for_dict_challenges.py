# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names_students = []
for student in students:
    name_student = student['first_name']
    amount_name = 0
    for student in students:
        if name_student == student['first_name']:
            amount_name += 1
    answer = f'{name_student}: {amount_name}'
    if names_students == False:
        names_students.append(answer)
    elif answer in names_students:
        pass
    else:
        names_students.append(answer)
print('\n'.join(names_students))

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names_students = {}
for student in students:
    name_student = student['first_name']
    amount_name = 0
    for student in students:
        if name_student == student['first_name']:
            amount_name += 1
    if names_students == False:
        names_students[name_student] = amount_name
    elif answer in names_students:
        pass
    else:
        names_students[name_student] = amount_name

counter = 0
for key, value in names_students.items():
    if value > counter:
        search_name = key
        counter = value
print(f'Самое частое имя среди учеников: {search_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

number_class = 1
for students in school_students:
    names_students = {}
    for student in students:
        name_student = student['first_name']
        amount_name = 0
        for student in students:
            if name_student == student['first_name']:
                amount_name += 1
        if names_students == False:
            names_students[name_student] = amount_name
        elif answer in names_students:
            pass
        else:
            names_students[name_student] = amount_name
    counter = 0
    for key, value in names_students.items():
        if value > counter:
            search_name = key
            counter = value
    print(f'Самое частое имя в классе {number_class}: {search_name}')
    number_class += 1

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_in_school in school:
    amount_m = 0
    amount_f = 0
    for students in class_in_school['students']:
        if is_male[students['first_name']] == True:
            amount_m += 1
        else:
            amount_f += 1
    print(f'Класс {class_in_school["class"]}: девочки {amount_f}, мальчики {amount_m}.')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for class_in_school in school:
    amount_m = 0
    amount_f = 0
    for students in class_in_school['students']:
        if is_male[students['first_name']] == True:
            amount_m += 1
        else:
            amount_f += 1
    print(f'Класс {class_in_school["class"]}: девочки {amount_f}, мальчики {amount_m}.')
