import discord
from discord.ext import commands

from pythonrobot_discord_bot.bot import PythonRobot


class EventsCog(commands.Cog):
    def __init__(self, bot: PythonRobot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild) -> None:
        self.bot.logger.info(f"Joined {guild.name}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EventsCog(bot))
