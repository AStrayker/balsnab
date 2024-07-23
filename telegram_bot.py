from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Введите сюда ваш токен API
API_TOKEN = '6072615655:AAHQh3BVU3HNHd3p7vfvE3JsBzfHiG-hNMU'
CHANNEL_ID = '@bsc_ceh'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который будет отправлять ваши сообщения в канал.')

def echo(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    context.bot.send_message(chat_id=CHANNEL_ID, text=message)

def main() -> None:
    updater = Updater(API_TOKEN)
    
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
