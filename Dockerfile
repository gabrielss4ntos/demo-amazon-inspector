FROM alpine:latest

# Instala as bibliotecas vulneráveis
RUN apk add --no-cache \
    httpd \
    openssh-client \
    php7-common \
    php7-cli \
    php7-cgi \
    php7-curl \
    php7-json \
    php7-mbstring \
    php7-openssl@1.1.1k-r3 \
    php7-pdo \
    php7-phar \
    php7-xml \
    mysql-client@8.0.29-r0 \
    java-openjdk@17.0.3-r0 \
    nodejs@16.13.0-r0
