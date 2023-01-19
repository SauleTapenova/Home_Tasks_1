# 1. Представлен список чисел. Необходимо вывести элементы 
# исходного списка, значения которых больше предыдущего
#  элемента. Use comprehension.
# result_list = []
# list = [int(i) for i in input().split()]
# print(list)
# result_list = [list[i] for i in range(1, len(list)) if list[i]> list[i-1]]
# print(result_list)

# 2. Для чисел в пределах от 20 до N найти числа,
# кратные 20 или 21. Use comprehension.
# a = int(input())
# list = [i for i in range(20, a+1) if i % 20 == 0 or i % 21 == 0]
# print( list)

# 3. Написать функцию, аргументы имена сотрудников,
#  возвращает словарь, ключи — первые буквы имён, 
#  значения — списки, содержащие имена, начинающиеся с
#  соответствующей буквы.

def thesaurus(*names_empl):
    res = {}
    for name in sorted(names_empl):
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))



