import logging
import os

from discord.client import _ColourFormatter
from dotenv import load_dotenv

from pythonrobot_discord_bot.bot import PythonRobot

load_dotenv(".env")


def main() -> None:
    bot = PythonRobot()
    bot.run(
        os.environ.get("DISCORD_BOT_SECRET"),
        log_handler=logging.StreamHandler(),
        log_formatter=_ColourFormatter(),
        log_level=logging.INFO,
    )


if __name__ == "__main__":
    main()
