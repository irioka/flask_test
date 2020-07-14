# AWS SAM flask サンプル

## 開発環境構築手順

1. WSL を使用する

   - Ubuntu 20.04.LTS
     - Daito 等の環境と分けるため
   - anaconda
     - Python は 3.7 に(Lambda は 3.8 でも OK). `conda install python==3.7.6`
   - awscli
   - npm
   - conda install boto3

2. Serverless Framework インストール & 初期化

   ```cmd
   npm install serverless
   npm init -f
   ```

   node_modules/.bin に`serverless`,`sls`などのコマンドがインストールされる.

3. 開発用 npm プラグインをインストール

   ```cmd
   npm install -D serverless-wsgi serverless-python-requirements
   npm install -D serverless-dynamodb-local
   ```

4. `package.json`の`scripts`にコマンドを追加.

   ```cmd
   "deploy": "sls deploy"
   "remove": "sls remove"
   "serve": "sls wsgi serve"
   ```

5. ローカルへの Deploy

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

   Lambda, Role, Cloudformation stack, s3 bucket, API Gateway, CloudWatch が作成される.

6. AWS への Deploy

   ```cmd
   npm run deploy
   ```

   wsl のホームディレクトリの.aws に config と credentials の設定が必要

## Tips

- ローカルの Docker は不要.
- Lambda へは requirements.txt での必要なライブラリを含めた Zip が Deploy される.

  _プロジェクトフォルダ下も全て内包されるので注意_

### AWS 上の Deploy 内容の削除

```cmd
npm run remove
```
