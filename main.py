from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType

BOT_TOKEN: str = '6602485432:AAHsV-VP6Y-ETdIcbNYhWCmH4zLfLGA6ySw'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.reply(''
                         'Привет!\nЯ бот, '
                         'который поможет тебе отслеживать твою статистику.\n'
                         'Жду твоих команд!')
async def process_help_info_command(message: Message):
    await message.answer('Здесь будет список моих команд!')
async def process_support_command(message: Message):
    await message.answer('@killazius - пиши скорее,если ты нашел баг/недочет в боте, '
                         'либо просто хочешь подкинуть мне идею')

async def process_messages(message: Message):
    await message.send_copy(message.chat.id)

dp.message.register(process_start_command,Command(commands=['start']))
dp.message.register(process_help_info_command,Command(commands=['help','info']))
dp.message.register(process_support_command,Command(commands=['support']))
dp.message.register(process_messages)

if __name__ == '__main__':
    dp.run_polling(bot)