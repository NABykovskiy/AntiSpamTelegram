from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, IS_MEMBER, IS_NOT_MEMBER
from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, ChatMemberUpdated
from bot_texts import get_add_user, get_intro, get_kick_user, get_leave_user
from bot_init import tg_bot

user_router = Router(name='main')


@user_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(get_intro())


@user_router.message()
async def echo_handler(message: Message) -> None:
    try:
        print(message.html_text)
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        pass


@user_router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def on_user_leave(event: ChatMemberUpdated):
    await tg_bot.send_message(event.chat.id, get_kick_user())


@user_router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(event: ChatMemberUpdated):
    await tg_bot.send_message(event.chat.id, get_add_user())


@user_router.message_handler(commands=['stats'])
async def my_command(message: Message):
    await message.reply("Это ваша команда!")
