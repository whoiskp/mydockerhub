FROM python:3.6-alpine

RUN apk add --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
    && echo "Asia/Ho_Chi_Minh" > /etc/timezone \
    && rm -rf /tmp/* /var/cache/*

# RUN apk add --no-cache -u ca-certificates libva-intel-driver python3-dev build-base linux-headers pcre-dev vim curl \
#     && rm -rf /tmp/* /var/cache/*

COPY requirements.freeze /
RUN pip --no-cache-dir install -r requirements.freeze

COPY . /mycode

WORKDIR /mycode