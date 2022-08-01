import discord
from discord import app_commands
from discord.ext import commands


class SocialCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(description="Help Command")
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title="Help", description="This is a help command", color=0x00FF00)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SocialCommandsCog(bot))
