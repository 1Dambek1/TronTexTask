from loguru import logger
import sys
import os

def setup_logging() -> None:
    logger.remove()


    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )

    logger.add(
        sys.stdout,
        level="DEBUG",
        format=log_format,
        colorize=True,
        enqueue=True
    )
