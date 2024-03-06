r = open('rocket.txt', encoding="UTF-8")

arr_r = [] # Массив с элементами ракет. Вид: [ [date,code,rocketparts], ... ]

# Парсинг файла с элементами ракет
for i in r:
    i = i[:-1]
    i = i.split('@')
    arr_r.append(i)

request = input()
while request != 'nlo':
    found = False
    for i in arr_r:
        if request == i[1]:
            found = True
            print(f"Шифр: {i[1]} от: {i[2]} был получен {i[0]}")
    if found == False:
        print("Такой сигнал еще не был получен")
    request = input()
