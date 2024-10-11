import asyncio
import logging
from user_routers import user_router
from bot_init import tg_bot, dp


async def main():
    dp.include_router(user_router)
    await tg_bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(tg_bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    