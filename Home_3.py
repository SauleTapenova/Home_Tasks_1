# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на
# нечётных позициях(не индексах).

# from random import sample
# sum = 0
# def new_spisok(len_spiska):
#     m = []
#     a = sample(range(1, len_spiska * 2), k=len_spiska)
#     print (a)
#     return a
# def find_sum_index(massiv,len_spiska):
#     sum =0
#     for i in range(1, len_spiska+1,2):
#         sum = sum + massiv[i-1]
#     print(sum)
              
# len_spiska = int(input())
# massiv = new_spisok(len_spiska)
# find_sum_index(massiv, len_spiska)

# 2. Напишите программу, которая найдёт произведение 
# пар чисел списка.Парой считаем первый и последний
#  элемент, второй и предпоследний и т.д.
# from random import sample
# arr = 0
# def new_spisok(len_spiska):
#     m = []
#     a = sample(range(1, len_spiska * 2), k=len_spiska)
#     print (a)
#     return a
    
# def find_proiz(arr,len_spiska):
#     a = len_spiska % 2
#     if a!=0:
#         v = [1]*(len_spiska //2+1)
#         for i in range(0,len_spiska //2+1):
#             if i !=(len_spiska -i -1):
#                 v[i]= arr[i] * arr[len_spiska -i -1]
#             elif i==(len_spiska -i -1):
#                 v[i]=arr[i]
#     else:
#         v = [1]*(len_spiska //2)
#         for i in range(0,len_spiska //2):
#             if i !=(len_spiska -i -1):
#                 v[i]= arr[i] * arr[len_spiska -i -1]
#             elif i==(len_spiska -i -1):
#                 v[i]=arr[i]
#     return v   
              
# len_spiska = int(input())
# arr = new_spisok(len_spiska)
# f =[]
# f = find_proiz(arr, len_spiska)
# print (f)


# 3. Напишите программу, которая будет преобразовывать
#  десятичное число в двоичное.Без использования 
# встроенной функции преобразования, без строк.

# def change_to_binar(number):
#     m = []
#     while number!=0:
#         m.append(number%2)
#         number = number//2
#     for i in range(0,len(m)//2):
#         m[i],m[len(m)-i-1]=m [len(m)-i-1], m[i]
#     return m
# number = int(input())
# n =[]
# n = change_to_binar(number)
# print(n)
print(5)

