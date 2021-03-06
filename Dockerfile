FROM ubuntu:latest
WORKDIR /home/usr
COPY ./ ./
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/usr"
RUN mkdir -p /dev/net
RUN apt update && apt install openvpn build-essential net-tools netcat w3m python3 mysql-common python-pymysql default-mysql-server default-mysql-client vim python3-pip -y 
#RUN mknod /dev/net/tun c 10 200
#RUN chmod 600 /dev/net/tun
RUN pip3 install pymysql requests
#CMD ["/bin/bash"]
EXPOSE 80
EXPOSE 443
EXPOSE 8080
EXPOSE 22
ENTRYPOINT service mysql restart && (./dbinit.sh; bash)
