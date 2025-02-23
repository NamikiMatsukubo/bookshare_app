# ベースイメージとしてPython 3.xを使用
# FROM python:3.9-slim

# 作業ディレクトリを設定
# WORKDIR /app

# 必要なパッケージをインストール
# RUN apt-get update && apt-get install -y \
#     python3-pip \
#     && apt-get clean

# 依存関係をコピーしてインストール
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコンテナにコピー
# COPY . /app/

# ポート8000を開放
# EXPOSE 8000

# コンテナが実行される際のデフォルトコマンド
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /book_share_app

COPY requirements.txt /book_share_app/

RUN pip install -r requirements.txt

COPY . /book_share_app/

