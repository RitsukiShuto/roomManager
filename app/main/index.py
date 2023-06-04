# Created by RitsukiShuto on 2023/05/26.
# pwd: /home/src/roomManager/app/main/index.py
# ref: https://qiita.com/neomi/items/cdf492d6a0c50310ff87
#
from flask import Blueprint, render_template, request
from app.static.backend.Status import Status

main = Blueprint('main', __name__, url_prefix='/')

# ルートディレクトリにアクセスしたときの処理
@main.route('/main')

# index.htmlを参照してtestDataをテンプレートのhtmlDataに設定して表示する
def index():
    nowStatus = Status()

    return render_template('/main/index.html', message=nowStatus.message, status=nowStatus.status)

# フォームのデータを受け取る
@main.route('/main', methods=['POST'])
def post():
    # フォームのデータをセットしてページを更新
    nowStatus = Status()

    # 受け取ったデータをコンソールに表示
    print(request.form['status'])
    print(request.form['message'])

    # 受け取ったデータをセット
    nowStatus.setStatus(request.form['status'], request.form['message'])

    return render_template('/main/index.html', message=nowStatus.message, status=nowStatus.status)