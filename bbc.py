#!/usr/bin/env python
# coding: utf-8

# Imports
import requests
from bs4 import BeautifulSoup
from termcolor import colored, cprint
import pandas as pd
import sys

#from getarticle import get_article_text

#vars
baseurl = "https://www.bbc.co.uk"
scrape_url = "https://www.bbc.co.uk/news"
x = 1
stories = ['null']

def get_headlines():
	global x
	#request and parse html
	response = requests.get(scrape_url)
	soup = BeautifulSoup(response.text, "html.parser")

	#main headline vars
	headlineouter = soup.find('a', class_ = "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor")
	headlineinner = headlineouter.find('h3')
	headline_url = headlineouter['href']
	stories.append(headline_url)
	#print the main headline and accompanying url
	cprint(f"[{x}]{headlineinner.text}", 'red', attrs=['bold'], end='\n')
	x+=1
	#isolate all headlines (articles)
	articles = soup.find_all('a',class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")

	#extract headline and url from links on main age & print
	i = 0
	links_to_fetch = 10
	while i < links_to_fetch:
		articleurl = articles[i].get('href')
		articleheadline = articles[i].h3.text
		stories.append(articleurl)
		cprint(f"[{x}]{articleheadline}:", 'red', attrs=['bold'],end='\n')
		x+=1
		i+=1

def get_article_text(partial_url):
    base_url = "https://www.bbc.co.uk"
    complete_url = base_url + partial_url
    response = requests.get(complete_url)
    soup = BeautifulSoup(response.text, "html.parser")
    story = soup.find_all('p')
	#i is set to 12 to ignore all the pre-amble / social media ads.
	#range is -4 to remove unnecessary post-amble?
    i = 12
    while i < (len(story)-4):
        print(story[i].text)
        i+=1

def main():
	global x
	x = 1 
	get_headlines()
	article_id = input("select an article id or Q to quit\n")

	if article_id == 'Q' or article_id == 'q':
		cprint("Goodbye!", 'red', end='\n')
		sys.exit()
	
	else:
		partial_url = stories[int(article_id)]
		get_article_text(partial_url)

while __name__ == "__main__":
	main()
	
	
