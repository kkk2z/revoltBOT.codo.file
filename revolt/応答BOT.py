import revolt
import asyncio
import random
import os
class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        if message.content == "トリガーメッセージ":
            responses = ["メッセージ1", "メッセージ2", "メッセージ3","メッセージ4","メッセージ5"] 
          # 必要に応じて追加
            await message.channel.send(random.choice(responses))
async def main():
    async with revolt.utils.client_session() as session:
        client = Client(session, os.environ['TOKEN'])
        await client.start()
asyncio.run(main())
