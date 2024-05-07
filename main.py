import requests
import time


API_URL: str = f'https://api.telegram.org/bot'
BOT_TOKEN: str = '6602485432:AAHsV-VP6Y-ETdIcbNYhWCmH4zLfLGA6ySw'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            username = result['message']['from']['username']
            user_text = result['message']['text']
            print(username,user_text)
            TEXT: str = f'Привет @{username}, это FACEIT STATS!'
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
    time.sleep(5)
    counter += 1

