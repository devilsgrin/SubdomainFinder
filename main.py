import sys
import os
import argparse
import Modules.subDomain as sub
from time import sleep
from bs4 import BeautifulSoup

def banner():
    banner = """
  ___   __    __        __   _   _____           _ 
 / _ \ / /_   \ \      / /__| |_|_   _|__   ___ | |
| | | | '_ \   \ \ /\ / / _ \ '_ \| |/ _ \ / _ \| |
| |_| | (_) |   \ V  V /  __/ |_) | | (_) | (_) | |
 \___/ \___/     \_/\_/ \___|_.__/|_|\___/ \___/|_|
    """
    use = """
    Target: <Target> (For example: https://www.google.com)
    Wordlist: <Wordlist> (For example: /Wordlists/top1k.txt
    
    Wordlist List:
        subdomains.txt, top1k.txt, top10k.txt, top100.txt, top500.txt
    """
    print(banner + "\n" + use)

banner()


checkTarget = sub.SubFinder()

checkTarget.startSearch()


