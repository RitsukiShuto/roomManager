# Created by RitsukiShuto on 2023/06/04.
# Discordのアクティビティを取得するクラス
#
import discord
from discord.ext import commands

import Status       # ステータスクラス


def main():
    # Botのトークンをテキストファイルから読み込む
    with open('./token/discoToken.txt', 'r') as f:
        TOKEN = f.read()

if __name__ == '__main__':
    main()