'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №3.hard_ver2
Дополнительное практическое задание по модулю:"Подробнее о функциях"
ВАРИАНТ РЕШЕНИЯ 2
'''

# Реализация функции
def calculate_structure_sum(data_structure):
    count = 0 #Инициализация счетчика, как промежуточных, так и итогового подсчетов символов и суммирований чисел
    for element in data_structure: #Перебор текущего набора данных
        if isinstance(element,list) or isinstance(element,tuple) or isinstance(element,set):
            count += calculate_structure_sum(element) #Рекурсивная отправка текущего набора данных для дальнейшего детального разбора
        elif isinstance(element,dict):
            keys, values = zip(*element.items()) #Словарь, как особый случай набора данных - разбивается на два списка
            count += calculate_structure_sum(keys) #Отправка на подсчет ключей из словаря
            count += calculate_structure_sum(values) #Отправка на подсчет значений из словаря
        elif isinstance(element, str): 
            count += len(element) #Подсчет символов в строке
        elif isinstance(element, int):
            count += element #Суммирование чисел в текущем наборе     
    return count #Возврат, как промежуточных, так и итогового подсчетов символов и суммирований чисел


# Задание структуры данных
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Обращение к функции
print(calculate_structure_sum(data_structure))