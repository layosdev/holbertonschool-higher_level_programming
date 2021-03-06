#!/usr/bin/python3
"""takes your Github credentials (username and password)
   and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    try:
        print(req.json().get('id'))
    except:
        pass
