#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'wife', 'grandma', 'uncle']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['lena', 168], ['Aleksey',188],['Diana', 165], ['Rimma',150],['Anton', 188]
]
mfh = my_family_height
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца-')
print(mfh[1][1])
print('см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
l=len(my_family_height)

h = []
for i in mfh:
    for n in i:
        if type(n)==int:
            h.append(n)
print(sum(h))

print('Общий рост моей семьи-' + str(sum(h)) + ' см')


