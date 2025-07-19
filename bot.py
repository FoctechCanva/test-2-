import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("8031287037:AAHvhktR7r2SwQn7GJuQRVrLIS759eLf6ao")

join_links = [
    "https://t.me/+ubKdvq2fjv1lM2Q1",
    "https://t.me/+ubKdvq2fjv1lM2Q1",
    "https://t.me/+ubKdvq2fjv1lM2Q1",
    "https://t.me/+ubKdvq2fjv1lM2Q1",
    "https://t.me/+ubKdvq2fjv1lM2Q1",
    "https://t.me/+ubKdvq2fjv1lM2Q1",
]
claim_link = "https://t.me/claim_channel"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Join ❣️", url=join_links[0])],
        [InlineKeyboardButton("Join ❣️", url=join_links[1])],
        [InlineKeyboardButton("Join ❣️", url=join_links[2])],
        [InlineKeyboardButton("Join ❣️", url=join_links[3])],
        [InlineKeyboardButton("Join ❣️", url=join_links[4])],
        [InlineKeyboardButton("Join ❣️", url=join_links[5])],
        [InlineKeyboardButton("✅ Claim", url=claim_link)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = "🎁 Claim Fast Very Limited!!\n\nYono-777 BIG PromoCode Claim Fastt All Users 😱😱\n❤️ Join All Channels Claim Fastt 👇"
    with open("image.jpg", "rb") as photo:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo, caption=caption, reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
