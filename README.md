# Raspberry Piによる在室管理システム
### Created by RitsukiShuto on 2023/05/25.

# OSバージョン
```
Linux raspberrypi 5.10.103-v8+ #1529 SMP PREEMPT Tue Mar 8 12:26:46 GMT 2022 aarch64 GNU/Linux
```

# 1.環境構築
## 事前準備
パッケージインデックスのダウンロードとアップデート
``` bash
sudo apt-get update
```
```
sudo apt-get upgrade
```

pythonのインストール
```
sudo apt-get install python-dev python3-dev python-pip python3-pip
```
Flaskのインストール
```
pip3 install flask
```

## 開発環境バージョン
```
Python 3.7.3
Flask  1.0.2
```

# ディレクトリの構成
```
roomManager
└─app
   ├─main
   │  └─index.py
   ├─static
   │  └─css
   │      └─style.css
   ├─templates
   │  └─main
   │      └─index.html
   └─run.py
```

# 2.ディレクトリの中身
## app/main/index.py
index.pyはアプリケーションのメイン画面を表示するためのファイル。

## app/static/css/style.css
style.cssはアプリケーションのスタイルシートを定義するためのファイル。

## app/templates/main/index.html
index.htmlはアプリケーションのメイン画面を表示するためのファイル。

## app/run.py
run.pyはアプリケーションを起動するためのファイル。