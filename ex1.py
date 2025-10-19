import requests
url = 'https://cloudflare-dns.com/dns-query'
params = {
     'name': 'fmi.unibuc.ro',
     'type': 'A',
     'ct': 'application/dns-json',
 }
ae = requests.get(url, params=params)
from pprint import pprint
pprint(ae.json())
