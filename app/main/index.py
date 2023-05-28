# Created by RitsukiShuto on 2023/05/26.
# pwd: /home/src/roomManager/app/main/index.py
# ref: https://qiita.com/neomi/items/cdf492d6a0c50310ff87
#
from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix='/')

# ルートディレクトリにアクセスしたときの処理
@main.route('/main')

# index.htmlを参照してtestDataをテンプレートのhtmlDataに設定して表示する
def index():
    status = '作業中'
    displaying_message = 'Hello World'

    return render_template('/main/index.html', displaying_message=displaying_message, status=status)