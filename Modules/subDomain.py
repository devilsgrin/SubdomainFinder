import requests
import urllib.request as ureq
import sys
import os
from requests.exceptions import HTTPError

class SubFinder:
    def __init__(self):
        self.target = input("Target: ")
        self.wordlist = input("Wordlist: " + "../" )

    def startSearch(self):
        wordlist_data=[]

        with open(self.wordlist, 'r') as file:
            for line in file:
                wordlist_data.append(line.rstrip())

        self.renameDomain(wordlist_data)
    def renameDomain(self,data):
        subdomains = []
        while data:
            a = self.target.replace("www",data[0])
            subdomains.append(a)
            data.pop(0)

        self.checkSub(subdomains)
    def checkSub(self,subs):
        while subs:
            try:
                response = requests.get(subs[0])
                response.raise_for_status()

            except HTTPError as http_err:
                #print(f'[-]HTTP error occurred: {http_err}')
                pass
            except Exception as err:
                #print(f'[-]Other error occurred: {err}')
                pass
            else:
                print('\033[92m [+] Success for: ' + subs[0])

            subs.pop(0)

    def CheckConnection(self, host="https://www.google.com"):
        try:
            ureq.urlopen(host)
            return True
        except:
            print("Connection has lost")





