import requests
from requests.auth import HTTPDigestAuth

url='https://sigee.ave-asso.fr/listSales?event=96#mark'
cookie='username=jean.vinnccent%40gmail.com; PHPSESSID=3eakr7iatmsnruc5ps5sdr81n6'
cook = dict(cookies_are=cookie)

r = requests.get(url, cookies=cook)
print(r.text)