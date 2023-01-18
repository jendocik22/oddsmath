import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pendulum
import time

ua = UserAgent()

url = f'https://www.timeform.com/greyhound-racing/racecards'
responce = requests.get(
    url=url,
    headers={'user-agent': f'{ua.random}'}
)

src = responce.text
# print(src)

with open("pars_website.html", 'w') as file:
    file.write(src)
print("TimeForm.com Version 1.01")
with open("pars_website.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_zabeg = soup.find(class_="wfr-bytrack-content wfr-content").find_all("a")
# print(all_zabeg)

all_link = []  # Список ссылок ипподромов

today = pendulum.today('Europe/Moscow').format('DD-MM-YYYY')

with open(f"{today}.txt", 'w') as file:
    file.write('DAY' + '\t' + 'MONTH' + '\t' + 'YEAR' + '\t' + 'WEEK' + '\t' + 'TRACK' + '\t' + 'TIME' + '\t' + 'GRADE' + '\t' + 'DISTANCE' + '\t' + 'TRAP' + '\t' + 'NAME' + '\t' + 'AGE' + '\t' + 'SEX' + '\t' + 'COMMENT' + '\t' + 'DATE' + '\t' + 'DIST' + '\t' + 'GRD' + '\t' + 'TRP' + '\t' + 'TFSEC' + '\t' + 'BEND_1' +'\t' + 'BEND_2' +'\t' + 'BEND_3' +'\t' + 'BEND_4' + '\t' + 'FIN' + '\t' + 'TFGOING' + '\t' + 'BSP' + '\t' + 'ISP' + '\t' + 'TFTIME' + '\t' + 'BTN' + '\n')

word = 'racecards'

for i in all_zabeg:
    link_url = i.get('href')
    if link_url.find("racecards") != -1:
        y = 'https://www.timeform.com' + link_url
        #print(y)
        time.sleep(4)
        # all_link.append(y)
        # print(all_link)

        # ----------------------------------------------------
        # БЛОК ЗАБЕГА
        # ----------------------------------------------------
        ua1 = UserAgent()

        # y = f'https://www.timeform.com/greyhound-racing/racecards/central-park/2118/2022-10-28/1033638'
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
        print(name_ippodrom)
        date = race_zabeg[-6].lstrip('date">')
        print(date)
        number_race = race_zabeg[-5].lstrip('(').rstrip(')')
        # print(number_race)
        name_day = race_zabeg[-4]
        # print(name_day)
        number_day = race_zabeg[-3]
        # print(number_day)
        month = race_zabeg[-2]
        # print(month)
        year = race_zabeg[-1].rstrip('</b>]')
        # print(year)

        race_zabeg2 = soup1.find(class_="rph-race-details w-content rp-content rp-setting-race-details").find_all("b")
        race_zabeg2 = str(race_zabeg2)
        race_zabeg2 = race_zabeg2.split('>')
        # print(race_zabeg2)
        if race_zabeg2[2] == ", <b":
            distance = race_zabeg2[7].rstrip('m)</b')
            # print(distance)  # Дистанция забега
            grade = (race_zabeg2[5].rstrip('</b')).lstrip('(').rstrip(')')
            # print(grade)  # Класс забега
        else:
            distance = race_zabeg2[5].rstrip('m)</b')
            # print(distance)  # Дистанция забега
            grade = (race_zabeg2[3].rstrip('</b')).lstrip('(').rstrip(')')
            # print(grade)  # Класс забега

        for item in range(1, 7):
            race_zabeg2 = soup1.find(class_=f"rpb-greyhound rpb-greyhound-{item} hover-opacity")
            # print(race_zabeg2)
            if race_zabeg2 == None:
                continue
            link_dog = 'https://www.timeform.com' + race_zabeg2.get('href')  # ссылка на собаку

            nm = str(race_zabeg2)
            mn1 = nm.split('>')
            # print(mn1)
            name_dog = (mn1[-2].lstrip("\n\n                            ").rstrip("\n\n                        </a'"))
            # print(name_dog)
            # print(link_dog)
            mn1 = nm.split('(')
            number_trap = (mn1[1])[0]
            # print(number_trap) # НОМЕР ТРАПА

            # today = pendulum.today('Europe/Moscow').format('DD-MM-YYYY')
            with open(f"{today}.txt", 'a') as file:
                file.write(f'{number_day}' + '\t' + f'{month}' + '\t' + f'{year}' + '\t' + f'{name_day}' + '\t' + f'{name_ippodrom}' + '\t' + f'{date}' + '\t' + f'{grade}' + '\t' + f'{distance}' + '\t' + f'{number_trap}' + '\t' + f'{name_dog}' + '\t')  # '\t' + 'AGE' + '\t' + 'SEX' + '\t' + 'DATE' + '\t' + 'DIST' + '\t' + 'GRD' + '\t' + 'TRP' + '\t' + 'TFSEC' + '\t' + 'BEND' + '\t' + 'FIN' + '\t' + 'BTN' + '\t' + 'TFGOING' + '\t' + 'BSP' + '\t' + 'ISP' + '\t' + 'TFTIME' +

            time.sleep(2)

            # ----------------------------------------------------
            # БЛОК СОБАКИ
            # ----------------------------------------------------
            # link_dog

            ua2 = UserAgent()

            #uy = f'https://www.timeform.com/greyhound-racing/greyhound-form/roca-roma/70874'
            responce = requests.get(
                url=link_dog,
                headers={'user-agent': f'{ua2.random}'}
            )

            dog = responce.text
            #print(dog)

            with open("pars_dog.html", 'w') as file:
                file.write(dog)

            with open("pars_dog.html") as file:
                dog = file.read()

            soup2 = BeautifulSoup(dog, "lxml")

            dog_info = soup2.find(class_="w-dog-ledger w-container")

            runs1 = soup2.find(class_="w-dog-ledger w-container").find_all('b')[0]
            wins1 = soup2.find(class_="w-dog-ledger w-container").find_all('b')[1]
            runs1 = str(runs1)
            wins1 = str(wins1)
            runs = runs1.lstrip('<b>').rstrip('</b>')
            # print(runs)# RUNS
            wins = wins1.lstrip('<b>').rstrip('</b>')
            # print(wins)# WINS
            sex_age1 = soup2.find(class_="w-dog-ledger w-container").find_all('span')[3]
            sex_age = str(sex_age1)
            sex_age = sex_age.lstrip('<span><b>Age, Sex, Colou').rstrip('</span>')
            sex_age = sex_age.lstrip("r</b")
            sex_age = sex_age.lstrip(">")
            sex_age = sex_age.split()
            sex = sex_age[1]
            # print(sex) # пол собаки
            age = sex_age[2]
            # print(age) # дата рождения

            today = pendulum.today('Europe/Moscow').format('DD-MM-YYYY')
            with open(f"{today}.txt", 'a') as file:
                file.write(f'{age}' + '\t' + f'{sex}' + '\t')

            # Забеги истории
            dog_historia = soup2.find(class_="w-dog-ledger-table w-dog-ledger-performances recent-form").find_all('tr')
            # print(dog_historia)

            for ty in dog_historia:
                ees = ty.find(class_="recent-form-meeting-date")
                ees = str(ees)
                ees = ees.split('\n')
                if ees == ['None']:
                    continue
                comment = ees[0].lstrip('<td class="recent-form-meeting-date" title="').rstrip('">')
                # print(comment) # КОММЕНТАРИЙ СОБАКИ

                ty = str(ty)
                ty = ty.split('\n')
                # print(ty)
                if len(ty) > 5:
                    if ty[0] == '<tr class="ledger-performance-time-off">' or ty[0] == '<tr class="ledger-performance-stable-change">':
                        continue
                    if ty[0] == '<tr>' or ty[0] == '<tr class="ledger-performance-win">':
                        ty.pop(0)
                    if ty[0] == '<th class="recent-form-header-meeting-date" title="The date the meeting is taking place">':
                        del ty[:]
                    if ty[11] == '<span>(E)</span>':
                        ty.pop(11)
                    if len(ty) > 0:
                        # print(ty)
                        data_zabeg_history = (ty[1].split('>'))[-2].rstrip('</a')
                        # print(data_zabeg_history) # ДАТА ИСТОРИЧЕСКОГО ЗАБЕГА
                        distance_zabeg_history = (ty[8].split('>'))[-2].rstrip('m</td')
                        # print(distance_zabeg_history) # ДИСТАНЦИЯ ИСТОРИЧЕСКОГО ЗАБЕГА
                        class_zabeg_history = (ty[9].split('>'))[-2].rstrip('</td')
                        # print(class_zabeg_history) # КЛАСС ИСТОРИЧЕСКОГО ЗАБЕГА
                        trap_zabeg_history = (ty[13].split('>'))[-2].rstrip('</td')
                        # print(trap_zabeg_history) # КЛАСС ИСТОРИЧЕСКОГО ЗАБЕГА
                        tfsec_zabeg_history = (ty[14].split('>'))[-2].rstrip('</td')
                        # print(tfsec_zabeg_history) # TFSec ИСТОРИЧЕСКОГО ЗАБЕГА
                        bend_zabeg_history = (ty[15].split('>'))[-2].rstrip('</td')
                        # print(bend_zabeg_history) # Bend ИСТОРИЧЕСКОГО ЗАБЕГА
                        if len(bend_zabeg_history) > 0:
                            bend_zabeg_history1 = bend_zabeg_history[0]
                            bend_zabeg_history2 = bend_zabeg_history[1]
                            bend_zabeg_history3 = bend_zabeg_history[2]
                            bend_zabeg_history4 = bend_zabeg_history[3]  # Bend ИСТОРИЧЕСКОГО ЗАБЕГА
                        finish_zabeg_history1 = (ty[16].split('>'))[-3].rstrip('</b')
                        if len(finish_zabeg_history1) == 1:
                            finish_zabeg_history = finish_zabeg_history1
                        else:
                            finish_zabeg_history = finish_zabeg_history1[0]
                        # print(finish_zabeg_history) # ФИНИШ ИСТОРИЧЕСКОГО ЗАБЕГА
                        tfgoing_zabeg_history = ((ty[18].split('>'))[-2].rstrip('/td')).rstrip('<')
                        # print(tfgoing_zabeg_history) # TFGoing ИСТОРИЧЕСКОГО ЗАБЕГА
                        bsp_zabeg_history = ((ty[19].split('>'))[-2].rstrip('/td')).rstrip('<')
                        # print(bsp_zabeg_history)  # BSP ИСТОРИЧЕСКОГО ЗАБЕГА
                        isp_zabeg_history1 = ((ty[20].split('>'))[-2].rstrip('/td')).rstrip('<')
                        # print(isp_zabeg_history1)  # ISP ИСТОРИЧЕСКОГО ЗАБЕГА
                        if len(isp_zabeg_history1) > 0:
                            isp_zabeg_history = int((isp_zabeg_history1.split('/'))[0]) / int((isp_zabeg_history1.split('/'))[1]) + 1
                        tftime_zabeg_history = ((ty[21].split('>'))[-2].rstrip('/td')).rstrip('<')
                        # print(tftime_zabeg_history)  # TFTime ИСТОРИЧЕСКОГО ЗАБЕГА

                        # detsl = 0
                        # while detsl < 10: grade distance
                        if distance_zabeg_history == distance:
                            if class_zabeg_history == grade or class_zabeg_history == 'T3':
                                # print(f'{data_zabeg_history}')
                                with open(f"{today}.txt", 'a') as file:
                                    file.write(f'{comment}' + '\t' + f'{data_zabeg_history}' + '\t' + f'{distance_zabeg_history}' + '\t' + f'{class_zabeg_history}' + '\t' + f'{trap_zabeg_history}' + '\t' + f'{tfsec_zabeg_history}' + '\t' + f'{bend_zabeg_history1}' +'\t' + f'{bend_zabeg_history2}' +'\t' + f'{bend_zabeg_history3}' +'\t' + f'{bend_zabeg_history4}' + '\t' + f'{finish_zabeg_history}' + '\t' + f'{tfgoing_zabeg_history}' + '\t' + f'{bsp_zabeg_history}' + '\t' + f'{isp_zabeg_history}' + '\t' + f'{tftime_zabeg_history}' + '\t')

                                btn = ((ty[17].split('>'))[-2].rstrip('/td')).rstrip('<')
                                # print(btn)
                                if len(btn) == 1 and btn in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                                    with open(f"{today}.txt", 'a') as file:
                                        file.write(f'{btn}' + '\t')

                                if len(btn) == 2 and btn in ('10', '11', '12', '13', '14', '15', '16', '17', '18', '19'):
                                    with open(f"{today}.txt", 'a') as file:
                                        file.write(f'{btn}' + '\t')

                                if btn == 'nk':
                                    btn_zabeg_history = '-0,5'
                                    with open(f"{today}.txt", 'a') as file:
                                        file.write(f'{btn_zabeg_history}' + '\t')

                                if btn == '-':
                                    btn_zabeg_history = '0'
                                    with open(f"{today}.txt", 'a') as file:
                                        file.write(f'{btn_zabeg_history}' + '\t')

                                if btn == 'sh':
                                    btn_zabeg_history = '0,15'
                                    with open(f"{today}.txt", 'a') as file:
                                        file.write(f'{btn_zabeg_history}' + '\t')

                                if btn == 'dis':
                                    btn_zabeg_history = '15'
                                    with open(f"{today}.txt", 'a') as file:
                                        file.write(f'{btn_zabeg_history}' + '\t')

                                if btn == 'hd':
                                    btn_zabeg_history = '-1'
                                    with open(f"{today}.txt", 'a') as file:
                                        file.write(f'{btn_zabeg_history}' + '\t')

                                if btn == 'dh':
                                    btn_zabeg_history = '-1'
                                    with open(f"{today}.txt", 'a') as file:
                                        file.write(f'{btn_zabeg_history}' + '\t')

                                    # Bend ИСТОРИЧЕСКОГО ЗАБЕГА
                                # print(btn)
                                btn1 = []
                                if len(btn) > 4:
                                    for word in btn:
                                        if word in ("&", 'a', 'm', 'p', ';', 'f', 'r', 'a', 'c'):
                                            continue
                                        else:
                                            btn1.append(word)
                                    # print(btn1)

                                    if len(btn1) == 3 and btn1[-1] == '2':
                                        btn_zabeg_history = (int(btn1[0]) + int(btn1[1]) / int(btn1[2]))
                                        with open(f"{today}.txt", 'a') as file:
                                            file.write(f'{btn_zabeg_history}' + '\t')

                                    elif len(btn1) == 3 and btn1[-1] == '4':
                                        btn_zabeg_history = (int(btn1[0]) + int(btn1[1]) / int(btn1[2]))
                                        with open(f"{today}.txt", 'a') as file:
                                            file.write(f'{btn_zabeg_history}' + '\t')

                                    elif len(btn1) == 2 and btn1[-1] == '2':
                                        btn_zabeg_history = (int(btn1[0]) / int(btn1[1]))
                                        with open(f"{today}.txt", 'a') as file:
                                            file.write(f'{btn_zabeg_history}' + '\t')

                                    elif len(btn1) == 2 and btn1[-1] == '4':
                                        btn_zabeg_history = (int(btn1[0]) / int(btn1[1]))
                                        with open(f"{today}.txt", 'a') as file:
                                            file.write(f'{btn_zabeg_history}' + '\t')

                                    elif len(btn1) == 4 and btn1[-1] == '2':
                                        btn_zabeg_history = (int(btn1[0]) * 10 + int(btn1[1]) + int(btn1[2]) / int(btn1[3]))
                                        with open(f"{today}.txt", 'a') as file:
                                            file.write(f'{btn_zabeg_history}' + '\t')

                                    elif len(btn1) == 4 and btn1[-1] == '4':
                                        btn_zabeg_history = (int(btn1[0]) * 10 + int(btn1[1]) + int(btn1[2]) / int(btn1[3]))
                                        with open(f"{today}.txt", 'a') as file:
                                            file.write(f'{btn_zabeg_history}' + '\t')

                                        # Btn ИСТОРИЧЕСКОГО ЗАБЕГА

            time.sleep(2)

            with open(f"{today}.txt", 'a') as file:
                file.write('\n')