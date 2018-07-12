FROM ubuntu:16.04
EXPOSE 22

RUN apt-get update && apt-get install -y openssh-server python
RUN mkdir /var/run/sshd && \
    echo 'root:hunter2' | chpasswd && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

ENTRYPOINT ["/usr/sbin/sshd", "-D"]
