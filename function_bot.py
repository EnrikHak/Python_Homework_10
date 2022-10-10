from datetime import datetime
from itertools import count
from random import randint
from tkinter import *


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет, друг!Как дела, что нового?')


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!!!')


def time(update, context):
    context.bot.send_message(update.effective_chat.id, (f'{datetime.now().time()}'))


#   Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)

def abc(update, context):
    text = update.message.text
    t_without = " ".join(list(filter(lambda x: 'абв' not in x.lower(), text.split())))
    context.bot.send_message(update.effective_chat.id, t_without)


#   Игра в конфеты


def game(update, context):
    context.bot.send_message(update.effective_chat.id, f'{update.effective_user.first_name}, приветствую в игре Конфеты\nИдет жребий\n')
    candies = randint(100, 2000)
    context.bot.send_message(update.effective_chat.id, f'Конфет насыпано {candies}')
    pl = randint(0,1)
    while candies > 0:
        if pl == 1:
            count_pl = 0
            context.bot.send.message(update.effective_chat.id, f'Ходит {update.effective_user.first_name}')
            if candies >= 28:
                context.bot.send_message(update.effective_chat.id,"Сколько взять конфет?(от 1 до 28): ")
                take_candies = int(update.message.text)
                while take_candies < 1 or take_candies > 28:
                    context.bot.send_message(update.effective_chat.id, "Ошибочка, попробуйте заново\nСколько взять конфет?(от 1 до 28): ")
                    take_candies = int(update.message.text)
            else:
                context.bot.send_message(update.effective_chat.id, f"Сколько взять конфет?(от 1 до {candies}): ")
                take_candies = int(update.message.text)
                while take_candies < 1 or take_candies > candies:
                    context.bot.send_message(update.effective_chat.id, f"Ошибочка, попробуй заново\nСколько взять конфет?(от 1 до {candies}): ")
                    take_candies = int(update.message.text)

            candies = candies - take_candies
            context.bot.send_message(update.effective_chat.id, f'{update.effective_user.first_name} взял: {take_candies}\nОсталось {candies} конфет')
            if pl == 1 and candies == 0:
                result = f'Выиграл {update.effective_user.first_name}'
                context.bot.send.message(update.effective_chat.id, result)
                count_pl += 1
        
        
        if pl == 0:
            count_bot = 0
            context.bot.send.message(update.effective_chat.id, f'Ходит R_bot')
            take_candies = candies % 29
            if take_candies == 0:
                take_candies = 1
            candies = candies - take_candies
            context.bot.send_message(update.effective_chat.id, f"R_bot взял {take_candies}\nОсталось {candies} конфет")
            if pl == 0 and candies == 0:
                result = 'Выиграл R_bot'
                context.bot.send.message(update.effective_chat.id, result)
                count_bot += 1

                return result

                



def clicker(update, context, count, count_pl, count_bot):
    context.bot.send_message(update.effective_chat.id, f'Общее количество сыграных игр {count}')
    context.bot.send_message(update.effective_chat.id, f'Победы игрока - {count_pl}')
    context.bot.send_message(update.effective_chat.id, f"Победы R_bot'a - {count_bot}")