import random
import webbrowser
import urllib.request
import pprint
import json

response = urllib.request.urlopen("https://dog.ceo/api/breed/corgi/images/random")

data = json.loads(response.read())

pprint.pprint(data)

url = data["message"]

webbrowser.open(url)
