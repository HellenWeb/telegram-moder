# Import

import aiogram
from aiogram import types, executor
from dispacher import bot, dp

# Commands

"""Command <Start>"""


@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message):
    mark = types.InlineKeyboardMarkup(row_width=2)
    mark.add(
        types.InlineKeyboardButton(
            text="Repository", url="https://github.com/HellenWeb/telegram-moder"
        ),
        types.InlineKeyboardButton(text="Help", callback_data="help"),
    )
    await message.answer(
        f"<strong>Hello {message.from_user.first_name}</strong>\n\n- <strong>I will help you with the management of your group</strong>\n- I can issue block warnings and participate in chat administration\n\n<strong>Creator @YungHellen</strong>",
        reply_markup=mark,
        parse_mode="html",
    )


"""Command <Commands>"""


@dp.message_handler(commands=["commands"])
async def commands(message: types.Message):
    await message.answer(
        f"<strong>/start or /help</strong> = starting message\n<strong>/report</strong> = Throw warning\n<strong>/commands</strong> = All commands",
        parse_mode="html",
    )

# Delete <Join> Message

@dp.message_handler(content_types=['new_join_message'])
async def clear(message: types.Message):
    await message.delete()


# Callback


@dp.callback_query_handler(lambda m: m.data == "help")
async def help_call(callback: types.CallbackQuery):
    mark = types.InlineKeyboardMarkup(row_width=2)
    mark.add(
        types.InlineKeyboardButton(
            text="Repository", url="https://github.com/HellenWeb/telegram-moder"
        ),
        types.InlineKeyboardButton(text="Back", callback_data="back"),
    )
    await bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        text=f"<strong>/start or /help</strong> = starting message\n<strong>/report</strong> = Throw warning\n<strong>/commands</strong> = All commands",
        reply_markup=mark,
        parse_mode="html"
    )


@dp.callback_query_handler(lambda r: r.data == "back")
async def back(callback: types.CallbackQuery):
    mark = types.InlineKeyboardMarkup(row_width=2)
    mark.add(
        types.InlineKeyboardButton(
            text="Repository", url="https://github.com/HellenWeb/telegram-moder"
        ),
        types.InlineKeyboardButton(text="Help", callback_data="help"),
    )
    await bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        text=f"<strong>Hello {callback.message.from_user.first_name}</strong>\n\n- <strong>I will help you with the management of your group</strong>\n- I can issue block warnings and participate in chat administration\n\n<strong>Creator @YungHellen</strong>",
        reply_markup=mark,
        parse_mode="html"
    )


# Polling

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
