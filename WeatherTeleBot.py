import time
import pyowm
import requests
from datetime import datetime
# import logging

# logging.basicConfig(filename='WeatherTeleBot.log', filemode='w', format='%(time)s — %(name)s — %(level)s — %('message)s')

owm = pyowm.OWM('caf14d0af187617f830a3e39dffa2de9', language="ru")


def send_telegram(text: str):
    try:
        # https://api.telegram.org/bot848471226:AAHCCy9pW0j4qakzrSck2GGNNzH3DAIIX2g/sendMessage?chat_id=253689257&text=TEXT
        token = "848471226:AAHCCy9pW0j4qakzrSck2GGNNzH3DAIIX2g"
        url = "https://api.telegram.org/bot"
        url += token
        method = url + "/sendMessage"
        r = requests.post(method, data={"chat_id": 253689257, "text": text})
        if r.status_code != 200:
            raise Exception("post_text error")
    except Exception as e:
        # logging.exception("Exception occurred")
        pass


tCurrent = time.time()
while True:
    if time.time() >= tCurrent + 1:
        try:
            print(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
            tCurrent = time.time()
            # вытаскиваем данные с owm
            observation = owm.weather_at_place('Taganrog,RU')
            w = observation.get_weather()
            temp = w.get_temperature('celsius')["temp"]
            wind = w.get_wind()["speed"]
            humidity = w.get_humidity()
            answer = "В Таганроге сейчас " + w.get_detailed_status() + ", температра " + str(
                temp) + "°, скорость ветра " + str(wind) + "м/с, влажность " + str(humidity) + "%"
            # вызываем функцию для отрпавки ответа в телеграм
            send_telegram(answer)
        except Exception as e:
            pass
        time.sleep(3600)  # sleep 1час
