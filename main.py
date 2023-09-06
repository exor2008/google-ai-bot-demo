import os

from google_ai_bot_demo.bot.bot import bot

if __name__ == "__main__":
    bot.start(os.environ["DISCORD_TOKEN"])
