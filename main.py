import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
from flask import Flask
from threading import Thread

# Keep bot alive on Render
app = Flask(__name__)
@app.route('/')
def home():
    return "I'm alive!"
def run():
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

BASE_DIR = Path(__file__).resolve().parent

if os.path.exists('/etc/secrets/config.json'):
    CONFIG_PATH = Path('/etc/secrets/config.json')
elif (BASE_DIR / 'config.json').exists():
    CONFIG_PATH = BASE_DIR / 'config.json'
else:
    CONFIG_PATH = Path('config.json')

try:
    with CONFIG_PATH.open('r', encoding='utf-8') as f:
        config = json.load(f)
    print(f'成功讀取設定檔：{CONFIG_PATH}')
except Exception as e:
    print(f'讀取設定檔失敗！路徑：{CONFIG_PATH}，錯誤：{e}')

TOKEN = os.getenv('TOKEN')

if not TOKEN:
    load_dotenv(dotenv_path=BASE_DIR / 'token.env')
    TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    water_reminder.start()

@tasks.loop(minutes=1)
async def water_reminder():
    # Use GMT+8 timezone (you can adjust this as needed)
    tz_tw = timezone(timedelta(hours=8))
    now = datetime.now(tz_tw)

    # Only remind between 09:00 and 17:59 (you can adjust this as needed)
    if (now.minute == 0) and (9 <= now.hour <= 17):
        print(f'[{now.strftime('%Y-%m-%d %H:%M:%S')}] Starting hourly water reminder...')

        for user_id in config.get('IDS', []):
            try:
                if config['isDM']:
                    user = await bot.fetch_user(user_id)
                    await user.send('💧 Time to drink water! Stay hydrated! 💧')
                else:
                    channel = bot.get_channel(user_id)
                    if channel is None:
                        channel = await bot.fetch_channel(user_id)
                    await channel.send('💧 Time to drink water! Stay hydrated! 💧')
                
                print(f'[{now}] Sent water reminder to {user_id}')

            except Exception as e:
                print(f'Error sending to {user_id}: {e}')

if __name__ == '__main__':
    if TOKEN:
        keep_alive()
        bot.run(TOKEN)
    else:
        print('Error! TOKEN not found!')