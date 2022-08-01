import logging
import os

from dotenv import load_dotenv

from pythonrobot_discord_bot import PythonRobot

load_dotenv(".env")


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("discord").setLevel(logging.WARNING)

    bot = PythonRobot()
    bot.run(os.environ.get("DISCORD_BOT_SECRET"), log_handler=None)


if __name__ == "__main__":
    main()
