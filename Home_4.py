# 1. Вычислить число c заданной точностью d


from decimal import Decimal, ROUND_HALF_UP
a = float(input()) 
b = float(input()) 
number = Decimal(a)  
  
print(number.quantize(Decimal(str(b)), ROUND_HALF_UP)) 

# 2. Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.

# def Fun(n):
#     spisok = []
#     p = 2
#     while p * p <= n:
#         if n % p == 0:
#             spisok.append(p)
#             n //= p
#         else:
#             p += 1
#     if n > 1:
#         spisok.append(n)
#     return spisok 
# print (Fun(int(input())))  



# 3.3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности в том же порядке.

# from random import random
# pos = []
# a = int(input())
# if a > 0:
#     for i in range(a):
#         pos.append(int(random() * a))
#     print(pos)   
# else:
#     print('Negative value of the number of numbers!')
# m = []
# for k in pos:
#     if pos.count(k) == 1:
#         m.append(k)
# print(m)        


