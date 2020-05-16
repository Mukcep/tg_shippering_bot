import json
import logging

from aiogram import Bot, Dispatcher, executor, types


def load_token():
	try:
		f = open('config.json', 'r')
		data = json.loads(f.read())
		return data['API_TOKEN']
	except Exception as ex:
		logging.error(f'Не удалось загрузить токен! Ошибка: {str(ex)}')


API_TOKEN = load_token()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)