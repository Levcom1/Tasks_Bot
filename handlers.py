from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from main import dp
from sqlighter import add, algebra, geometry


@dp.message_handler(Command('add'))
async def add_cmd(message: Message):
    s = ''.join(message.text.split('')[1:])
    await add(s)
    await message.answer('Запись успешно добавлена!')


@dp.message_handler(Command('algebra'))
async def algebra(message: Message):
    await message.answer(await algebra())


@dp.message_handler(Command('geometry'))
async def geometry(message: Message):
    await message.answer(await geometry())


@dp.message_handler(Command('russian'))
async def russian(message: Message):
    await message.answer(await russian())


@dp.message_handler(Command('litricher'))
async def litricher(message: Message):
    await message.answer(await litricher())


@dp.message_handler(Command('biology'))
async def biology(message: Message):
    await message.answer(await biology())


@dp.message_handler(Command('geography'))
async def geography(message: Message):
    await message.answer(await geography())


@dp.message_handler(Command('history'))
async def history(message: Message):
    await message.answer(await history())


@dp.message_handler(Command('obshyestvoznanie'))
async def obshyestvoznanie(message: Message):
    await message.answer(await obshyestvoznanie())


@dp.message_handler(Command('informatic'))
async def informatic(message: Message):
    await message.answer(await informatic())


@dp.message_handler(Command('english'))
async def english(message: Message):
    await message.answer(await english())


@dp.message_handler(Command('fisics'))
async def fisics(message: Message):
    await message.answer(await fisics())


@dp.message_handler(Command('chemistry'))
async def chemistry(message: Message):
    await message.answer(await chemistry())


@dp.message_handler(Command('total'))
async def total(message: Message):
    await message.answer(await total())
