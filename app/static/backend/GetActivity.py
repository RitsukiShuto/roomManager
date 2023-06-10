# GetByDiscordActivityからのデータを受け取る
# ここで受け取ったデータをテンプレートに渡す

from app.static.backend.GetByDiscordActivity import MyClient, runGetActivity
import discord

def callGetActivity():
    # Intentsオブジェクトを生成
    intents = discord.Intents.all()

    # クライアントのインスタンスを生成
    client = MyClient(intents=intents)

    runGetActivity(client)


callGetActivity()