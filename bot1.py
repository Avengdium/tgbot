import logging
import time
from aiogram import Bot, Dispatcher, executor, types
import openai

bot_token = '6200885139:AAFrlCeEENOar9MD5j-U_-_6HmSIvCb8CwM'
openai.api_key = "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"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

messages = {}

@dp.message_handler(text="Кто тебя создал?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто твой создатель?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Who is u'r owner?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто твой разработчик?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Who is your owner?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Who is your owner")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто тебя создал")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто твой создатель")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Who is u'r owner")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто твой разработчик")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто твой разраб?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто твой разраб")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто тебя создал?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто твой разработал")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто тебя разработал?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто тебя разработал?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто тебя разработал")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Who is u'r owner?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Кто твой разработчик?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="Who is your owner?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="who is your owner")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="кто тебя создал")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="кто твой создатель")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="who is u'r owner")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="кто твой разработчик")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="кто твой разраб?")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(text="кто твой разраб")
async def hello(message: types.Message):
    await message.answer("Меня создал Артём Вахтин")

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    try:
        username = message.from_user.username
        messages[username] = []
        await message.answer("Приветствую тебя, тестер. \nДанный бот принадлежит Артёму Вахтину.\nENG SUPPORT! \nRU SUPPORT! \nВерсия ИИ = 2.0\nДля очистки памяти ИИ пропишите /clearhistory")
        await message.answer_animation(
  animation="https://tenor.com/view/dog-gif-25785256"
)
    except Exception as e:
        logging.error(f'Ошибочка случилась {e}')


@dp.message_handler(commands=['clearhistory'])
async def new_topic_cmd(message: types.Message):
    try:
        username = message.from_user.username
        messages[username] = []
        await message.reply('* * * \n\nПамять очищена, ИИ больше не помнит старую переписку * * *', parse_mode='Markdown')
    except Exception as e:
        logging.error(f'Ошибочка: {e}')


@dp.message_handler()
async def echo_msg(message: types.Message):
    try:
        user_message = message.text
        username = message.from_user.username

        if username not in messages:
            messages[username] = []
        messages[username].append({"role": "user", "content": user_message})
        messages[username].append({"role": "user", "content": f"chat: {message.chat} Сейчас {time.strftime('%d/%m/%Y %H:%M:%S')} user: {message.from_user.first_name} message: {message.text}"})
        logging.info(f'{username}: {user_message}')

        should_respond = not message.reply_to_message or message.reply_to_message.from_user.id == bot.id

        if should_respond:
            processing_message = await message.reply(
                '* * * \n\nГенерирую ответ....* * *',
                parse_mode='Markdown')
            await bot.send_chat_action(chat_id=message.chat.id, action="typing")
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages[username],
                max_tokens=1000,
                temperature=0.7,
                frequency_penalty=0,
                presence_penalty=0,
                user=user_message
            )
            chatgpt_response = completion.choices[0]['message']
            messages[username].append({"role": "assistant", "content": chatgpt_response['content']})
            logging.info(f'bot response: {chatgpt_response["content"]}')
            await message.reply(chatgpt_response['content'])
            await bot.delete_message(chat_id=processing_message.chat.id, message_id=processing_message.message_id)
    except Exception as ex:
        if ex == 'context_length_exceeded':
            await message.reply(
                'The bot ran out of memory, re-creating the dialogue * * * \n\nУ бота закончилась память, пересоздаю диалог * * *',
                parse_mode='Markdown')
            await new_topic_cmd(message)
            await echo_msg(message)


if __name__ == '__main__':
    executor.start_polling(dp)