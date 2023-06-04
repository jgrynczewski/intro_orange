import json
import requests


response = requests.get('https://api.punkapi.com/v2/beers?brewed_before=11-2012&abv_gt=6')
content = response.content

data = json.loads(content)
for item in data:
    print(item)
