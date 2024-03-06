r = open('rocket.txt', encoding="UTF-8")

arr_r = [] # Массив с ракетами. Вид: [ [date,code,rocketparts], ... ]

cnt = 1

def genName(rocket_part):
    global cnt
    name = rocket_part[2].split(' ')
    nameCut = ''
    for i in name:
        nameCut += i[0].capitalize()
    queue = str(cnt)+rocket_part[1]+nameCut
    cnt += 1
    return [rocket_part[0], rocket_part[1], rocket_part[2], queue]

# Парсинг файла с ракетами
for i in r:
    i = i[:-1]
    i = i.split('@')
    arr_r.append(i)

# Сортировка вставкой массива с ракетами с ключем date
for i in range(len(arr_r)):
    j = i
    while j > 0 and arr_r[j-1][0] > arr_r[j][0]:
        tmp = arr_r[j-1]
        arr_r[j-1] = arr_r[j]
        arr_r[j] = tmp
        j -= 1

csv = open('out.csv', mode='w', encoding='UTF-8')
csv.write('date;code;rocketparts;queue\n')

for i in arr_r:
    queue = genName(i)
    csv.write(f'{queue[0]};{queue[1]};{queue[2]};{queue[3]}\n')



