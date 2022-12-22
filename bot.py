import asyncio
import logging
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5717622433:AAGxWsBsH1dVCBD3xmyI5c3ON97bj9q-XgU')

dp = Dispatcher()

@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Иди нахуй пизда тупая")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
