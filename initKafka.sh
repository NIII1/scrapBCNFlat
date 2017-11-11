#!/bin/sh

#Start zookeeper:
/usr/local/zookeeper/bin/zkServer.sh start
#Start kafka:
/usr/local/kafka/bin/kafka-server-start.sh -daemon /usr/local/kafka/config/zookeeper.properties
