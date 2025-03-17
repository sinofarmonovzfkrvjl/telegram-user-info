from fastapi import FastAPI
from telethon.sync import TelegramClient

app = FastAPI(
    title="Telegram User Info",
    description="Get Telegram User Info",
    version="0.0.1",
    docs_url='/',
    redoc_url='/docs'
)

async def get_user_info(username):
    api_id = 21137581
    api_hash = "b5aaa153030af4280e4e658619830d75"
    client = TelegramClient("bot_session", api_id, api_hash)
    await client.start(bot_token="8106975001:AAEhrChQRTTo2Z5t96fIRFd23GxNEhHvZjE")

    user = await client.get_entity(username)

    user_info = {
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_bot": user.bot,
        "status": str(user.status),
    }

    await client.disconnect()
    return user_info

@app.get("/{username}")
async def root(username):
    return await get_user_info(username)
