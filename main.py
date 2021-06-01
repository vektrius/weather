# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погода
# Из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import time

import cv2
import DataBaseUpdater
from weather import Weather
from ImageMaker import Images


def ShowImage(img):
    cv2.imshow('Day info', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    current_time = time.time()
    weather = Weather()
    all_day = DataBaseUpdater.DayBase.select()
    for day_num in range(len(weather.weather_dict)):
        day_info = weather.weather_dict[day_num]
        if DataBaseUpdater.data_validation(day_info=day_info,field=all_day[day_num]):
            DataBaseUpdater.Save_field(day_info= day_info, field=all_day[day_num])

    while True:
        print(f'1.Вывести погоду за период времени дней, со вчерашнего дня. \n'
              f'2.Создать карточку дня \n')

        num_act = int(input('Что делаем?:'))
        if num_act == 1:
            n_start = int(input('С какого дня?:'))
            n_end = int(input('До какого дня?:'))
            weather.take_weather_n_day(start_day= n_start, end_day=n_end)
        elif num_act == 2:
            day_card_create = int(input('Для какого по номеру дня сделать открытку?'))
            day_card_name_file = input('Название файла для сохранения?:')
            img_create = Images()
            try:
                img = img_create.create_image_weather(weather.weather_dict[day_card_create-1])
            except IndexError:
                print('Вы ввели не верный номер дня, или не создали список погоды.')
                continue
            cv2.imwrite(f'img/day_card/{day_card_name_file}.png', img)
        else:
            print('Выберите верный пункт!!!')





    print(f'Время выполнения - {time.time() - current_time}')

