#!/bin/bash
# get aqi data from aqicn.org api

source token
sep="-"

url_1='https://api.waqi.info/feed/'
url_2='/?token='

for i in $(cat locations); do
	file_time=`date +%Y-%m-%d.%H:%M:%S`
	echo $i$sep$file_time
	curl $url_1$i$url_2$token >> data/$i$sep$file_time
done
