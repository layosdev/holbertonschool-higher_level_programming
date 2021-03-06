#!/usr/bin/python3
""" takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) < 2:
        data = ""
    else:
        data = sys.argv[1]

    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': data})
    try:
        dict = req.json()
        if len(dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(dict["id"], dict["name"]))
    except ValueError:
        print("Not a valid JSON")
