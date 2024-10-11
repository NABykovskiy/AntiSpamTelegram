from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, IS_MEMBER, IS_NOT_MEMBER, Command
from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, ChatMemberUpdated
from bot_texts import get_add_user, get_intro, get_kick_user, get_end, get_profanity_warning
from bot_init import tg_bot, dp
from check_swear import SwearingCheck

user_router = Router(name='main')
sch = SwearingCheck()
stop_flag = False


@user_router.message(CommandStart())
async def start_handler(message: Message):
    global stop_flag
    stop_flag = False
    await message.answer(get_intro())


@user_router.message()
async def echo_handler(message: Message) -> None:
    global stop_flag
    if message.text.startswith('/'):
        await commands(message)
    elif not stop_flag:
        try:
            is_profanity = sch.predict_proba(message.html_text)
            if is_profanity[0] >= 0.3:
                await message.reply(get_profanity_warning())
        except TypeError:
            pass


@user_router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def on_user_leave(event: ChatMemberUpdated):
    await tg_bot.send_message(event.chat.id, get_kick_user())


@user_router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(event: ChatMemberUpdated):
    await tg_bot.send_message(event.chat.id, get_add_user())


@user_router.chat_member(Command(*['toxta']))
async def commands(message: Message):
    if message.text == '/toxta':
        global stop_flag
        stop_flag = True
        await tg_bot.send_message(message.chat.id, get_end())
