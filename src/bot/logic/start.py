from aiogram import types


async def start(message: types.Message) -> None:
    await message.answer("<b>Testing was successful</b>")
