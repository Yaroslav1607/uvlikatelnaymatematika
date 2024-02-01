import telebot
from telebot import types  # для указание типов
import random

bot = telebot.TeleBot("6378681836:AAE7m_eo3RYwVyLZ3h1Pq9xrMdgQ8XHScSA")
a = ['+', '-']
sloj = 0
r = 0
plus = ''
p = 0
n = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("лёгкий")
    btn2 = types.KeyboardButton("средний")
    btn3 = types.KeyboardButton("сложный")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет,  {0.first_name}!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    global sloj, r, plus, n, p, ch1, ch2
    if message.text == "лёгкий":
        sloj = 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("да")
        btn2 = types.KeyboardButton("нет")
        types.KeyboardButton("оценка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Хотите продолжить", reply_markup=markup)
    elif message.text == "средний":
        sloj = 2
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("да")
        btn2 = types.KeyboardButton("нет")
        btn3 = types.KeyboardButton("оценка")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Хотите продолжить", reply_markup=markup)
    elif message.text == "сложный":
        sloj = 3
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("да")
        btn2 = types.KeyboardButton("нет")
        types.KeyboardButton("оценка")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Хотите продолжить", reply_markup=markup)
    elif message.text == "нет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("лёгкий")
        btn2 = types.KeyboardButton("средний")
        btn3 = types.KeyboardButton("сложный")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'выберите сложность', reply_markup=markup)
    elif message.text == "оценка":
        p1 = "правильных: " + str(p)
        n1 = "неправильных: " + str(n)
        bot.send_message(message.chat.id, str(p1))
        bot.send_message(message.chat.id, str(n1))
    elif message.text == "да":
        if sloj == 1:
            ch1 = random.randint(0, 10)
            plus = random.choice(a)
            ch2 = random.randint(0, 10)
            w = str(ch1) + plus + str(ch2)
            print(ch1, plus, ch2)
            bot.send_message(message.chat.id, w)
        if sloj == 2:
            ch1 = random.randint(10, 100)
            plus = random.choice(a)
            ch2 = random.randint(10, 100)
            w = str(ch1) + plus + str(ch2)
            print(ch1, plus, ch2)
            bot.send_message(message.chat.id, w)
        if sloj == 3:
            ch1 = random.randint(100, 1000)
            plus = random.choice(a)
            ch2 = random.randint(100, 1000)
            w = str(ch1) + plus + str(ch2)
            print(ch1, plus, ch2)
            bot.send_message(message.chat.id, w)
        bot.send_message(message.chat.id, 'результат?')
        if plus == '+':
            r = ch1 + ch2
        if plus == '-':
            r = ch1 - ch2
        print(r)
    elif int(message.text) == r:
        bot.send_message(message.chat.id, 'правильно')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("да")

        btn2 = types.KeyboardButton("нет")
        btn3 = types.KeyboardButton("оценка")
        markup.add(btn1, btn2, btn3)
        p += 1
        bot.send_message(message.chat.id, "Хотите продолжить", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'неправильно')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("да")
        btn2 = types.KeyboardButton("нет")
        btn3 = types.KeyboardButton("оценка")
        markup.add(btn1, btn2, btn3)
        n += 1
        bot.send_message(message.chat.id, "Хотите продолжить", reply_markup=markup)


bot.polling(none_stop=True)
