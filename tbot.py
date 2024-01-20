import requests
import json
import telebot
from telebot import types
url = "https://api.weather.yandex.ru/v2/informers?lat=55.75222&lon=37.61556"
headers = {"X-Yandex-API-Key": "weather token"}
bot = telebot.TeleBot('6169575331:AAEBdTW60CMa24zsWcxA_42SAzi6QCC1M3M');
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"https://habr.com/ru/users/lubaznatel/")
@bot.message_handler(commands=['weather'])
def get_weather(message):
    r = requests.get(url=url, headers=headers)
    bot.send_message(message.chat.id, r.text)
bot.infinity_polling()