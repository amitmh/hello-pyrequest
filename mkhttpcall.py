#!/usr/bin/env python3
import requests

headers = {'user-agent': 'my-app/0.0.1', 'Accept': 'application/xml'}
proxies = {'http://host.name': 'foo.bar:4012'}

r = requests.request('GET',
                     'http://docs.python-requests.org/en/master/api/',
                     allow_redirects=False,
                     proxies=proxies,
                     headers=headers)

print(r.text)
print(r.status_code)
print(r.headers)
