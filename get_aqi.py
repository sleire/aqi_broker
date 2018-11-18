import requests

def get_aqi(location, token_str):
    '''get location aqi from aqicn.org api'''
    url_1 = 'https://api.waqi.info/feed/'
    url_2 = '/?token='
    r = requests.get(url_1 + l + url_2 + tok)
    return r.json()

# api token
with open('token') as t:
    tok = t.readlines()[0]

# list of locations
loc = [line.rstrip('\n') for line in open('locations')]

# get aqi data for all locations
for l in loc:
    aqi = get_aqi(l, tok)
    print(aqi)
    print('\n')