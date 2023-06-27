FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# 容器内创建 app 文件夹
ENV APP_HOME=/app

RUN mkdir -p $APP_HOME && mkdir -p /app/models && /app/logs

WORKDIR $APP_HOME

# COPY pip.conf /root/.pip/pip.conf

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 将当前目录加入到工作目录中 (. 表示当前目录)
COPY . ${APP_HOME}

RUN sed -i 's/\r//' start.sh && \
    chmod +x start.sh

# 启动
ENTRYPOINT [ "/bin/bash", "start.sh" ]