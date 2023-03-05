from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='5437617243:AAHhqnpxBF22RvJCvroqJ_tAdkQXU37xYCg')
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    #chat_id = message.chat.id
    #text = "Я текстовый бот, поговорим?"
    #sent_messages = await bot.send_message(chat_id=chat_id, text=text)
    #print(sent_messages.to_python())
    #sent_message = await bot.send_photo(chat_id=chat_id,
                         #photo='https://japanorama39.ru/wp-content/uploads/2020/05/3-donnykimball.com_.jpg')
    #print(sent_message.photo[-1].file_unique_id)
    #result = await bot.set_chat_title(chat_id=-848752647, title='New name')
    #print(result)
    #invite_link = await bot.export_chat_invite_link(chat_id=-848752647)
    #print(invite_link)
    bot_user = await bot.get_me()
    print(bot_user.username)
executor.start_polling(dp)
