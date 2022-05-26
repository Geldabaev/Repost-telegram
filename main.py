from telethon import TelegramClient, events
import asyncio

api_id = 12345678
api_hash = 'your api hash telgram ac.'


my_channel_id = 'grab_test' # твой канал
channels = ['posts_grab', 'aiogram_ru'] # каналы откуда нужно постить

client = TelegramClient('myGrab', api_id, api_hash)
print("GRAB - Started")


@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message)


client.start()
client.run_until_disconnected()