#txt = input("Введите текст через пробел:\n")
#print(f"Исходный текст: {txt}")
#find_txt = "абв"
#lst = [i for i in txt.split() if find_txt not in i]
#print(f'Результат: {" ".join(lst)}')

#Задача №1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

# import random
# def WordRange (num):
#     for x in range(num):
#         random_txt = random.sample(text, 3)
#         list_word.append("".join(random_txt))
#     return(" ".join(list_word))

# def RangeWithoutWord (list_word):
#     list_word2 = list(filter(lambda x: text not in x, list_word.split()))
#     return(" ".join(list_word2))

# text = "абв"
# print("Word to remove: ", text)
# num = (int(input("Count of word: ")))
# list_word = []
# list_word = WordRange(num)
# print (list_word)
# new_list = RangeWithoutWord (list_word)
# print (new_list)

#Задача №2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def rle_encode(data_input):
#     encoding = ''
#     count = 1
#     if not data_input:
#         return ''
#     for ind in range(1, len(data_input)):
#         if data_input[ind] == data_input[ind - 1]:
#             count += 1
#         else :
#             if count == 1:
#                 encoding += data_input[ind - 1]
#             else:
#                 encoding += str(count) + data_input[ind - 1]
#                 count = 1
#     else:
#         if count == 1:
#             encoding += data_input[ind]
#         else:
#             encoding += str(count) + data_input[ind]
#     return encoding

# def rle_decode(data_output):
#     decoding = ''
#     count = ''
#     for char in data_output:
#         if char.isdigit():
#             count += char
#         else :
#             if not count:
#                 decoding += char
#             else: 
#                 decoding += int(count) * char
#                 count = ''
#     return decoding

#     return decoded_string


# with open('file_encode.txt', 'r') as data:
#     decoded_string = data.readline()

# with open('file_decode.txt', 'w') as data:
#     encoded_string = rle_encode(decoded_string)
#     data.write('qwf6g5j5d1k4A8s')

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))



