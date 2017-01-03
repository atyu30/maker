# Version : 0.0.1
# Pull base image.
FROM centos7base:7.3.1611
MAINTAINER Atyu30 "ipostfix@gmail.com"
ENV REFRESHED_AT 2017-01-01

# Clean yum cache and install influxdb
RUN yum -y install http://yum.yuyizhi.com/influxdb-1.1.1.x86_64.rpm && yum clean all

COPY influxdb.conf /etc/influxdb/influxdb.conf

VOLUME /var/lib/influxdb

# Expose ports.
EXPOSE 8083
EXPOSE 8086

