from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Start komandasini ishlatganda javob beradigan funksiya
async def start(update: Update, context):
    await update.message.reply_text("Salom! Qalay, hol-ahvolingiz yaxshimi?")

# Foydalanuvchi "yaxshi" deb javob berganda
async def reply_good(update: Update, context):
    await update.message.reply_text("Yaxshi bo'lganidan xursandman!")

# Foydalanuvchi boshqa narsa yozganda
async def handle_message(update: Update, context):
    await update.message.reply_text("Sizning javobingizni tushunmadim. Iltimos, 'yaxshi' deb yozing.")

if __name__ == '__main__':
    app = ApplicationBuilder().token('7838036969:AAE_M_i3nFBcqWcKIyvKfkF4adyItGkk9Ic').build()

    # /start komandasini qayta ishlash
    app.add_handler(CommandHandler("start", start))

    # Foydalanuvchining "yaxshi" javobini qayta ishlash
    app.add_handler(MessageHandler(filters.Text(['yaxshi', 'Yaxshi']), reply_good))

    # Har qanday boshqa xabarni qayta ishlash
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()
