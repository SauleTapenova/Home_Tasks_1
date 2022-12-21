# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# n = float(input())
# sum = 0
# m = len(str(n))
# n = n * 10 ** (m - 1)
# while n != 0:
#     c = n % 10
#     n = n // 10
#     sum = sum + c
# print (sum)  


# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# m = []
# n = int(input())
# f1 = 1
# f2 = 1
# for i in range(1, n+1):    
#     f2 =  i *(f1 * f2) 
#     m.append(f2)   
# print (m)
    
#3. Задайте список из n чисел, заполненный по формуле 
#(1 + 1/n) ** n и выведите на экран их сумму.
# m= []
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     a = (1 + 1/i) ** i
#     m.append(round (a,3))
#     sum = sum + a
# print (m)
# print (round (sum,3))

#4. Напишите программу, которая принимает на вход 2 числа.
#Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).

# m= []
# n = int(input())
# a1= int (input ())
# a2= int (input())
# count = 1
# for i in range(-n, n+1):
#     m.append(i)
# print (m)
# if 0<a1<=n and 0<a2<=n:
#     count = m[a1-1]*m[a2-1]
#     print(count)
# else:
#     print('There are no values for these indexes!')

# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

import random
a = int (input())
n = list(range(a))
print(n)

for i in range(0, a-1):
    c = random.randint (0, i+1)
    n[i], n[c]=n[c], n[i]
print(n)
    
# a = int (input())


# from random import randint, randrange 
# print(randrange (4))

# print(n)

# a1= int (input ())
# a2= int (input())


