import asyncio
import logging
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from user_routers import user_router
from bot_init import tg_bot


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(user_router)
    await tg_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(tg_bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())