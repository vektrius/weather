import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont

class Images:
    def __init__(self):
        self.probe = cv2.imread('img/probe.jpg')

        self.height_probe = np.size(self.probe,0)
        self.width_probe = np.size(self.probe,1)

        self.day_state_dict = {
            'Ясно' : cv2.imread('img/sun.jpg'),
            'Пасмурно' : cv2.imread('img/cloudy.jpg'),
            'Облачно с прояснениями' : cv2.imread('img/cloudy.jpg'),
            'Дождь' : cv2.imread('img/rain.jpg'),
            'Малооблачно' : cv2.imread('img/cloudy.jpg')
        }

    def create_image_weather(self,day_info):

        '''
        Создание карточки дня.
        :param day_info:
        :return cv2.image:
        '''
        state = day_info['Состояние:']
        day = day_info['День недели:']
        date = day_info['Дата:']
        temp_day = day_info['Температура в течении дня:']
        temp_night = day_info['Температура ночью:']

        with Image.open('img/probe.jpg').convert("RGBA") as base:
           txt = Image.new("RGBA", base.size, (255,2555,255,0))

           fnt1 = ImageFont.truetype("test.ttf", 20)
           fnt2 = ImageFont.truetype("test.ttf", 40)

           d = ImageDraw.Draw(txt)
           d.text((10, 120), day, font = fnt2, fill = (255,255,255,128))
           d.text((10, 170), f'Температура днём:{temp_day}', font=fnt1, fill=(255, 255, 255, 128))
           d.text((10, 220), f'Температура ночью:{temp_night}', font=fnt1, fill=(255, 255, 255, 128))
           d.text((10, 270), f'Состояние:{state}', font=fnt1, fill=(255, 255, 255, 128))

           out = Image.alpha_composite(base, txt)
           out.save('img/frame.png')

        frame = cv2.imread('img/frame.png')
        day_state_img = self.day_state_dict[state]

        height_day_img = np.size(day_state_img, 0)
        width_day_img = np.size(day_state_img, 1)

        for i in range(height_day_img):
            for j in range(width_day_img):
                check = any(day_state_img[i,j] <= 247)
                if check:
                    frame[i,j] = day_state_img[i,j]





        return frame

