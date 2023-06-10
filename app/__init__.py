# Created by RitsukiShuto on 2023/05/26.
# pwd: /home/src/roomManager/app/__init__.py
# ref: https://qiita.com/neomi/items/cdf492d6a0c50310ff87
#
from flask import Flask

app = Flask(__name__)

# index.pyをインポート
from app.main.index import main as main

# blueprintを登録
app.register_blueprint(main)