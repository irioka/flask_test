# AWS SAM flask サンプル

## 開発環境構築

1. npmパッケージインストール

   ```powershell
   npm install
   ```

   - スクラッチからの作成方法.
      - Serverless Framework インストール & 初期化

         ```powershell
         npm install serverless
         npm init -f
         ```

         node_modules/.bin に`serverless`などのコマンドがインストールされる.

      - 開発用 npm プラグインをインストール

         ```powershell
         npm install -D serverless-wsgi serverless-python-requirements serverless-offline-python
         npm install -D serverless-dynamodb-local
         ```

      - `package.json`の`scripts`にコマンドを追加.

         ```json
         "serve": "serverless wsgi serve"
         "db_install": "serverless dynamodb install",
         "db_start": "serverless dynamodb start"
         "deploy": "serverless deploy"
         "package": "serverless package"
         "remove": "serverless remove"
         ```

2. ローカルでの実行

   - DynamoDB初期化&実行

      ```powershell
      npm run db_install
      npm run db_start
      ```

      - 実行にはJavaが必要.

   - Serverless実行&Debug

      ```powershell
      npm run serve
      ```

      - DynamoDBとServerlessは別々のコンソールで実行.
      - Debugの構成で`Python: Attach using Process Id`を作成し、上記のプロセスにAttachするとBreakpointが使えるようになる.

   - POST/GETのテスト

      ```powershell
      curl -H "Content-Type: application/json" -X POST http://localhost:5000/users -d '{"userId": "alexdebrie1", "name": "Alex DeBrie"}'
      ```

      ```powershell
      curl -H "Content-Type: application/json" -X GET http://localhost:5000/users/alexdebrie1
      ```

3. PackagingとAWS への Deploy

   ```powershell
   npm run package
   ```

   ```powershell
   npm run deploy
   ```

   Lambda, Role, Cloudformation stack, s3 bucket, API Gateway, CloudWatch が作成される.

   - AWS 上の Deploy 内容の削除

      ```cmd
      npm run remove
      ```

## Tips

### WSL

- Ubuntu 20.04LTS

```bash
sudo apt install make unzip
```

```bash
cd /tmp
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

```bash
cd /tmp
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
command -v nvm
nvm install --lts
```

homeディレクトリの.aws/configure,credentialsを設定.Permissionに注意.

### Dockerコンテナ利用方法

_ATTENTION: npmパッケージがWindowsと食い違うなどでErrorとなる._

- Windows で docker-machine 作成(マシン名や各サイズは任意)

   ```powershell
   docker-machine create --virtualbox-cpu-count 2 --virtualbox-disk-size 20000 --virtualbox-memory 4096 default
   ```

   _ATTENTION: Docker Toolbox(VirtualBox) の場合はソースコードのあるドライブを共有フォルダへマウントする._

- VSCodeでdockerコンテナを操作するために以下の環境変数をセットする
  - COMPOSE_CONVERT_WINDOWS_PATHS=true
  - DOCKER_CERT_PATH=%USERPROFILE%\.docker\machine\machines\default
  - DOCKER_HOST=tcp://{docker-machine の IP}:2376
  - DOCKER_TLS_VERIFY=1

### Dockerマシンとコンテナの起動

```powershell
docker-machine start default

docker-machine env --shell powershell default

& "C:\Program Files\Docker Toolbox\docker-machine.exe" env --shell powershell default | Invoke-Expression

docker-compose -f docker-compose.yml up -d --build
```

- DockerマシンへのAttach Shell

   VSCodeのDockerパネルで起動したコンテナを右クリックして、`Attach Shell`するとターミナルが開く.
