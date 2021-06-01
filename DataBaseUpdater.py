from Database import *


def add_new_day(day_info):
    state = day_info['Состояние:']
    day = day_info['День недели:']
    date = day_info['Дата:']
    temp_day = day_info['Температура в течении дня:']
    temp_night = day_info['Температура ночью:']

    new_day = DayBase(day = day,date = date,temp_morning = temp_day,temp_night = temp_night,state = state,img = None)
    new_day.save()

def Save_field(field,day_info):
    state = day_info['Состояние:']
    day = day_info['День недели:']
    date = day_info['Дата:']
    temp_day = day_info['Температура в течении дня:']
    temp_night = day_info['Температура ночью:']

    field.day = day
    field.date = date
    field.temp_morning = temp_day
    field.temp_night = temp_night
    field.state = state

    field.save()

def data_validation(day_info,field):
    state = day_info['Состояние:']
    day = day_info['День недели:']
    date = day_info['Дата:']
    temp_day = day_info['Температура в течении дня:']
    temp_night = day_info['Температура ночью:']

    if state == field.state and day == field.day and date == field.date and temp_day == field.temp_morning \
       and temp_night == field.temp_night:
        return True
    else:
        return False
