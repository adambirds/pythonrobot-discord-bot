import discord
from discord import app_commands
from discord.ext import commands


class SocialCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(description="Lists social links.")
    async def socials(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title="Socials", description="", color=discord.Colour.red())
        embed.add_field(name="GitHub", value="https://github.com/adambirds")
        embed.add_field(name="Twitch", value="https://twitch.tv/codingandgamingwithadam")
        embed.add_field(name="\u200b", value="\u200b")
        embed.add_field(
            name="YouTube", value="https://www.youtube.com/channel/UCOJ37qE6yr-7fspsgzpTGkQ"
        )
        embed.add_field(name="Instagram", value="https://instagram.com/adambirds")
        embed.add_field(name="\u200b", value="\u200b")
        embed.add_field(name="Facebook", value="https://facebook.com/adbwebdesigns")
        embed.add_field(name="Twitter", value="https://twitter.com/adbwebdesigns")
        embed.add_field(name="\u200b", value="\u200b")
        embed.add_field(name="TikTok", value="https://tiktok.com/username")
        embed.add_field(name="Reddit", value="https://reddit.com/username")
        embed.add_field(name="\u200b", value="\u200b")
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SocialCommandsCog(bot))
