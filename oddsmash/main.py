import requests
import pendulum
import sqlite3
from fake_useragent import UserAgent
import time
from datetime import datetime

ua = UserAgent()


def collect_data():
    page = 1
    b = {}
    with open("p1.txt", "w") as file:
        file.write('\n')
    # with open("p2.txt", "w") as file:
    #     file.write('\n')
    while True:
        for item in range(page, page + 1):
            url = f'https://www.oddsmath.com/api/v1/betting-tips.json/?sport_type=soccer&limit=100&include_recent=1&include_statistics=1&range=prematch&timezone=Europe%2FMinsk&country_code=BY&language=en&page={item}'
            responce = requests.get(
                url=url,
                headers={'user-agent': f'{ua.random}'}
            )
            page += 1

            data = responce.json()
            siroe = data['data']
            b = siroe.items()
            e = siroe.values()

            today = pendulum.today('Europe/Moscow').format('YYYY-MM-DD')
            tomorrow = pendulum.tomorrow('Europe/Moscow').format('YYYY-MM-DD')

            conn = sqlite3.connect('baza.db')
            cursor = conn.cursor()

            for i in e:
                day = i['time'].split()
                if day[0] == today or day[0] == tomorrow:

                    if i['selection_column'] == '1' and i['selection_cat_id'] == 0:

                        oddsmash_dct = i['hometeam']
                        cursor.execute('''SELECT * FROM tab_1 WHERE oddsmath = ? ''', (oddsmash_dct,))
                        conn.commit()
                        betfair_dct = cursor.fetchone()
                        if betfair_dct != None:
                            betfair_team = betfair_dct[1]

                            with open("p1.txt", "a") as file:
                                file.write((f"{betfair_team}\t{(format(i['selection_stake'], '.2f'))}\t{day[0]}\n"))

                    elif i['selection_column'] == '2' and i['selection_cat_id'] == 0:

                        oddsmash_dct = i['awayteam']
                        cursor.execute('''SELECT * FROM tab_1 WHERE oddsmath = ? ''', (oddsmash_dct,))
                        conn.commit()
                        betfair_dct = cursor.fetchone()
                        if betfair_dct != None:
                            betfair_team = betfair_dct[1]

                            with open("p1.txt", "a") as file:
                                file.write((f"{betfair_team}\t{(format(i['selection_stake'], '.2f'))}\t{day[0]}\n"))

        if len(b) < 100:
            break


def main():
    collect_data()


if __name__ == "__main__":
    while True:
        print(f'Последнее обновление: {datetime.now()}')
        main()
        time.sleep(180)
