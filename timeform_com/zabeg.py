import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pendulum

ua1 = UserAgent()

y = f'https://www.timeform.com/greyhound-racing/racecards/newcastle/1526/2022-10-29/1034141'
responce = requests.get(
    url=y,
    headers={'user-agent': f'{ua1.random}'}
)

race = responce.text
# print(race)

with open("pars_zabeg.html", 'w') as file:
    file.write(race)

with open("pars_zabeg.html") as file:
    race = file.read()

soup1 = BeautifulSoup(race, "lxml")

race_zabeg1 = soup1.find(class_="w-header")
race_zabeg1 = str(race_zabeg1)
race_zabeg1 = race_zabeg1.split()

race_zabeg = soup1.find(class_="rph-race-details-col rph-race-details-col-1").find_all("b")
race_zabeg = str(race_zabeg)
race_zabeg = race_zabeg.split()

name_ippodrom = race_zabeg1[-3]
# print(name_ippodrom)
date = race_zabeg[-6].lstrip('date">')
#print(date)
number_race = race_zabeg[-5].lstrip('(').rstrip(')')
# print(number_race)
name_day = race_zabeg[-4]
#print(name_day)
number_day = race_zabeg[-3]
# print(number_day)
month = race_zabeg[-2]
# print(month)
year = race_zabeg[-1].rstrip('</b>]')
# print(year)

race_zabeg2 = soup1.find(class_="rph-race-details w-content rp-content rp-setting-race-details").find_all("b")
race_zabeg2 = str(race_zabeg2)
race_zabeg2 = race_zabeg2.split('>')
#print(race_zabeg2)
if race_zabeg2[2] == ", <b":
    distance = race_zabeg2[7].rstrip('m)</b')
    #print(distance) # Дистанция забега
    grade = (race_zabeg2[5].rstrip('</b')).lstrip('(').rstrip(')')
    #print(grade) # Класс забега
else:
    distance = race_zabeg2[5].rstrip('m)</b')
    #print(distance) # Дистанция забега
    grade = (race_zabeg2[3].rstrip('</b')).lstrip('(').rstrip(')')
    #print(grade) # Класс забега


for item in range(1, 7):
    race_zabeg2 = soup1.find(class_=f"rpb-greyhound rpb-greyhound-{item} hover-opacity")
    #print(race_zabeg2)
    if race_zabeg2 == None:
        continue
    link_dog = 'https://www.timeform.com' + race_zabeg2.get('href') #ссылка на собаку

    nm = str(race_zabeg2)
    mn1 = nm.split('>')
    #print(mn1)
    name_dog = (mn1[-2].lstrip("\n\n                            ").rstrip("\n\n                        </a'"))
    # print(name_dog)
    # print(link_dog)
    mn1 = nm.split('(')
    number_trap = (mn1[1])[0]
    #print(number_trap) # НОМЕР ТРАПА

    today = pendulum.today('Europe/Moscow').format('DD-MM-YYYY')
    with open(f"{today}.txt", 'a') as file:
        file.write(f'{number_day}' + '\t' + f'{month}' + '\t' + f'{year}' + '\t' + f'{name_day}' + '\t' + f'{name_ippodrom}' + '\t' + f'{date}' + '\t' + f'{grade}' + '\t' + f'{distance}' + '\t' + f'{number_trap}' + '\t' + f'{name_dog}' +'\n')            #  '\t' + 'AGE' + '\t' + 'SEX' + '\t' + 'DATE' + '\t' + 'DIST' + '\t' + 'GRD' + '\t' + 'TRP' + '\t' + 'TFSEC' + '\t' + 'BEND' + '\t' + 'FIN' + '\t' + 'BTN' + '\t' + 'TFGOING' + '\t' + 'BSP' + '\t' + 'ISP' + '\t' + 'TFTIME' +
