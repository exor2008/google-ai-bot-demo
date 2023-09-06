import asyncio
import os
import traceback

from interactions import (
    Embed,
    Extension,
    OptionType,
    SlashContext,
    slash_command,
    slash_option,
)
from interactions.ext.paginators import Paginator

from google_ai_bot_demo.ai import generate
from google_ai_bot_demo.utils import logger

TEMPERATURE = float(os.getenv("TEMPERATURE"))
CANDIDATES = int(os.getenv("CANDIDATES"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
PAGINATION = int(os.getenv("PAGINATION"))


class ChatCommands(Extension):
    @slash_command("ask", description="Ask question")
    @slash_option(
        "question",
        "Your question for AI",
        OptionType.STRING,
        required=True,
    )
    async def ask(self, ctx: SlashContext, question: str):
        await ctx.defer()

        loop = asyncio.get_running_loop()
        resp = await loop.run_in_executor(
            None, generate, question, TEMPERATURE, CANDIDATES, MAX_TOKENS
        )
        for i, candidate in enumerate(resp.candidates):
            txt = candidate["output"]

            # if len(resp) > PAGINATION:
            #     paginator = Paginator.create_from_string(
            #         ctx.bot, txt, page_size=PAGINATION
            #     )
            #     await paginator.send(ctx)
            # else:
            #     await ctx.respond(resp)
            embed = get_embed(i, txt, question)
            await ctx.send(embed=embed)

    @ask.error
    async def say_error(self, e, *args, **kwargs):
        logger.error(f"Error in /ask\nTrace: {traceback.format_exc()}")


def get_embed(variant: int, text: str, question: str) -> Embed:
    embed = Embed(
        title=f"Variant {variant + 1}",
        description=text,
        footer=f"Question was: {question}",
    )

    return embed
