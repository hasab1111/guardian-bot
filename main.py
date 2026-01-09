from pyrogram import Client, filters
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

app = Client(
    "guardian",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("🤖 البوت شغال 24/7")

print("Bot started")

app.run()
