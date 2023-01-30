import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from filters import IsAdminFilter
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from sqlighter import SQLighter
import keyboards as kb

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


# keyboard buttons
@dp.message_handler(commands=['start'])
async def buttons(message: types.Message):
    # markup = InlineKeyboardMarkup()
    # button = InlineKeyboardButton(text='текст кнопки', callback_data='butt_id')
    # markup.add(button)

    await bot.send_message(message.chat.id, "Добро пожаловать!",
                           reply_markup=kb.markup1)
    await bot.send_message(message.chat.id, "Бот позволяет:\n• Добавлять задания\n• Удалять задания")


@dp.callback_query_handler(lambda c: c.callback == "butt_id")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "кнопка нажата")


# activate filters
dp.filters_factory.bind(IsAdminFilter)


# ban command (admins only!)
@dp.message_handler(is_admin=True, commands=['ban'], commands_prefix='!/')
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('Это команда для бана пользователя!')
        return
    await message.bot.delete_message(config.GROUP_ID, message.message_id)
    await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)
    await message.reply_to_message.reply('Пользователь забанен! Что же, бывает :)')


# # remove new user joined messages
# @dp.message_handler(content_types=['new_chat_members'])
# async def on_user_joined(message: types.Message):
#     await message.delete()


# # simple profanity check
# @dp.message_handler()
# async def filter_messages(message: types.Message):
#     if 'bad word' or 'плохое слово' in message.text:
#         # profanity detected, remove
#         await message.delete()


# initializing connection with
# db = SQLighter('db.db')


# # Command activating subscribe
# @dp.message_handler(commands=['subscribe'])
# async def subscribe(message: types.Message):
#
#     if not db.subscriber_exists(message.from_user.id):
#         # if not user in base, create it
#         db.add_subscriber(message.from_user.id)
#     else:
#         # if it still there, update his status
#         db.update_subscription(message.from_user.id, True)
#
#     await message.answer('Вы подписались на рассылку!')
#
#
# # unsubscribe command
# @dp.message_handler(commands=['unsubscribe'])
# async def unsubscribe(message: types.Message):
#     if not db.subscriber_exists(message.from_user.id):
#         # if not user in base, connect it with passive subscribe (remember it)
#         db.add_subscriber(message.from_user.id, False)
#         await message.answer('Вы и так неподписаны. Подписывайтесь! :)')
#     else:
#         # if he still there, update his status
#         db.update_subscription(message.from_user.id, False)
#         await message.answer('Вы успешно отписались')


# run long-polling
if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
