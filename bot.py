import os
import asyncio
import logging
from aiogram import Bot
from dotenv import load_dotenv
from get_yuan_rate import get_yuan_rate

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN") 
CHANNEL_ID = os.getenv("CHANNEL_ID")  

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=TOKEN)


async def send_yuan_rate():
    try:
        rate = get_yuan_rate()
        if rate is None:
            logging.error("Не удалось получить курс юаня!")
            return

        message = f"🇨🇳 Курс юаня на сегодня: {rate:.2f} ₽"
        logging.info(f"Отправка сообщения: {message} в {CHANNEL_ID}")

        await bot.send_message(CHANNEL_ID, message)
        logging.info("Сообщение успешно отправлено!")

    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения: {e}")

    finally:
        await bot.session.close()  # Закрываем соединение с Telegram API


if __name__ == "__main__":
    asyncio.run(send_yuan_rate())
