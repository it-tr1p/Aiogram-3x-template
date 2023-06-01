__all__ = ["register_user_commands"]

from aiogram import Router
from aiogram.filters import CommandStart

from .start import start


def register_user_commands(router: Router) -> None:
    # Register commands
    router.message.register(start, CommandStart())

    # Register callbacks
