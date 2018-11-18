#!/bin/bash
# get aqi data from aqicn.org api

sep="-"

url_1='https://api.waqi.info/feed/'
url_2='/?token='

for i in $(cat token); do
	token=$i
done

for i in $(cat locations); do
	file_time=`date +%Y-%m-%d.%H:%M:%S`
	curl $url_1$i$url_2$token
done