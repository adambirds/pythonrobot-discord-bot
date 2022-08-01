from discord.ext import commands


class AdminCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.has_role("Admins")
    @commands.command()
    async def syncbot(self, ctx: commands.Context) -> None:
        await self.bot.tree.sync()
        await ctx.send("Slash commands have been synchronized on this server")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AdminCommandsCog(bot))
