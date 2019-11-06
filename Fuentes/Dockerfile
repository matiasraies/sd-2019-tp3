# Docker file for python simple webservice build

FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y install apache2

# Python2.7
RUN apt-get -y install python2.7
RUN apt-get -y install vim
RUN apt-get -y install python-pip

# Http settings
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

RUN mkdir -p /production/www/chat/cgi-bin
RUN mkdir -p /production/www/chat/public_html

RUN mkdir -p /production/www/alumnos/cgi-bin
RUN mkdir -p /production/www/alumnos/public_html

COPY apache2 /etc/apache2
RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/cgi.load
RUN apt-get -qq update && \
    apt-get -qq install -y python3 && \
    apt-get -qq clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
EXPOSE 80

ENTRYPOINT [ "/usr/sbin/apache2" ]
CMD ["-D", "FOREGROUND"]
