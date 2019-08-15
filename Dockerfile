FROM ubuntu:18.04

RUN apt-get update && apt-get install python3 python3-pip git -y

WORKDIR /usr/share/git/flooddamage-tiff-downloader
COPY . .

RUN pip3 install -r requirements.txt
