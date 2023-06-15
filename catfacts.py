#!/usr/bin/python3

import requests

url= "https://cat-fact.herokuapp.com/facts"

def main():
    resp= requests.get(url).json()
    ## x= resp.jason()
    
    for x in resp:
        print(x)

if __name__ == "__main__":
    main()
