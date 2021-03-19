FROM learnk8s/labs-docker:encrypted
RUN mkdir -p /data/folder1
RUN mkdir -p /home/ubuntu/Documents
RUN apt-get update -qq
RUN apt-get install -y openssl
COPY message.txt /home/ubuntu/Documents/message.txt

