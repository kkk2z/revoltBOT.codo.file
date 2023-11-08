import revolt
import asyncio
## となりのこまんど実効しろ　pip install revolt
# Revoltボットのトークンを入力してください
#ダサく
TOKEN = "your_bot_token"

# Revoltクライアントを作成します
client = revolt.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.content.startswith("!ban"):
        # ユーザーをBANします
        if "admin" in [role.name for role in message.author.roles]:
            if message.mentions:
                for user in message.mentions:
                    await client.ban_user(user, message.channel)
            else:
                await message.channel.send("メンションでユーザーを指定してください")
        else:
            await message.channel.send("管理者専用コマンドです")

    elif message.content.startswith("!kick"):
        # ユーザーをキックします
        if "admin" in [role.name for role in message.author.roles]:
            if message.mentions:
                for user in message.mentions:
                    await client.kick_user(user, message.channel)
            else:
                await message.channel.send("メンションでユーザーを指定してください")
        else:
            await message.channel.send("管理者専用コマンドです")
  
    elif message.content.startswith("!timeout"):
        # ユーザーをタイムアウトします
        if "admin" in [role.name for role in message.author.roles]:
            if message.mentions:
                for user in message.mentions:
                    await client.timeout_user(user, message.channel)
            else:
                await message.channel.send("メンションでユーザーを指定してください")
        else:
            await message.channel.send("管理者専用コマンドです")

    elif message.content.startswith("!hello"):
        # BOTからの応答
        await message.channel.send("こんにちは！")
  
    # その他のコマンドやメッセージに対する処理を追加できます

# Revoltに接続します
client.run(TOKEN)
