"""Logging configuration using python's logging + simple wrapper.

We use standard logging to be compatible with many environments; loguru can
be added optionally in dev.
"""
import logging


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger for the given name.

    The format is minimal and includes level and module.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


# module-level logger
logger = get_logger("todo_app")