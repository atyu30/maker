#!/bin/bash 
docker run -d \
    -p 8083:8083 -p 8086:8086 \
    -v /opt/influxd:/var/lib/influxdb \
    influxdb-server:v1 influxd
