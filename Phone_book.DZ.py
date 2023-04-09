# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных



def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    # print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    # print(new_item)
    # print(data_array)
    data_array.append(new_item)
    # print(data_array)
    write_file(filename, data_array)

def change_item(filename, id, data):
    data_array = read_file(filename)
    for i in range(1,len(data_array)):
        if data_array[i][0] == id:
            if data == 1:
                data_array[i][1] = input('Фамилия:     ')
            elif data == 2:
                data_array[i][2] = input('Имя:     ')
            elif data == 3:
                data_array[i][3] = input('Отчество:     ')
            elif data == 4:
                data_array[i][4] = input('Телефон:     ')
            elif data == 5:
                data_array[i][1] = input('Фамилия:     ')
                data_array[i][2] = input('Имя:     ')
                data_array[i][3] = input('Отчество:     ')
                data_array[i][4] = input('Телефон:     ')
    write_file(filename, data_array)


def delete_item(filename, id):
    data_array = read_file(filename)
    for i in range(1,len(data_array)):
        if data_array[i][0] == id:
            del data_array[i]
    write_file(filename, data_array)


def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(1,len(data_array)):
        print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1],"Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])


def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input('Выберите действие: '))

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
        show_all_items(filename)
    elif user_operation == 3:
        user_id = input('Введите ID изменяемой записи: ')
        print('1 - Изменить Фамилию')
        print('2 - Изменить Имя')
        print('3 - Изменить Отчество')
        print('4 - Изменить телефон')
        print('5 - Изменить все данные')
        user_change = int(input())
        change_item(filename, user_id, user_change)
        show_all_items(filename)
    elif user_operation == 4:
        user_id = input('Укажите ID удаляемой записи: ')
        delete_item(filename, user_id)
        show_all_items(filename)


filename = 'file_1.txt'
menu()