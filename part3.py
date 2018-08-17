# wiesliam
# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

page = requests.get("http://michigandaily.com")
print(page)
soup = BeautifulSoup(page.content, 'html.parser')
