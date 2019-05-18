# memo

## 手順

### FrontEndイメージ作成

1. `frontend`ディレクトリ作成
2. `frontend/static`ディレクトリ作成
3. `frontend/templates`ディレクトリ作成
4. `frontend/templates/index.html`ファイル作成

    ```html
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
        <!-- <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.min.js"></script> -->
        <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
        <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
        <script src="/static/js/script.js" defer></script>
        <title></title>
    </head>
    <body>
        <div id="app">
        </div>
    </body>
    </html>
    ```

5. `frontend/static/js`ディレクトリ作成
6. `frontend/static/js/script.js`ファイル作成

    ```js
    var app = new Vue({
        el: '#app',
        data: {
        }
    })
    ```

7. `frontend/static/css`ディレクトリ作成
8. `frontend/static/css/style.css`ファイル作成（空）
9. `frontend/default.conf`ファイル作成

    ```conf
    server {
        listen      80;
        server_name localhost;

        location / {
            root   /app/templates;
            index  index.html index.htm;
        }

        location /static {
            alias /app/static/;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
    }
    ```

10. frontendディレクトリ内に `Dockerfile` 作成

    ```Dockerfile
    FROM nginx:latest

    WORKDIR /app

    COPY ./* ./
    COPY default.conf /etc/nginx/conf.d
    ```

### BackEndイメージ作成

1. `cd {プロジェクトルート}`
2. `mkdir backend`
3. backendディレクトリ内にflask起動スクリプト `main.py` 作成

   ```python
   #!/usr/bin/env python
   # -*- coding: utf-8 -*-

   from flask import Flask, jsonify

   app = Flask(__name__)


   @app.route("/api")
   def api():
       return jsonify({'key': 'value'})


   if __name__ == "__main__":
       app.run()
   ```

4. backendディレクトリ内に `requirements.txt` 作成

   ```text
   Flask
   uwsgi
   ```

5. backendディレクトリ内に `uwsgi.ini` 作成

   ```ini
   [uwsgi]
   wsgi-file = main.py
   callable = app
   master = true
   processes = 1
   http = :3031
   chmod-socket = 666
   vacuum = true
   die-on-term = true
   py-autoreload = 1
   ```

7. backendディレクトリ内に `Dockerfile` 作成

   ```Dockerfile
   FROM python:3.6

   WORKDIR /app

   COPY ./* ./

   RUN pip install --no-cache-dir -r requirements.txt

   CMD ["uwsgi","--ini","/app/uwsgi.ini"]
   ```

### docker-compose

1. プロジェクトルート直下に `docker-compose.yml` 作成

    ```docker-compose
    version: '3'
    services:
      db:
        image: postgres
        ports:
          - "5432:5432"
      uwsgi:
        build: ./backend
        volumes:
          - ./backend:/app
        ports:
          - "3031:3031"
        environment:
          TZ: "Asia/Tokyo"
      nginx:
        build: ./frontend
        volumes:
          - ./frontend:/app
          - ./frontend/default.conf:/etc/nginx/conf.d/default.conf
        ports:
          - "8080:80"
    ```

2. `docker-compose build`