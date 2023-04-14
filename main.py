from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
import config
import re


storage = MemoryStorage()
bot = Bot(config.tg_bot_token)
dp = Dispatcher(bot, storage=storage)


class Steps(StatesGroup):
    question = State()
    communication_source = State()
    email = State()


@dp.message_handler(state="*", commands=['start', 'cancel'])
async def commands(message, state: FSMContext):
    print(f'\t{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Bot has been triggered by the user @{message["from"].username}')
    if message.text == config.start:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(config.main_option_question, callback_data='question'))
        markup.add(types.InlineKeyboardButton(config.main_option_website, url=config.website_url))
        await message.answer(config.intro_message, reply_markup=markup)
    elif message.text == config.cancel:
        await message.answer(config.cancel_message)

    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()


@dp.callback_query_handler(lambda query: query.data == "question", state=None)
async def ask_question(query):
    await Steps.question.set()
    await query.message.answer(config.ask_question_message)


@dp.message_handler(lambda message: message.text not in config.commands, state=Steps.question)
async def get_question(message, state: FSMContext):
    user_nickname = message['from'].username
    question = message.text
    async with state.proxy() as data:
        data['nick_name'] = user_nickname
        data['question'] = question
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(config.communication_option_tg, callback_data='telegram'))
    markup.add(types.InlineKeyboardButton(config.communication_option_email, callback_data='email'))
    await message.answer(config.ask_source_message, reply_markup=markup)
    await Steps.next()


@dp.callback_query_handler(lambda query: query.data in ['telegram', 'email'], state=Steps.communication_source)
async def get_source(query, state: FSMContext):
    communication_source = query.data
    async with state.proxy() as data:
        data['communication_source'] = communication_source
    if communication_source == 'telegram':
        await state.finish()
        await final(query.message, data)
    elif communication_source == 'email':
        await Steps.next()
        await query.message.answer(config.ask_email_message)


@dp.message_handler(lambda message: message.text not in config.commands, state=Steps.email)
async def ask_email(message, state: FSMContext):
    email = message.text
    if re.match(config.email_pattern, email):
        async with state.proxy() as data:
            data['email'] = email
        await state.finish()
        await final(message, data)
    else:
        await message.answer(config.invalid_email_message)


async def final(message, data):
    await message.answer(config.bye_message, parse_mode='html')
    channel = data["communication_source"]
    email_str = ""
    if channel == 'email':
        email_str = f'\n○ Email: {data["email"]}'
    notif_message = f'Hi there,\n\nA new user left a question through the bot:\n\n○ Username: @{data["nick_name"]}\n○ Question: {data["question"]}\n○ Send Reply to: {channel.capitalize()}' + email_str
    await bot.send_message('-957758757', notif_message)


if __name__ == '__main__':
    print('Bot was launched successfully.')
    executor.start_polling(dp, skip_updates=True)
