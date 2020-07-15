FROM amazonlinux:2

# RUN yum --enablerepo=amzn2-core clean metadata
RUN yum -y update
# Pythonはインストールされるバージョンに注意
RUN yum -y install python3
# RUN yum -y install python3 make zip unzip yarn gcc

# gcc-c++ zip gzip wget bzip2-devel git
# RUN yum install gcc openssl-devel bzip2-devel libffi-devel

# HASHエラーが起きる場合は先にダウンロードしたwhlをインストール
# RUN pip3 install botocore-1.17.20-py2.py3-none-any.whl
# RUN pip3 install boto3 werkzeug flask

# awscliはCloudFormation実行に必要
# RUN cd /opt
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN ./aws/install

RUN curl -sL https://rpm.nodesource.com/setup_14.x | bash -
RUN yum -y install nodejs
# RUN go get github.com/aws/aws-lambda-go/...
# RUN go get github.com/aws/aws-sdk-go/aws/...
# RUN go get github.com/sirupsen/logrus

# ENV PATH "$PATH:/root/go/bin"
