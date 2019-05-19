FROM nginx:latest

WORKDIR /app

COPY ./* ./
COPY default.conf /etc/nginx/conf.d

RUN cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime