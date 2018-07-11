FROM fedora:27
EXPOSE 22

RUN dnf -y install openssh-server passwd python && dnf clean all
RUN mkdir /var/run/sshd && \
    echo -e "hunter2\nhunter2" | (passwd --stdin root) && \
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''

ENTRYPOINT ["/usr/sbin/sshd", "-D"]
