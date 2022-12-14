#########################################################
from config import bot
import config
from time import sleep
import re

#########################################################
# Aquí vendrá la implementación de la lógica del bot
#########################################################

@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "Hola, soy un \U0001F916, ¿cómo estás?",
        parse_mode="Markdown")

@bot.message_handler(commands=['ping'])
def on_command_ping(message):
    sleep(1)
    bot.send_message(
        message.chat.id,
        "pong",
        parse_mode="Markdown")
        
@bot.message_handler(regexp=r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_add(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    
    parts = re.match(
        r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
        message.text,
        flags=re.IGNORECASE)
    
    # print (parts.groups())

    oper1 = float(parts[1])
    oper2 = float(parts[3])

    result = oper1 + oper2
    
    bot.reply_to(
        message,
        f"\U0001F522 Resultado: {result}")  
    
#########################################################
# Siempre al final
#########################################################
if __name__ == '__main__':
    bot.polling(timeout=20)
    
#########################################################