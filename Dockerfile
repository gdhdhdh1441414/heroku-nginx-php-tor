FROM php:7.3-apache
ENV LANG C.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL C.UTF-8
RUN echo "C.UTF-8 UTF-8" > /etc/locale.gen

RUN apt-get update
RUN apt-get install -y libicu-dev xz-utils git python python3 libgmp-dev unzip ffmpeg tor zip aria2 mediainfo
COPY misc/tor/torrc /etc/tor/torrc
COPY misc/tor/start-tor.sh misc/tor/start-tor.sh
COPY start.sh /start.sh
COPY ./web /var/www/html/
RUN service tor start
RUN cp /var/lib/tor/hidden_service/hostname /var/www/html/domain.txt

EXPOSE 80
ENV CONVERT=1
CMD service tor start
