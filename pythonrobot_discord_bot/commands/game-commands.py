import random

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


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GameCommandsCog(bot))
