r = open('rocket.txt', encoding="UTF-8")

arr_r = [] # Массив с элементами ракет. Вид: [ [date,code,rocketparts], ... ]

# Парсинг файла с ракетами
for i in r:
    i = i[:-1]
    i = i.split('@')
    arr_r.append(i)

# Сортировка вставкой массива с элементами ракет с ключем code
for i in range(len(arr_r)):
    j = i
    while j > 0 and arr_r[j-1][1] > arr_r[j][1]:
        tmp = arr_r[j-1]
        arr_r[j-1] = arr_r[j]
        arr_r[j] = tmp
        j -= 1

# Поиск ошибок содержащих код 312 и их вывод
for i in arr_r:
    if '312' in i[1]:
        print(f"{i[1]} для {i[2]}")

