import telebot
import sqlite3
from googletrans import Translator

bot = telebot.TeleBot("902231828:AAFwNVWjUJFTstm6ef-hH6mjr_OOvUiTKgg")

conn = sqlite3.connect("lang.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE if not EXISTS choice(client_id INTEGER NOT NULL PRIMARY KEY, language)""")

keyboard1=telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("English", "Russian", "Chinese", "Deutsch")
keyboard1.row("Spanish", "French", "Italian", "Polish")


@bot.message_handler(commands=['start'])
def send_start(message):
    usr_id = message.from_user.id
    conn = sqlite3.connect("lang.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT OR IGNORE INTO choice VALUES(?, 'en')""", (usr_id,))
    conn.commit()
    bot.send_message(message.chat.id, "Hi, choose a language for translation!", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_message(message):
    usr_id = message.from_user.id
    translator = Translator(service_urls=[
        'translate.google.com',
        'translate.google.co.kr',
    ])
    if message.text == "Russian":
        conn = sqlite3.connect("lang.db")
        cursor = conn.cursor()
        sql = """UPDATE choice SET language = "ru" WHERE client_id = (?)"""
        cursor.execute(sql, (usr_id,))
        conn.commit()
        bot.send_message(message.chat.id, "\U0001f1f7\U0001f1fa")
    elif message.text == "English":
        conn = sqlite3.connect("lang.db")
        cursor = conn.cursor()
        sql = """UPDATE choice SET language = "en" WHERE client_id = (?)"""
        cursor.execute(sql, (usr_id,))
        conn.commit()
        bot.send_message(message.chat.id, "\U0001F1EC\U0001F1E7")
    elif message.text == "Deutsch":
        conn = sqlite3.connect("lang.db")
        cursor = conn.cursor()
        sql = """UPDATE choice SET language = "de" WHERE client_id = (?)"""
        cursor.execute(sql, (usr_id,))
        conn.commit()
        bot.send_message(message.chat.id, "\U0001F1E9\U0001F1EA")
    elif message.text == "Spanish":
        conn = sqlite3.connect("lang.db")
        cursor = conn.cursor()
        sql = """UPDATE choice SET language = "spanish" WHERE client_id = (?)"""
        cursor.execute(sql, (usr_id,))
        conn.commit()
        bot.send_message(message.chat.id, "\U0001F1EA\U0001F1F8")
    elif message.text == "French":
        conn = sqlite3.connect("lang.db")
        cursor = conn.cursor()
        sql = """UPDATE choice SET language = "fr" WHERE client_id = (?)"""
        cursor.execute(sql, (usr_id,))
        conn.commit()
        bot.send_message(message.chat.id, "\U0001F1EB\U0001F1F7")
    elif message.text == "Italian":
        conn = sqlite3.connect("lang.db")
        cursor = conn.cursor()
        sql = """UPDATE choice SET language = "it" WHERE client_id = (?)"""
        cursor.execute(sql, (usr_id,))
        conn.commit()
        bot.send_message(message.chat.id, "\U0001F1EE\U0001F1F9")
    elif message.text == "Chinese":
        conn = sqlite3.connect("lang.db")
        cursor = conn.cursor()
        sql = """UPDATE choice SET language = "zh-cn" WHERE client_id = (?)"""
        cursor.execute(sql, (usr_id,))
        conn.commit()
        bot.send_message(message.chat.id, "\U0001F1E8\U0001F1F3")
    elif message.text == "Polish":
        conn = sqlite3.connect("lang.db")
        cursor = conn.cursor()
        sql = """UPDATE choice SET language = "pl" WHERE client_id = (?)"""
        cursor.execute(sql, (usr_id,))
        conn.commit()
        bot.send_message(message.chat.id, "\U0001F1F5\U0001F1F1")
    conn = sqlite3.connect("lang.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT language FROM choice WHERE client_id = (?)""", (usr_id,))
    p = cursor.fetchone()[0]
    res = translator.translate(message.text, dest=p)
    bot.send_message(message.chat.id, res.text)


bot.polling( none_stop=True)