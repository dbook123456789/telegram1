from asyncore import dispatcher
import requests
import json
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
updater=Updater(token= "5375484209:AAHr7wCyl9DPQzOc91G0pe1ZCgUo8Jkos3M",use_context=True)
dispatcher=updater.dispatcher
def hello (update,context):
    context.bot.send_message (chat_id=update.effective_chat.id,text ="HELLO WORLD")
hello_Handler=CommandHandler("HELLO",hello)
dispatcher.add_handler(hello_Handler)
updater.start_polling ()
    