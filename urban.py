import sys
import requests
from bs4 import BeautifulSoup as bs
import argparse

parser = argparse.ArgumentParser(description="Urban Dictionary command line tool")
parser.add_argument("lookup" , help="Enter a word or phrase to lookup.")

try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

r = requests.get('https://www.urbandictionary.com/define.php?term={}'.format(args.lookup))
head = r.headers['content-type']
content = r.text
soup = bs(content, 'html.parser')
definition = soup.find("meta", property="og:description")
title = soup.find("meta", property="og:title")


print (title["content"])
print (definition["content"])
