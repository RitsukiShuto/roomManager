# Created by RitsukiShuto on 2023/06/04.
# Discordのアクティビティを取得するクラス
#
import discord
import Status

global game
global client

setByDiscordActivity = Status.Status()

class MyClient(discord.Client):
    # 起動時に動作する処理
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        # アクティビティを取得するユーザーを指定
        member = discord.utils.get(self.get_all_members(), name="DoubchBuger")

        # memberがNoneだったらエラーを返す
        if member == None:
            print("member is None.")
            return

        getDiscordActivity(member)

    # メッセージ受信時に動作する処理
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        # メッセージ送信者がBotだった場合は無視する
        if message.author.bot:
            return
        
        # メッセージの内容によって返信する
        if message.content == '/getact':
            member = discord.utils.get(self.get_all_members())
            getDiscordActivity(member)

    # プロフィールが更新されたときに動作する処理
    async def on_member_update(self, before, after):
        getDiscordActivity(after)

    # webサイトからPOSTされたときに動作する処理
    # async def on_post(self, request):
    #     print(request)
    #     getDiscordActivity();


def getDiscordActivity(member):
    print(member)

    if member.activity == None:
        game = ""
        print("None")

    else:
        game = member.activity.name
        setByDiscordActivity.setStatus("対応不可", game)

        # インスタンスへの格納成功
        print("Success to set status. " + setByDiscordActivity.message + " is set.")

        # index.pyに返す
        return setByDiscordActivity

def main():
    # Botのトークンを読み込む
    try:                            # webAppから起動した時
        with open('token/discoToken.txt', 'r') as f:
            TOKEN = f.read()
    
    except FileNotFoundError:       # デバッガから起動した時
        print("Token file is not found.")
        print("open token file by debug mode.")

        with open('app/static/backend/token/discoToken.txt', 'r') as f:
            TOKEN = f.read()

    # Intentsオブジェクトを生成
    intents = discord.Intents.all()

    # クライアントのインスタンスを生成
    client = MyClient(intents=intents)
    client.run(TOKEN)

if __name__ == '__main__':
    main()