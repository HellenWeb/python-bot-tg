
# Modules

import telebot
from telebot import types
import random
import config

# Default Varibles

bot = telebot.TeleBot(config.token)

# Logic Bot

# Welcome Message

@bot.message_handler(commands=['start'])
def welcome_message(message):
    if message:

        # Add Stiker from folders "static"

        sti = open('static/welcomesticker.tgs', 'rb')
        bot.send_sticker(message.chat.id, sti)

        # Menu

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        # Button Menu

        item1 = types.KeyboardButton('🆘  Help')
        item2 = types.KeyboardButton('❓  Random numbers')

        # Add Button

        markup.add(item1, item2)

        # Welcome Message

        bot.send_message(message.chat.id, f"<strong>Hello this is a test bot!</strong> 😄\nRepository - https://github.com/HellenWeb/python-bot-tg\nCreator @YungHellen", format(message.from_user), bot.get_me(), 
        parse_mode='html', reply_markup=markup)

# Help Command

@bot.message_handler(commands=['help'])
def help_command(message):
    if message:

        # Add Message

        bot.send_message(message.chat.id, f"<strong>Commands:</strong>\n/start - start bot\n/help - list command\n/random - random number\n/info - information about the creator", format(message.from_user), bot.get_me(), 
        parse_mode='html')  

# Random Command

@bot.message_handler(commands=['random'])
def random_command(message):
    if message:

        # Variebles with result User and Robot

        me = random.randint(1, 6)
        robot = random.randint(1, 6)
        
        # Menu inline

        markupInline = types.InlineKeyboardMarkup(row_width=1)
        itemIn = types.InlineKeyboardButton('🔵 Again', callback_data=again)

        markupInline.add(itemIn)

        # Сonditions

        if me > robot:
            bot.send_message(message.chat.id, f"You - <strong>{me}</strong>\nI - <strong>{robot}</strong>\nYou won, congratulations 👏", format(message.from_user), bot.get_me(), 
            parse_mode='html', reply_markup=markupInline)
        else:
            bot.send_message(message.chat.id, f"You - <strong>{me}</strong>\nI - <strong>{robot}</strong>\nYou've lost but don't be upset 😌", format(message.from_user), bot.get_me(), 
            parse_mode='html', reply_markup=markupInline) 

# Info Command

@bot.message_handler(commands=['info'])
def info_messsage(message):
    if message:
        bot.send_message(message.chat.id, f"<strong>Creator:</strong>\nGithub - https://github.com/HellenWeb\nTelegram - @YungHellen", format(message.from_user), bot.get_me(), 
        parse_mode='html')            

# Menu Command

@bot.message_handler(content_types=['text'])
def menu_command(message):
    if message:
        if message.chat.type == 'private':
            if message.text == '🆘  Help':
                bot.send_message(message.chat.id, f"<strong>Commands:</strong>\n/start - start bot\n/help - list command\n/random - random number\n/info - information about the creator", format(message.from_user), bot.get_me(), 
                parse_mode='html')  
            elif message.text == '❓  Random numbers':
                me = random.randint(1, 6)
                robot = random.randint(1, 6)
                if me > robot:
                    bot.send_message(message.chat.id, f"You - <strong>{me}</strong>\nI - <strong>{robot}</strong>\nYou won, congratulations 👏", format(message.from_user), bot.get_me(), 
                    parse_mode='html')
                else:
                    bot.send_message(message.chat.id, f"You - <strong>{me}</strong>\nI - <strong>{robot}</strong>\nYou've lost but don't be upset 😌", format(message.from_user), bot.get_me(), 
                    parse_mode='html')   

bot.polling(non_stop=True)

# \\ ||




