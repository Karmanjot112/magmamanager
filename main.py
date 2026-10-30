import asyncio
import logging

from config.settings import Settings
from core.bot import MagmaBot
from core.logging import configure_logging


async def run() -> None:
    settings = Settings.from_env()
    configure_logging(settings.log_level)
    bot = MagmaBot(settings)
    try:
        await bot.start(settings.discord_token)
    finally:
        await bot.close()


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        logging.getLogger("magma_manager").info("Shutdown requested.")