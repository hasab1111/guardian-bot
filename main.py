from pyrogram import Client

import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

app = Client(
    "guardian",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message()
async def alive(client, message):
    await message.reply("🤖 البوت شغال")

app.run()
