import json
import requests
import sqlite3

conn = sqlite3.connect('dog.sqlite')
cursor = conn.cursor()


response = requests.get("https://api.thedogapi.com/v1/breeds")
# print(response.text)
# print(response.headers)
# print(response.status_code)
res = response.json()
# print(res)

with open('dg.json', 'w') as c:
    json.dump(res, c, indent=4)


lists = []
for each in res:
    try:
        name = each['name']
        life_span = each['life_span']
        breed = each['breed_group']
        # print(bred)
        row = (name, life_span, breed)
        lists.append(row)

    except KeyError:
        pass

# print(lists)

cursor.execute('''CREATE TABLE IF NOT EXISTS dogs
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50),
                    life_span VARCHAR(50),
                    breed VARCHAR(50))''')

cursor.executemany('INSERT INTO dogs (name, life_span, breed) VALUES (?, ?, ?)', lists)

conn.commit()