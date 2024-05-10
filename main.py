from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
from aiogram.types import ContentType
import logging
import os
import dotenv


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



dotenv.load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

TEXT = (f'Мы знаем, что вы являетесь обладателем Premium подписки Telegram\n'
        f'Если вы хотите поддержать бота, прошу забустить канал нашего разработчика\n'
        f'https://t.me/boost/killazDev\n'
        f'https://t.me/boost/killazDev\n'
        f'https://t.me/boost/killazDev')

admin_ids: list[int] = []
class IsAdmin(BaseFilter):
    def __init__(self,admin_ids: list[int]) -> None:
        self.admin_ids: list[int] = admin_ids

    async def __call__(self,message: Message) -> bool:
        return message.from_user.id in self.admin_ids


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
    if message.from_user.is_premium:
        await message.answer(text=TEXT)
    await message.send_copy(message.chat.id)
@dp.message(IsAdmin(admin_ids))
async def admin_call(message: Message):
    await message.answer(text='Привет админ!')


dp.message.register(process_help_info_command,Command(commands=['help','info']))
dp.message.register(process_support_command,Command(commands=['support']))
dp.message.register(process_messages)

if __name__ == '__main__':
    dp.run_polling(bot)





