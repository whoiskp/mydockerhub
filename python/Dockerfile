FROM python:3.6-alpine

RUN apk add --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
    && echo "Asia/Ho_Chi_Minh" > /etc/timezone

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

ENV INSTALL_PATH /mycode
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY requirements.freeze .
RUN pip --no-cache-dir install -r requirements.freeze

RUN apk del build-deps \
    && rm -rf /tmp/* /var/cache/*