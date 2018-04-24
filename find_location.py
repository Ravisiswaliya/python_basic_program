#1 method
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

for d in data:
    print(d,':',data[d])



# 2nd method
import geocoder
loc = geocoder.ip('me')
print(loc.latlng)
