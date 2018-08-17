# wiesliam
# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

def find_author(link):
	page = requests.get(link)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.find('title')
	title = title.text.replace(" | The Michigan Daily", "")
	try:
		author = soup.select(".byline > .link > a")[0].text
	except:
		author = None
	return title, author

page = requests.get("http://michigandaily.com")
#print(page)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

most_read = []
links = soup.select("ol > li > a")
for link in links:
	most_read.append(find_author("http://www.michigandaily.com" + link.get('href')))

#print(most_read)

print("Michigan Daily -- MOST READ  ")

for title, author in most_read:
	print(title, '\n  by', author)

