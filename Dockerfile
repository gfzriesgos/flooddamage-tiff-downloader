FROM ubuntu:18.04

RUN apt-get update && apt-get install python3 python3-pip git -y

RUN mkdir /usr/share/git && \
    cd /usr/share/git && \
    git clone https://github.com/gfzriesgos/flooddamage-tiff-downloader.git && \
    cd flooddamage-tiff-downloader && \
    git checkout dockerhub && \
    pip3 install -r requirements.txt
