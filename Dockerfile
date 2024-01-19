FROM debian:latest

# Update
RUN DEBIAN_FRONTEND=noninteractive apt-get update || true

# Install build dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --fix-missing \
    apt-utils \
    autoconf \
    automake \
    bind9-host \
    build-essential \
    dh-autoreconf \
    cpanminus \
    curl \
    devscripts \
    exuberant-ctags \
    git-core \
    jq \
    llvm \
    libgeoip1 \
    libgeoip-dev \
    libpcre3 \
    libpcre3-dbg \
    libpcre3-dev \
    libperl-dev \
    libmagic-dev \
    libtool \
    lsof \
    make \
    mercurial \
    ngrep \
    procps \
    python3 \
    telnet \
    tcpflow \
    valgrind \
    vim \
    wget \
    zlib1g \
    zlib1g-dev
