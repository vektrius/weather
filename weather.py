import re

import bs4
import requests

re_day = r'\+\d+'
response = requests.get('https://yandex.by/pogoda/155?utm_source=serp&utm_campaign=wizard&utm_medium=desktop&utm_content=wizard_desktop_main&utm_term=title')
if len(response.text) > 150000:
    with open('Html.txt', 'w', encoding='utf8') as f:
        f.write(response.text)
    print('Обновление!')

with open('Html.txt', 'r', encoding='utf8') as f:
    text = f.read()


class Weather:
    def __init__(self):
        self.soup = bs4.BeautifulSoup(text, 'html.parser').find_all(attrs={'class': 'swiper-wrapper'})[1]

        self.day = self.soup.find_all(attrs={'class': 'forecast-briefly__name'})
        self.date = self.soup.find_all('time')
        self.temperature_morning = self.soup.find_all(attrs={'class': 'temp forecast-briefly__temp forecast-briefly__temp_day'})
        self.temperature_night = self.soup.find_all(attrs={'class': 'temp forecast-briefly__temp forecast-briefly__temp_night'})
        self.weather_state = self.soup.find_all(attrs={'class': 'forecast-briefly__condition'})

        self.weather_dict = []  # сюда добавляются ТОЛЬКО словари



    def take_weather_n_day(self,start_day,end_day):
        self.weather_dict.clear()
        if start_day < 0 or end_day > 31:
            raise IndexError('The beginning of the period can not be less than 0, and more than 31')

        for i in range(start_day, end_day):
            temperature_day_celsies = re.search(re_day, self.temperature_morning[i].text)
            temperature_night_celsies = re.search(re_day, self.temperature_night[i].text)

            day_dict = {'День недели:': self.day[i].text,
                        'Дата:': self.date[i].text,
                        'Температура в течении дня:': temperature_day_celsies.group(),
                        'Температура ночью:': temperature_night_celsies.group(),
                        'Состояние:': self.weather_state[i].text, }

            self.weather_dict.append(day_dict)

        count = start_day
        for day in self.weather_dict:
            print(f'------№{count}-------')
            count += 1
            for key, value in day.items():
                print(key, value)
            print('\n\n')

