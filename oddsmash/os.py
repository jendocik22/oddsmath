import requests
import json
import pendulum
import os
import sqlite3
import openpyxl
from bs4 import BeautifulSoup

url = "https://www.oddsmath.com/api/v1/betting-tips.json/?sport_type=soccer&limit=100&include_statistics=1&timezone=UTC&country_code=RU&language=en"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01"

    "user-agent" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text
print(src)
print(type(src))
data = json.loads(src)
print(data)
print(type(data))
f = open("os.txt")
s = f.readlines()
a = s[0]
data = json.loads(a)
siroe = data['data']
b = siroe.items()
#print(type(b))
# print(len(b)) # для поиска последней страницы
e = siroe.values()

today = pendulum.today('Europe/Moscow').format('YYYY-MM-DD')
tomorrow = pendulum.tomorrow('Europe/Moscow').format('YYYY-MM-DD')

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()
with open("p1.txt", "w") as file:
    file.write('\n')
with open("p2.txt", "w") as file:
    file.write('\n')
for i in e:
    day = i['time'].split()
    if day[0] == today or day[0] == tomorrow:

        if i['selection_column'] == '1':

            oddsmash_dct = i['hometeam']
            cursor.execute('''SELECT * FROM tab_1 WHERE oddsmath = ? ''', (oddsmash_dct,))
            conn.commit()
            betfair_dct = cursor.fetchone()
            if betfair_dct != None:
                betfair_team = betfair_dct[1]

                with open("p1.txt", "a") as file:
                    file.write((f"{betfair_team}\t{(format(i['selection_stake'], '.2f'))}\t{day[0]}\n"))

        elif i['selection_column'] == '2':

            oddsmash_dct = i['awayteam']
            cursor.execute('''SELECT * FROM tab_1 WHERE oddsmath = ? ''', (oddsmash_dct,))
            conn.commit()
            betfair_dct = cursor.fetchone()
            if betfair_dct != None:
                betfair_team = betfair_dct[1]

                with open("p2.txt", "a") as file:
                    file.write((f"{betfair_team}\t{(format(i['selection_stake'], '.2f'))}\t{day[0]}\n"))
