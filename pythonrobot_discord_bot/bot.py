import os

import discord
from aiohttp import ClientSession
from discord.client import _log
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True


class PythonRobot(commands.AutoShardedBot):
    session: ClientSession

    QUOTES_API = "https://api.quotable.io/random"

    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        super().__init__(
            case_insensitive=True, command_prefix="!", help_command=None, intents=intents
        )

        self.logger = _log

    async def setup_hook(self) -> None:
        self.session = ClientSession()

        for folder in ["commands", "events"]:
            for extension in [
                f[:-3] for f in os.listdir(f"pythonrobot_discord_bot/{folder}") if f.endswith(".py")
            ]:
                try:
                    await self.load_extension(f"pythonrobot_discord_bot.{folder}.{extension}")
                except commands.errors.ExtensionFailed as exc:
                    self.logger.warning("Skipped %s.%s: %s", folder, extension, exc.__cause__)

    async def close(self) -> None:
        if self.session is not None:
            await self.session.close()
        self.logger.info("Exited")
        await super().close()

    async def on_ready(self) -> None:
        self.logger.info("Booted up")
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="!help")
        )

    async def on_message(self, message: discord.Message) -> None:
        """
        on_message event.
        """
        if message.author.bot:
            return

        self.logger.info(f"{message.author}: {message.content}")

        await self.process_commands(message)
