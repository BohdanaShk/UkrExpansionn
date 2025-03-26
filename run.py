import asyncio  # Імпортуємо модуль для роботи з асинхронністю
from aiogram import Bot, Dispatcher, F  # Імпортуємо необхідні компоненти з бібліотеки aiogram
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from config import TOKEN
import app

reply_markup = app.key


bot = Bot(token=TOKEN)  # Ініціалізуємо об'єкт бота з токеном
dp = Dispatcher()  # Ініціалізуємо диспетчер для обробки подій (команд, повідомлень тощо)


@dp.message(CommandStart())
async def cmd_start(message: Message):
        await message.answer('Вас вітає Руттенштайнер бот! Будь ласка виберіть категорію', reply_markup = app.key)


@dp.message(F.text == 'Наші послуги')
async def cmd_text1(message: Message):
    await message.answer('Будь ласка, почекайте поки файл грузиться... ')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('rutikDOCS/Pricelist_Branch.docx'))


@dp.message(F.text == '')
async def cmd_text1(message: Message):
    await message.answer('')

@dp.message(F.text == 'Ваша філія в ЄС')
async def cmd_text1(message: Message):
    await message.answer('Будь ласка, почекайте поки файл грузиться... ')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('rutikDOCS/Prices_Sales_Distributor_2025.docx'))



@dp.message(F.text == 'Ваша компанія в ЄС')
async def cmd_text1(message: Message):
    await message.answer('Будь ласка, почекайте поки файл грузиться... ')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('rutikDOCS/Pricelist_general_services_Q1-2025.docx'))


@dp.message(F.text == 'Ваш товар в ЄС')
async def cmd_text1(message: Message):
    await message.answer('Будь ласка, почекайте поки файл грузиться... ')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('rutikDOCS/Pricelist_GMBH_Q1-2025.docx'))




@dp.message(F.text == 'Про нас')
async def cmd_text1(message: Message):
    await message.answer("""✅Більш ніж за 30 років, Ruttensteiner Business Consulting змогла побудувати безцінну широку мережу в різноманітних галузях. Саме ці контакти приносять клієнтам додаткову цінність, яку вони очікують від бізнес-консультаційної агенції. 
    
✅Швидкі та небюрократичні рішення.
Агентство виділяється серед інших своїм особливим іміджем: «Ми більше, ніж консультанти. Ми робимо все, щоб наші клієнти досягали своїх цілей», – говорить засновник і власник Дітмар Ервін Руттенштайнер. Це означає, що агентство не тільки надає консультації, але й бере на себе оперативну діяльність, таку як реєстрація представництв, активне сприяння продажу товарів клієнта, організацію та оформлення створення компаній і філій.Тим часом Руттенштайнер і його команда опікувалися компаніями з 14 країн світу. Ми раді, якщо ми також можемо зарахувати вас до наших клієнтів. 
    
    📞Ваше запитання відсилайте WhatsApp +38 0672098020 """)

@dp.message(F.text == 'Контакти📞')
async def cmd_text1(message: Message):
    await message.answer("""WhatsApp +380672098020
    Telegram +380672098020 або @Wolfgang_Bergmann""")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('бот виключений')
