#!/bin/bash
# get aqi data from aqicn.org api

source token

url_1='https://api.waqi.info/feed/'
url_2='/?token='

for i in $(cat locations); do
	#file_time=`date +%Y-%m-%d.%H:%M:%S`
	#filename= $i$file_time
	#echo $file_time
	curl $url_1$i$url_2$token
done
