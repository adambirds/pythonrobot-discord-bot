from datetime import datetime

import discord
import pytz
from discord import app_commands
from discord.ext import commands


class UtilCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(description="Give the current time in any timezone.")
    async def time(self, interaction: discord.Interaction, *, timezone: str) -> None:
        """
        /time command.
        """
        timezone = timezone.replace(" ", "_")
        if timezone in pytz.all_timezones:
            date_time = datetime.now(pytz.timezone(timezone)).strftime("%A %-dth %B %Y %H:%M")
            await interaction.response.send_message(
                content=f"The date and time in {timezone} is {date_time}."
            )
        else:
            await interaction.response.send_message(content=f"{timezone} is not a valid timezone.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UtilCommandsCog(bot))
