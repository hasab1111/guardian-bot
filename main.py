from pyrogram import Client
from flask import Flask
import threading
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

bot = Client(
    "guardian",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=8000)

def run_bot():
    bot.run()

threading.Thread(target=run_web).start()
run_bot()
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

threading.Thread(target=run_flask).start()
