import os
import asyncio
import logging
from datetime import datetime
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

        # Дата в формате ДД.ММ.ГГГГ
        today_date = datetime.now().strftime("%d.%m.%Y")
        
        # Рассчитываем курсы с надбавками
        rate_200 = rate + 0.8
        rate_2000 = rate + 0.7
        rate_6000 = rate + 0.6

        # Формируем сообщение
        message = (
            f"🇨🇳 Актуальный курс на {today_date}:\n"
            f"От 200¥ - {rate_200:.2f}₽\n"
            f"От 2000¥ - {rate_2000:.2f}₽\n"
            f"От 6000¥ - {rate_6000:.2f}₽"
        )

        logging.info(f"Отправка сообщения: {message} в {CHANNEL_ID}")
        await bot.send_message(CHANNEL_ID, message)
        logging.info("Сообщение успешно отправлено!")
    
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения: {e}")
    
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(send_yuan_rate())
