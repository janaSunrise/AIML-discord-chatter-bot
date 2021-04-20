from datetime import datetime

import discord
from discord.ext.commands import Cog, command, cooldown, BucketType
from loguru import logger


class Main(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @Cog.listener("on_message")
    async def on_message_handle(self, message):
        if message.author.bot or str(message.channel) != self.bot.channel_name:
            return

        if message.content is None:
            logger.error("Empty message received!")
            return

        text = message.content
        for character in ["/", "'", ".", "\\", "(", ")", '"', "\n", "@", "<", ">"]:
            text = text.replace(character, "")

        response = self.bot.aiml_kernel.respond(text).replace("://", "").replace("@", "")
        response = f"`{message.author.name}`: {response}"

        if len(response) > 1800:
            response = response[0:1800]

        await message.channel.send(response)

    @command()
    @cooldown(1, 600, BucketType.user)
    async def reset(self, ctx) -> None:
        now = datetime.now()

        self.bot.last_reset_time = now
        await ctx.channel.send(
            embed=discord.Embed(
                description="Resetting info",
                color=discord.Color.green()
            )
        )
        self.bot.aiml_kernel.resetBrain()
        self.bot.setup_aiml()


def setup(bot) -> None:
    bot.add_cog(Main(bot))
