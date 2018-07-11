FROM centos:7
EXPOSE 22

RUN yum -y install openssh-server passwd; yum clean all
RUN mkdir /var/run/sshd && \
    echo -e "hunter2\nhunter2" | (passwd root) && \
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''

ENTRYPOINT ["/usr/sbin/sshd", "-D"]
