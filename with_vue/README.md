# Vue.js + flaskサンプル

## 開発環境構築手順

1. flask用のフレームワーク/ライブラリをインストール

    ```cmd
    pip install flask_restful flask-bootstrap
    conda install flask-sqlalchemy flask-login flask-wtf flask-cors
    ```

2. Vue-cliをグローバルにインストール

    ```cmd
    npm install -g @vue/cli
    npm install -g @vue/cli-init
    ```

3. プロジェクトで使用するVue.jsパッケージをローカルにインストール

    ```cmd
    npm install axios json-server
    npm install -D webpack webpack-cli
    npm install -D eslint prettier
    ```

4. Vue.jsプロジェクトの作成

    ```cmd
    vue init webpack front
    ```

## Tips

### json-server(フロントエンド開発用のモックのサーバ)

- `package.json`の`"scripts"`に以下を追記して、`npm run json-mock`で実行

  ```json
  "json-mock": "npx json-server --watch test/db.json --routes test/routes.json"
  ```

## 参考

- [FlaskとVue.jsでSPA Webアプリ開発](https://qiita.com/y-tsutsu/items/67f71fc8430a199a3efd)
- [Vue.jsとFlaskでフルスタックなWebアプリの開発環境を構築 その１〜〜環境構築〜〜](https://kittagon.hateblo.jp/entry/2018/08/27/011354)

