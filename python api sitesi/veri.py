import requests
import json

r = requests.get("http://127.0.0.1:5000/")
data = json.loads(r.text)
espri = data['all'][1]['espri']
print(espri)