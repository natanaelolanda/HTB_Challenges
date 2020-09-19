import requests
import hashlib
import re

req = requests.session()
url = "http://docker.hackthebox.eu:32369/"

html = req.get(url).text
pattern = r"\w{20}"
text = re.findall(pattern, html)[0]

md5Hash = hashlib.md5(text.encode('utf-8')).hexdigest()
r = req.post(url, data = {'hash': md5Hash})
print(r.text)
