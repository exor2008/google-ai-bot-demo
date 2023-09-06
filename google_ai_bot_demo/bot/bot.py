from interactions import Client, Intents

from google_ai_bot_demo.utils import logger

bot = Client(
    intents=Intents.DEFAULT | Intents.GUILD_MESSAGES,
    sync_interactions=True,
    asyncio_debug=True,
    logger=logger,
)


@bot.listen()
async def on_ready():
    logger.info(f"This bot is owned by {bot.owner}")


bot.load_extension("google_ai_bot_demo.bot.commands")
