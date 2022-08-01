import discord
from discord.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """
        on_message event.
        """
        if message.author.bot:
            return

        print(f"{message.author}: {message.content}")

        await self.bot.process_commands(message)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EventsCog(bot))
