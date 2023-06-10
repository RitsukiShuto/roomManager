# Created by RitsukiShuto on 2023/06/04.
# Discordのアクティビティを取得するクラス
#
import discord

# Botのトークンをテキストファイルから読み込む
with open('app/static/backend/token/discoToken.txt', 'r') as f:
    TOKEN = f.read()
    
client = discord.Client()
client.run(TOKEN)


# 起動時に動作する処理
@client.event
async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

    # アクティビティを取得するユーザーを指定
    member = discord.utils.get(self.get_all_members(), name="DoubchBuger")

    # memberがNoneだったらエラーを返す
    if member == None:
        print("member is None.")
        return

    game = getDiscordActivity(member)

    return game

# メッセージ受信時に動作する処理
@client.event
async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
        
    # メッセージの内容によって返信する
    if message.content == '/getact':
        member = discord.utils.get(self.get_all_members())
        game = getDiscordActivity(member)

    return game

def getDiscordActivity(member):
    print(member)

    if member.activity == None:
        game = ""
        print("None")

    else:
        print(member.activity.name)
        game = member.activity.name