# Created by RitsukiShuto on 2023/06/04.
# Discordのアクティビティを取得するクラス
#
import discord
from discord.ext import commands

class MyClient(discord.Client):
    # 起動時に動作する処理
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # メッセージを受信したときに動作する処理
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        # /nekoと発言したら「にゃーん」が返る処理
        if message.content == '/neko':
            print('にゃーん')
            await message.channel.send('にゃーん')


def main():
    # Botのトークンをテキストファイルから読み込む
    with open('app/static/backend/token/discoToken.txt', 'r') as f:
        TOKEN = f.read()

    # Intentsオブジェクトを生成
    intents = discord.Intents.all()

    # クライアントのインスタンスを生成
    client = MyClient(intents=intents)
    client.run(TOKEN)

if __name__ == '__main__':
    main()