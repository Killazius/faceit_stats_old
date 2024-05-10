from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
from aiogram.types import ContentType
import logging
from config import load_config


format='[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s'
logging.basicConfig(
    level=logging.DEBUG,
    format='[{asctime}] #{levelname:8} {filename}:'
           '{lineno} - {name} - {message}',
    style='{'
)
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('logs.log',mode='w')
logger.addHandler(file_handler)

config = load_config()
BOT_TOKEN = config.tg_bot.token
ADMIN_ID = config.tg_bot.admin_id

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

admin_id: str = ADMIN_ID


@dp.message(lambda msg: msg.text == '/start')
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
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.send_copy(message.chat.id)


dp.message.register(process_help_info_command,Command(commands=['help','info']))
dp.message.register(process_support_command,Command(commands=['support']))
dp.message.register(process_messages)

if __name__ == '__main__':
    dp.run_polling(bot)





