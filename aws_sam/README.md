# AWS SAM flaskサンプル

## 開発環境構築手順

1. Serverless Frameworkインストール & 初期化

    ```cmd
    npm install serverless
    npm init -f
    ```

    node_modules/.binに`serverless`,`sls`などのコマンドがインストールされる.

2. 開発用npmプラグインをインストール

    ```cmd
    npm install -D serverless-wsgi serverless-python-requirements
    ```

3. `package.json`の`scripts`にコマンドを追加.

    ```cmd
    "deploy": "sls deploy"
    "remove": "sls remove"
    "serve": "sls wsgi serve"
    ```

4. ローカルへのDeploy

    ```cmd
    npm run serve
    ```

    ```info
    Service Information
    service: serverless-flask
    stage: dev
    region: ap-northeast-1
    stack: serverless-flask-dev
    resources: 12
    api keys:
    None
    functions:
    app: serverless-flask-dev-app
    layers:
    None
    ```

    Lambda, Role, Cloudformation stack, s3 bucket, API Gateway, CloudWatchが作成される.

5. AWSへのDeploy

    ```cmd
    npm run deploy
    ```

## Tips

- ローカルのDockerは不要.
- Lambdaへはrequirements.txtでの必要なライブラリを含めたZipがDeployされる.
  
  _プロジェクトフォルダ下も全て内包されるので注意_

### AWS上のDeploy内容の削除

```cmd
npm run remove
```
