f = open('rocket_part.txt', encoding="UTF-8")

rockets = [ ]

#Парсинг файла с частями от ракет
for i in f:
    """Парсинг файла с частями от ракет"""
    i = i[:-1]
    i = i.split('@')
    rockets.append(i)

name = input()

#Поиск части ракеты в массиве
for i in rockets:
    if name == i[0]:
        print(i[1])