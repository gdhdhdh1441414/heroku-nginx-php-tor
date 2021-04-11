FROM php:7.3-apache
RUN apt-get update
RUN apt-get install -y libicu-dev xz-utils git python libgmp-dev unzip ffmpeg tor
COPY misc/tor/torrc /etc/tor/torrc
COPY misc/tor/start-tor.sh misc/tor/start-tor.sh
COPY ./web /var/www/html/
RUN echo "HiddenServicePort 80 127.0.0.1:8080" > /etc/tor/torrc
RUN cat /etc/tor/torrc
RUN service tor start
EXPOSE 8080
ENV CONVERT=1
