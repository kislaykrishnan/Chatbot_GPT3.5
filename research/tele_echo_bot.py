import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
#print(API_TOKEN)

#configure logging
logging.basicConfig(level=logging.INFO)

#Intialize a bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#start/help command replier
@dp.message_handler(commands=["hi", 'start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` ot `/help` or `hi`  command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.reply("Hi\nI am Echo Bot!\nPowered by aiogram.")


#any command replier
@dp.message_handler()
async def echo(message: types.Message):
    """
    This handler will return echo
    """
    await message.answer(message.text)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

#after writing the above function,the telebot gives answer as what you write to it.This is just to check that we have successfully connected with the bot and it is responsive.
#now after checking this,we will try and add AI response functionality to the chatbot.
