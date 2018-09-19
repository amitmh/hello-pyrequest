#!/usr/bin/env python3
import requests

DEF_URI='http://docs.python-requests1.org/en/master/api/'

def main():
    headers={'user-agent': 'my-app/0.0.1', 'Accept': 'application/xml'}
    proxies={'http://host.name': 'foo.bar:4012'}

    r = requests.request('GET',
                         DEF_URI,
                         proxies=proxies,
                         headers=headers)

    #print(r.text)
    print(r.status_code)
    print(r.headers)

if __name__ == "__main__":
    main()

        
