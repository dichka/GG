import sqlite3

id_vk = list()
name = list()
ispoln = list()

cover_youtube = ['Введи оригинального автора: ', 'Введи название композиции: ', 'Введи исполнителей через запятую: ']

number = input('Введи номер ГП: ')

con = sqlite3.connect("GG.sqlite")
cur = con.cursor()

sql = (f"""
SELECT smile, date  
FROM VK_patern
WHERE VK_patern.number = {number}
""")

cur.execute(sql)
result = cur.fetchone()
cur.close()


for i in range(len(cover_youtube)):
    name.append(input(cover_youtube[i]))
names = name[2].split(', ' or ',' or ' & ' or ' и ')

print('-------------------------')
print('Наименование песни в YouTube\n')
print(f'{name[0]} - {name[1]} (Cover by {name[2]})')
print('\n-------------------------')

con = sqlite3.connect("GG.sqlite")
cur = con.cursor()

for n in range(len(names)):
    sql = (f"""
    SELECT id_vk  
    FROM artists
    WHERE artists.name LIKE "%{names[n]}%"
    """)

    cur.execute(sql)
    result2 = cur.fetchone()
    id_vk.append(result2)
    names[n].split(',')
cur.close()

for i in range(len(names)):
    ispoln.append(f'@{id_vk[i][0]} ({(names[i].split())[0]})')

ispoln = ', '.join(ispoln)

print('Обложка для ВК\n')
print(f'{name[0]} - {name[1]}\nИсполняют: {ispoln}\n')
print(f'Гитарные посиделки {number} {result[0]}\n{result[1]}')
print('\n-------------------------\n')
