from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8749060005:AAGdt5DBA1eYztDvD8rx_ZnJgnem4i0KvAs"

ADMIN_ID = 8517633098

users = {}

keyboard = ReplyKeyboardMarkup(
    [["🛍 UC sotib olmoqchiman"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Keling sizga qancha UC kerak?\nPastdagi tugmani bosing 👇",
        reply_markup=keyboard
    )

async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if text == "🛍 UC sotib olmoqchiman":
        users[user_id] = {}
        await update.message.reply_text(
"""Iltimos qancha UC kerak bo‘lsa menga jo‘nating

📣📣📣📣📣📣📣📣📣📣📣📣
🛍 @ucrecon_bot AKSIYALAR
📣📣📣📣📣📣📣📣📣📣📣📣

👇👇👇👇👇👇👇👇👇👇
GLOBAL PUBG 🌎

🛍30 UC - 9.000 ⚡️
🛍60 UC - 13.000 ⚡️
🛍90 UC - 22.000 ⚡️
🛍120 UC - 26.000 ⚡️
🛍150 UC - 35.000 ⚡️
🛍180 UC - 39.000 ⚡️ID🪪
🛍210 UC - 48.000 ⚡️
🛍325 UC - 61.000 ⚡️
🛍385 UC - 73.000 ⚡️RP 💎
🛍660 UC - 123.000 ⚡️
🛍720 UC - 135.000 ⚡️RP💎
🛍780 UC - 149.000 ⚡️
🛍985UC - 185.000 ⚡️
🛍1045 UC - 197.000 ⚡️
🛍1320 UC - 245.000 ⚡️
🛍1800 UC - 300.000 ⚡️
🛍2125 UC - 360.000 ⚡️RP+💎
🛍2460 UC - 423.000 ⚡️
🛍3850 UC - 585.000 ⚡️
🛍4175 UC - 644.000 ⚡️
🛍4510 UC - 707.000 ⚡️
🛍5170 UC - 825.000 ⚡️
🛍5650 UC - 888.000 ⚡️
🛍8100 UC - 1.170.000 ⚡️
🛍9900 UC - 1.450.000 ⚡️
🛍24300 UC - 3.450.000 ⚡️

💳 TO'LOV HUMO VA VISA KARTALARIDA:

💳 HUMO:
9860160602662159
Mamirov L.

💳 VISA:
4231200092776151
Mamirov L.

🛍️ Manager: @recon_ae 🏪
📃 TO'LOV HAQIDA CHEK SHART (screenshot) ❌
❌ Feyklarga aldanib qolmang! ❌

🛍 ENG ARZON ISHONCHLI VA TEZKOR
⚡️⚡️⚡️ @ucrecon_bot ⚡️⚡️⚡️"""
        )
        return

    if user_id in users and "uc" not in users[user_id]:
        users[user_id]["uc"] = text
        await update.message.reply_text(
            "Iltimos PUBG ID raqamingizni yozing"
        )
        return

    if user_id in users and "id" not in users[user_id]:
        users[user_id]["id"] = text
        await update.message.reply_text(
            "Iltimos to‘lov chekini ham jo‘nating"
        )
        return

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_id in users:
        photo = update.message.photo[-1].file_id

        uc = users[user_id]["uc"]
        pubg_id = users[user_id]["id"]

        caption = f"""
🛒 YANGI BUYURTMA

👤 User: @{update.message.from_user.username}

💎 UC: {uc}

🆔 PUBG ID: {pubg_id}
"""

        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=photo,
            caption=caption
        )

        await update.message.reply_text(
            "✅ Buyurtmangiz adminga yuborildi"
        )

        del users[user_id]

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, photo))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messages))

print("Bot ishga tushdi...")
app.run_polling()