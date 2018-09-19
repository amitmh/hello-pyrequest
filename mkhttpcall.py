#!/usr/bin/env python3
import requests
import sys

DEF_URI = 'http://docs.python-requests.org/en/master/api/'
DEF_OUT = 'target/out'


def main():
    headers = {'user-agent': 'my-app/0.0.1', 'Accept': 'application/xml'}
    proxies = {'http://host.name': 'foo.bar:4012'}

    r = requests.get(DEF_URI, proxies=proxies, headers=headers)

    print(r.status_code)

    with open('%s.txt' % DEF_OUT, 'a') as response_file:
        response_file.write(r.text)

    with open('%s.headers' % DEF_OUT, 'a') as response_file:
        response_file.write(str(r.headers))


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        # raise
        sys.exit(ex)
