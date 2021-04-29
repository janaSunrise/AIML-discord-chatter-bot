import os

import discord

from bot import Bot, config

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_NAME = os.getenv("CHANNEL_NAME")

PREFIX = config.COMMAND_PREFIX

intents = discord.Intents.all()
intents.presences = False

bot = Bot(
    version="0.0.1",
    channel_name=CHANNEL_NAME,
    command_prefix=PREFIX,
    intents=intents,
    activity=discord.Game(name=f"Talk with me in #{CHANNEL_NAME} :)"),
    case_insensitive=True,
    owner_ids=config.devs,
    heartbeat_timeout=150.0,
)

# -- Run when this file is invoked --
if __name__ == "__main__":
    bot.run(TOKEN)
