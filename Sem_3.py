# 1.Задайте список, состоящий из произвольных чисел,
# количество задает пользователь. Напишите программу,
# определяющую присутствует ли в заданном списке число,
# полученное от пользователя.
# simple из random (собираем список)
# simple - формирует не повторяющиеся последовательности
# simple - принимает два аргумента (последовательность
# чисел и количество сколько мы хотим взять из этой 
# последовательности)
# функция
# from random import sample ## берем из библиотеки
#range - формирует последовательность
# in - это оператор, который проверяет входит ли (в) ...
# def num_find(dlina_spiska, chislo):
#     now_spisok = sample(range(1, dlina_spiska * 2), k=dlina_spiska)
#     print(now_spisok)
#     if chislo in now_spisok:
#         return 'Yes'
#     return 'No' 

# print (num_find (int(input('Введите длину списка: ')),  int(input('Введите число: '))))

# 2.Задайте список, состоящий из произвольных слов,
# количество задает пользователь. Напишите программу,
# которая определит индекс второго вхождения строки 
# в списке либо сообщит, что ее нет. 
# сообщит, что ее нет это (-1) - это маркер
#здесь получается две задачи:
# во - первых это сформировать(выделяем это в отдельную функцию)
# собираем с помощью sample в цикле
# во - вторых это поиск(функция поиска второго вхождения)
# воспользуемся встроенным методом который ищет вхождение 
# элементов в структуру

# from random import sample
# def spisok(count, word = 'abc'):
#     now_spisok = []
#     for i in range(count):
#         vremen = sample(word, k=3)
#         now_spisok.append("".join(vremen))
#     return now_spisok
# def index_find(word_2, now_list):
#     if word_2 in now_list and now_list.count(word_2)>1:
#         index_1 = now_list.index(word_2)
#         print(now_list.index(word_2, index_1+1)) 
#     else:
#         print(-1)
# list_1 = spisok(int(input()))              
# print (list_1)
# index_find(input(), list_1)  
print(0)   



