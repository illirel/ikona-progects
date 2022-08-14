#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
q = my_favorite_movies
l = len(q)
n = q.find(', ')
print(q[0:(n)])

rn = q.rfind(', ')
print(q[rn+2:l])


n = q.find(', ',start = q[n], end= ', ')


# TEMP = str()
# FilmList = list()

# for i in q:
#     if i != ',':
#         TEMP += i
#         print(TEMP)
#     elif i == ',':
#         FilmList.append(TEMP)
#         TEMP = str()
#         print(TEMP)
#     else:
#         FilmList.append(TEMP)
#     print(FilmList)
# stroka = str()
# listnew = []
# for i in q:
#     if i == ",":
#         listnew.append(stroka.strip())
#         stroka = str()
#     else:
#         stroka += i
# if stroka:
#     listnew.append(stroka.strip())
#
# print(listnew)
#
# print(listnew[1])
# print(listnew[-2])







