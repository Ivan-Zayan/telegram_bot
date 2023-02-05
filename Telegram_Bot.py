import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
from base_telega import chat_bot22
import time

try:
    header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'}

    bot = telebot.TeleBot('')  # Введите токен вашего телеграм бота


    def weather():
        url = 'https://www.gismeteo.ru/weather-azov-5107/now/'
        Azov = requests.get(url, headers=header)
        weather_Azov = BeautifulSoup(Azov.text, 'lxml')
        today = weather_Azov.find('span', class_="unit unit_temperature_c").text
        sun = weather_Azov.find('div', class_='now-desc').text
        all_weather = f'{today} {sun}'
        return all_weather


    def weather_tomorrow():
        url = 'https://www.gismeteo.ru/weather-azov-5107/tomorrow/'
        Azov = requests.get(url, headers=header)
        weather_Azov = BeautifulSoup(Azov.text, 'lxml')
        tom_day = weather_Azov.find('a', class_='weathertab weathertab-block tooltip')
        sun_tom_day = weather_Azov.find('a', class_='weathertab weathertab-block tooltip').get('data-text')
        today = tom_day.select('span', class_="unit unit_temperature_c")[2].text
        all_tomorrow = f'{today} {sun_tom_day}'
        return all_tomorrow,


    def weather_Ros():
        url = 'https://www.gismeteo.ru/weather-rostov-na-donu-5110/now/'
        Azov = requests.get(url, headers=header)
        weather_Azov = BeautifulSoup(Azov.text, 'lxml')
        today = weather_Azov.find('span', class_="unit unit_temperature_c").text
        sun = weather_Azov.find('div', class_='now-desc').text
        all_weather = f'{today}  {sun}'
        return all_weather


    def weather_tomorrow_Ros():
        url = 'https://www.gismeteo.ru/weather-rostov-na-donu-5110/tomorrow/'
        Azov = requests.get(url, headers=header)
        weather_Azov = BeautifulSoup(Azov.text, 'lxml')
        tom_day = weather_Azov.find('a', class_='weathertab weathertab-block tooltip')
        sun_tom_day = weather_Azov.find('a', class_='weathertab weathertab-block tooltip').get('data-text')
        today = tom_day.select('span', class_="unit unit_temperature_c")[2].text
        all_tomorrow = f'{today} {sun_tom_day}'
        return all_tomorrow


    @bot.message_handler(commands=['start'])
    def start(message):
        mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        my_father = types.KeyboardButton(' покажи создателя')
        hello = types.KeyboardButton('hello')
        sadly = types.KeyboardButton('мне грустно')
        body = types.KeyboardButton('нужно закопать тело')
        lot_body = types.KeyboardButton('нужно закопать несколько тел')
        milota = types.KeyboardButton('покажи милоту')
        milka = types.KeyboardButton('покажи МилкуКопилку')
        bludnitca = types.KeyboardButton('Кто зажрался?')
        diletant = types.KeyboardButton('Поиск Дилетанта')
        memskiy = types.KeyboardButton('Кто по бабушкам?')
        weather = types.KeyboardButton('Погода в Азове сейчас')
        weather_tomor = types.KeyboardButton('Погода в Азове завтра')
        waether_Ros = types.KeyboardButton('Погода в Ростове сейчас')
        weather_tomor_Ros = types.KeyboardButton('Погода в Ростове завтра')
        markup.add(my_father, hello, sadly, body, lot_body, milota, milka, bludnitca, diletant,
                   memskiy, weather, weather_tomor, waether_Ros, weather_tomor_Ros)
        bot.send_message(message.chat.id, 'рабочие команды', reply_markup=markup)


    @bot.message_handler()
    def get_user_text(message):
        if message.text == 'hello':
            bot.send_message(message.chat.id, "хай, привет, хола, намасте, чик чирык", parse_mode='html')
        elif message.text == 'мне грустно':
            bot.send_message(message.chat.id, 'шлю обнимашки, улыбнись и покушай', parse_mode='html')
        elif message.text == 'покажи создателя':
            bot.send_message(message.chat.id, 'https://vk.com/ivanushka2377')
        elif message.text == 'Кто зажрался?':
            bot.send_message(message.chat.id, 'https://vk.com/kkidaeva')
        elif message.text == 'Погода в Азове сейчас':
            bot.send_message(message.chat.id, weather())
        elif message.text == 'Погода в Азове завтра':
            bot.send_message(message.chat.id, weather_tomorrow())
        elif message.text == 'Погода в Ростове сейчас':
            bot.send_message(message.chat.id, weather_Ros())
        elif message.text == 'Погода в Ростове завтра':
            bot.send_message(message.chat.id, weather_tomorrow_Ros())
        elif message.text == 'Поиск Дилетанта':
            bot.send_message(message.chat.id, 'https://vk.com/verylongtacsa')
        elif message.text == 'Кто по бабушкам?':
            bot.send_message(message.chat.id, 'https://vk.com/roadtoarmenia')
        elif message.text == 'покажи МилкуКопилку':
            bot.send_message(message.chat.id, 'https://vk.com/y__a__i__s__t__i__n__a')
        elif message.text == 'нужно закопать тело':
            bot.send_message(message.chat.id, 'вам следует обратиться к Ивану Заянчковскому. Сочувствую',
                             parse_mode='html')
        elif message.text == 'нужно закопать несколько тел':
            bot.send_message(message.chat.id, 'вы хотели сказать: \"клубника лучше малины? Согласен с вами\"',
                             parse_mode='html')
        elif message.text == 'покажи милоту':
            photo = open('alpak.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, chat_bot22(message.text), parse_mode='html')


    @bot.message_handler(content_types=['photo'])
    def photo_user(message):
        bot.send_message(message.chat.id, 'Я не понимаю фотографии, напиши текстом', parse_mode='html')


    bot.polling(none_stop=True)
except:
    time.sleep(10)
