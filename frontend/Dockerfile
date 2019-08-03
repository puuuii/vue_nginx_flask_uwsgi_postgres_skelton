FROM nginx:latest

WORKDIR /app

COPY ./* ./
COPY default.conf /etc/nginx/conf.d

RUN cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime &&\
    apt update && apt install curl -y && apt install cron -y &&\
    curl https://dl.eff.org/certbot-auto -o /usr/bin/certbot &&\
    chmod 700 /usr/bin/certbot &&\
    echo "50 3 * * 0 /usr/bin/certbot renew --post-hook \"service nginx restart\"" >> /etc/cron.d/renew_certbot