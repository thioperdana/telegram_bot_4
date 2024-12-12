from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from dotenv import dotenv_values

from pprint import pprint

env = dotenv_values(".env")
bot_token = env.get("BOT_TOKEN")


async def start_func(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"User mengirim pesan: {update.message.text}")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello, {update.effective_user.full_name}"
    )


async def sum_list_func(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"User mengirim pesan: {update.message.text}")

    data_str = update.message.text.split()[1]
    data = eval(data_str)
    result = sum(data)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hasil penjumlahan {data} adalah {result}"
    )

async def echo_func(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"User mengirim pesan: {update.message.text}")

    pprint(update.to_dict())
    print(f"Tanggal mengirim pesan: {update.message.date}")

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.message.text}"
    )

if __name__ == "__main__":
    #membuat objek aplikasi
    app = Application.builder().token(bot_token).build()
    
    start_handler = CommandHandler('start', start_func)
    app.add_handler(start_handler)

    echo_handler = CommandHandler('echo', echo_func)
    app.add_handler(echo_handler)

    sum_list_handler = CommandHandler('sum_list', sum_list_func)
    app.add_handler(sum_list_handler)

    print("aplikasi berjalan")
    app.run_polling()
