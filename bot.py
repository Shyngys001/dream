import logging
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Применяем nest_asyncio, если цикл событий уже запущен (например, в Jupyter)
nest_asyncio.apply()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

OWNER_CHAT_ID = 1050963411  # Ваш Telegram ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    username = f"@{user.username}" if user.username else user.first_name
    # Отправляем уведомление владельцу
    await context.bot.send_message(chat_id=OWNER_CHAT_ID, text=f"Новый пользователь: {username}")
    # Отвечаем пользователю
    await update.message.reply_text("Привет! Спасибо за запуск бота.")

async def main():
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    application = ApplicationBuilder().token("8010910977:AAFg48Y8tuz2nM4pDRhFqZs5wI4umM-xlsw").build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())