import random
from typing import Literal

import discord
from discord import app_commands
from discord.ext import commands

from pythonrobot_discord_bot.bot import PythonRobot


class GameCommandsCog(commands.Cog):
    def __init__(self, bot: PythonRobot) -> None:
        self.bot = bot

    @app_commands.command(name="8ball", description="The bot will reply to a yes or no question.")
    async def eight_ball(self, interaction: discord.Interaction, *, question: str) -> None:
        """
        /8ball command
        """
        POSSIBLE_ANSWERS = [
            "Of Course",
            "Yes",
            "No",
            "Of Course Not",
            "Definitely",
            "Definitely Not",
        ]
        if question != "":
            list_length = len(POSSIBLE_ANSWERS)
            answer = POSSIBLE_ANSWERS[random.randint(0, list_length - 1)]

            embed = discord.Embed(title=question, color=discord.colour.parse_hex_number("CE031B"))
            embed.description = answer
            await interaction.response.send_message(embed=embed)
        else:
            return

    @app_commands.command(description="The bot will reply with na random quote.")
    async def quote(self, interaction: discord.Interaction) -> None:
        """
        /quote command
        """
        async with self.bot.session.get(self.bot.QUOTES_API) as r:
            json_data = await r.json(content_type="application/json")
        await interaction.response.send_message(
            content=f"{json_data['author']}: \"{json_data['content']}\""
        )

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
    await bot.add_cog(GameCommandsCog(bot))
