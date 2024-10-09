from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

user_router = Router(name='main')

@user_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я бот Мурик и я буду бороться со спамерами")
