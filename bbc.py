#!/usr/bin/env python
# coding: utf-8

# Imports
import requests
from bs4 import BeautifulSoup
from termcolor import colored, cprint
#from getarticle import get_article_text
#vars
baseurl = "https://www.bbc.co.uk"
scrape_url = "https://www.bbc.co.uk/news"
x = 1
#request and parse html
response = requests.get(scrape_url)
soup = BeautifulSoup(response.text, "html.parser")

#main headline vars
headlineouter = soup.find('a', class_ = "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor")
headlineinner = headlineouter.find('h3')

#print the main headline and accompanying url
cprint(f"{headlineinner.text}", 'red', attrs=['bold'], end=' ')
cprint(f"([{x}]{baseurl}{headlineouter['href']})", 'blue', end='\n')
x+=1
#isolate all headlines (articles)
articles = soup.find_all('a',class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")

#extract headline and url from links on main age & print
i = 0
links_to_fetch = 10
while i < links_to_fetch:
	articleurl = articles[i].get('href')
	articleheadline = articles[i].h3.text
	cprint(f"[{x}]{articleheadline}:", 'red', attrs=['bold'],end='')
	cprint(f"({baseurl}{articleurl})", 'blue', end='\n')
	x+=1
	i+=1

