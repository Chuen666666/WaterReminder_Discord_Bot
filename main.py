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
        try:
            if config['isDM']:
                user = await bot.fetch_user(config['ID'])
                await user.send("💧 It's time to drink water!")
            else:
                channel = bot.get_channel(config['ID'])
                if channel is None:
                    channel = await bot.fetch_channel(config['ID'])
                await channel.send("💧 It's time to drink water!")

            print(f'[{now}] Reminder sent.')
            await asyncio.sleep(60) # avoid multiple sends

        except Exception as e:
            print(f'Error sending reminder: {e}')


if __name__ == '__main__':
    bot.run(TOKEN)