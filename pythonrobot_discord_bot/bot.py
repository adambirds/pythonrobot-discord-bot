import os
from logging import Logger, getLogger

import discord
from aiohttp import ClientSession
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True


class PythonRobot(commands.AutoShardedBot):
    logger: Logger
    session: ClientSession

    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        super().__init__(
            case_insensitive=True, command_prefix="!", help_command=None, intents=intents
        )

        self.logger = getLogger("bot")

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

    async def on_ready(self) -> None:
        self.logger.info("Booted up")
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="!help")
        )
