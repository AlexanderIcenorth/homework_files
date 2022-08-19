from pprint import pprint

# Первая задача

# Первая строка в файле упорно не читается! Не могу понять ЧЯДНТ.
# Пока, как костыль, сделал в файле recipes.txt отступ на одну строку. Так работает верно.
# Но понять, в каком месте я туплю всё же хочется.


def cook_book():
    '''
    Открытие файла с рецептами и запись его содержимого в словарь указанного в задаче вида
    '''
    with open ('recipes.txt', 'r', encoding = 'utf-8-sig') as file:
        
        cook_book = {}

        for any in file:
            rec_one_dish = []
            dish_name = file.readline().rstrip('\n')
            quantity = file.readline().rstrip('\n')
            for lines in range(int(quantity)):
                recipe_attribs = file.readline().split(' | ')
                rec_one_dish.append({'ingredient_name' : recipe_attribs[0], 'quantity' : recipe_attribs[1],\
                     'measure' : recipe_attribs[2].rstrip('\n')})
        
            cook_book[dish_name] = rec_one_dish
            
    return cook_book


print('Результат выполнения первой задачи:\n')
pprint(cook_book())
print()

# Вторая задача
# Вводные данные для второй задачи:
dishes_list = ['Омлет', 'Фахитос', 'Запеченный картофель']
person = 3


def get_shop_list_by_dishes(dishes, person_count):
    '''
    Cоздание словаря с нужным количеством ингредиентов на указаное количество персон
    '''

    # Сначала отделяем нужные рецепты от всех остальных в отдельный словарь:   
    all_dishes = cook_book()
    desired_dishes = {}

    for recipe_name, recipe_ingrids in all_dishes.items():
        if recipe_name in dishes:
            desired_dishes.update({recipe_name : recipe_ingrids})             
   
    # Теперь создаём словарь со всеми ингредиентами из него:
    result_dict_for_one = {}
   
    for ingrids_list in desired_dishes.values():
        for ingrids_attribs in ingrids_list:
            if ingrids_attribs['ingredient_name'] not in result_dict_for_one:
                result_dict_for_one.update({ingrids_attribs['ingredient_name'] : {'measure' : ingrids_attribs['measure'],\
                     'quantity' : int(ingrids_attribs['quantity'])}}) # И они мне говорят что в Питоне мало синтаксиса! :D
            else:
                a = int(result_dict_for_one[ingrids_attribs['ingredient_name']]['quantity'])
                b = int(ingrids_attribs['quantity'])
                new_quantity = a + b
                result_dict_for_one.update({ingrids_attribs['ingredient_name'] : {'measure' : ingrids_attribs['measure'],\
                     'quantity' : new_quantity}})
    
    # И умножаем количество ингредиентов на количество персон:
    result_dict = {}

    for ingrid_name, ingrid_attribs in result_dict_for_one.items():
        result_dict.update({ingrid_name : {'quantity' : ingrid_attribs['quantity'] * person_count,\
             'measure' : ingrid_attribs['measure']}})

    return result_dict

          
print(f'Pезультат выполнения второй задачи для {person} персон:\n')
pprint(get_shop_list_by_dishes(dishes_list, person))
print()


# Третья задача
def open_files_to_lists():
    '''
    Извлечение данных из файлов 1.txt 2.txt 3.txt в списки list1 list2 list3 cоотвественно.
    Cравнение количества строк в них.
    Запись в итоговый файл указаного в задаче формата.
    '''
    # Извлекаем данные из файлов в списки.
    with open ('1.txt', 'r', encoding = 'utf-8-sig') as file1:
        intermediate_list1 = file1.readlines()
        list1 = []
        for line in intermediate_list1:
            list1.append(line.rstrip('\n'))
    
    with open ('2.txt', 'r', encoding = 'utf-8-sig') as file2:
        intermediate_list2 = file2.readlines()
        list2 = []
        for line in intermediate_list2:
            list2.append(line.rstrip('\n'))
    
    with open ('3.txt', 'r', encoding = 'utf-8-sig') as file3:
        intermediate_list3 = file3.readlines()
        list3 = []
        for line in intermediate_list3:
            list3.append(line.rstrip('\n'))
            
    # Определяем очерёдность записи. Создаём служебную информацию.
    len_list = [len(list1), len(list2), len(list3)]
    
    if min(len_list) == len(list1):
        first_value = list1
        first_name = '1.txt'
        first_len = str(len(list1))
        len_list.remove(len(list1))
    elif min(len_list) == len(list2):
        first_value = list2
        first_name = '2.txt'
        first_len = str(len(list2))
        len_list.remove(len(list2))
    else:
        first_value = list3
        first_name = '3.txt'
        first_len = str(len(list3))
        len_list.remove(len(list3))

    if min(len_list) == len(list1):
        mid_value = list1
        mid_name = '1.txt'
        mid_len = str(len(list1))
        len_list.remove(len(list1))
    elif min(len_list) == len(list2):
        mid_value = list2 
        mid_name = '2.txt'
        mid_len = str(len(list2))
        len_list.remove(len(list2))
    else:
        mid_value = list3
        mid_name = '3.txt'
        mid_len = str(len(list3))
        len_list.remove(len(list3))
    
    if len_list[0] == len(list1):
        last_value = list1
        last_name = '1.txt'
        last_len = str(len(list1))
    elif len_list[0] == len(list2):
        last_value = list2
        last_name = '2.txt'
        last_len = str(len(list2))
    else:
        last_value = list3
        last_name = '3.txt'
        last_len = str(len(list3))
    
    # Записываем всё в итоговый файл.
    with open ('result.txt', 'w', encoding = 'utf-8') as target:
        target.write(f'{first_name}\n')
        target.write(f'{first_len}\n')
        for string in first_value:
            target.write(f'{string}\n')
        target.write(f'{mid_name}\n')
        target.write(f'{mid_len}\n')
        for string in mid_value:
            target.write(f'{string}\n')
        target.write(f'{last_name}\n')
        target.write(f'{last_len}\n')
        for string in last_value:
            target.write(f'{string}\n')



open_files_to_lists()