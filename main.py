import asyncio
import json
from datetime import datetime
from pathlib import Path

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / 'token.env')
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise ValueError('TOKEN is missing in token.env file.')

with (BASE_DIR / 'config.json').open('r', encoding='utf-8') as f:
    config = json.load(f)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    water_reminder.start()

@tasks.loop(minutes=1)
async def water_reminder():
    now = datetime.now()

    # Only remind between 09:00 and 17:59 (you can adjust this as needed)
    if not (9 <= now.hour <= 17):
        return

    if now.minute == 0:
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

        await asyncio.sleep(60) # avoid multiple sends

if __name__ == '__main__':
    bot.run(TOKEN)