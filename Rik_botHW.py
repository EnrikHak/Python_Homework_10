from asyncore import dispatcher
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from function_bot import start, cancel, time, abc, game, clicker



bot = Bot(token='')
update = Updater(token='')
dispatcher = update.dispatcher




start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
time_handler = CommandHandler('time', time)
abc_handler = MessageHandler(Filters.text, abc)
game_handler = MessageHandler(Filters.text, game)
clicker_handler = CommandHandler('clicker', clicker)




dispatcher.add_handler(start_handler)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(time_handler)
dispatcher.add_handler(abc_handler)
dispatcher.add_handler(game_handler)
dispatcher.add_handler(clicker_handler)



print('server start')
update.start_polling()
update.idle()