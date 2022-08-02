from datetime import datetime
from typing import Literal

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

    @app_commands.command(description="Calculate simple maths.")
    async def calculator(
        self,
        interaction: discord.Interaction,
        value1: str,
        operator: Literal["+", "-", "*", "/"],
        value2: str,
    ) -> None:
        """
        /calculator command
        """
        try:
            value1_int = float(value1)
            value2_int = float(value2)
        except:
            return await interaction.response.send_message(
                content=f"<@{interaction.user.id}> you submitted an invalid number for your calculation."
            )

        match operator:
            case "+":
                answer = value1_int + value2_int
            case "-":
                answer = value1_int - value2_int
            case "*":
                answer = value1_int * value2_int
            case "/":
                try:
                    answer = value1_int / value2_int
                except:
                    return await interaction.response.send_message(
                        f"<@{interaction.user.id}> you can't divide by 0."
                    )

            case _:
                return await interaction.response.send_message(
                    f"<@{interaction.user.id}> you submitted an invalid operator."
                )

        await interaction.response.send_message(f"<@{interaction.user.id}> the answer is {answer}.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UtilCommandsCog(bot))
