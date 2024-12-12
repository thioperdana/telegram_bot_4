from telethon import TelegramClient, events
from src.utils.main_logger import logger_general, logger_error
from src.llm_process import ask_ai

from dotenv import dotenv_values

env = dotenv_values(".env")

bot = TelegramClient(
    f"{env['PROJECT_PATH']}/session/testing_bot",
    env["API_ID"], 
    env["API_HASH"]
).start(
    bot_token=env['BOT_TOKEN']
)

@bot.on(events.NewMessage())
async def logger(event):
    message_dict = event.message.to_dict()
    data = {
        "id_pesan" : message_dict['id'],
        "user_id" : message_dict['peer_id']['user_id'],
        "waktu" : message_dict['date']     
    }
    logger_general.debug(f"{data}")

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    "pesan yang dikirimkan saat memulai"
    await event.respond("Selamat datang di bot ini!")

@bot.on(events.NewMessage(pattern='/hitung'))
async def start(event):
    "pesan yang dikirimkan saat memulai"
    data = event.text.split()[1]
    result = eval(data)
    result = sum(result)

    await event.respond(f"Hasil dari penjumlahan {data} adalah {result}")

@bot.on(events.NewMessage(pattern='#tanyapython'))
async def tanya_python(event):
    "pertanyaan terhadap model llama 3.1"
    data = " ".join(event.text.split()[1:])
    logger_general.debug(f"pertanyaan yang dikirim : {data}")
    logger_general.info("memulai fungsi ask_ai")
    answers = ask_ai(data)
    logger_general.debug(f"jawaban dari ai adalah :{answers}")
    await event.respond(answers)


def run():
    "start bot.."
    print("bot telah berjalan")
    bot.run_until_disconnected()