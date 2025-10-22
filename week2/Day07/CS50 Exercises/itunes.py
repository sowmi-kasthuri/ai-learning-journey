# API interaction using requests package
# https://itunes.apple.com/search?entity=song&limit=1&term=weezer

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
# print(response.json()) # doesnt return in json format
# print(json.dumps(response.json(), indent=2)) # returns in json format

o = response.json()

for result in o["results"]:
    print(result["trackName"])

