import discord
from discord import app_commands
from discord.ext import commands


class SocialCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(description="Lists social links.")
    async def socials(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title="Socials", description="", color=discord.Colour.red())
        embed.add_field(name="GitHub", value="https://github.com/adambirds", inline=False)
        embed.add_field(
            name="Twitch", value="https://twitch.tv/codingandgamingwithadam", inline=False
        )
        embed.add_field(
            name="YouTube",
            value="https://www.youtube.com/channel/UCOJ37qE6yr-7fspsgzpTGkQ",
            inline=False,
        )
        embed.add_field(name="Instagram", value="https://instagram.com/adambirds", inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SocialCommandsCog(bot))
