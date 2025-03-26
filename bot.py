import os
import logging
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Применяем nest_asyncio для корректной работы в средах с уже запущенным event loop
nest_asyncio.apply()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получаем переменные окружения
OWNER_CHAT_ID = "1050963411"  # Ваш Telegram ID
BOT_TOKEN = "8010910977:AAFg48Y8tuz2nM4pDRhFqZs5wI4umM-xlsw"                  # Токен бота

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    username = f"@{user.username}" if user.username else user.first_name
    # Отправляем уведомление владельцу
    await context.bot.send_message(chat_id=OWNER_CHAT_ID, text=f"Новый пользователь: {username}")
    # Отвечаем пользователю
    await update.message.reply_text("")

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # Запускаем polling без await, поскольку run_polling() синхронный
    application.run_polling(close_loop=False)

if __name__ == '__main__':
    main()