#!/usr/bin/env python
# coding: utf-8

# Imports
import requests
from bs4 import BeautifulSoup
from termcolor import colored, cprint
import sys

#vars
baseurl = "https://www.bbc.co.uk"
scrape_url = "https://www.bbc.co.uk/news"
stories = ['null']

#def get_soup(url):
	

def get_headlines(item_start_id):
	current_item = item_start_id
	#request and parse html
	response = requests.get(scrape_url)
	soup = BeautifulSoup(response.text, "html.parser")

	#main headline vars
	headlineouter = soup.find('a', class_ = "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor")
	headlineinner = headlineouter.find('h3')
	headline_url = headlineouter['href']
	stories.append(headline_url)
	#print the main headline and accompanying url
	cprint(f"[{current_item}]{headlineinner.text}", 'red', attrs=['bold'], end='\n')
	current_item+=1
	
	#isolate the rest of the headlines (articles)
	articles = soup.find_all('a',class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")

	#extract headline and url from links on main page & print

	links_to_fetch = 10
	for item in range(links_to_fetch):
		articleurl = articles[item].get('href')
		articleheadline = articles[item].h3.text
		stories.append(articleurl)
		cprint(f"[{current_item}]{articleheadline}:", 'red', attrs=['bold'],end='\n')
		current_item+=1


def get_article_text(partial_url):
	global baseurl
	complete_url = baseurl + partial_url
	response = requests.get(complete_url)
	soup = BeautifulSoup(response.text, "html.parser")
	story = soup.find_all('p')
	#range_start is set to 12 to ignore all the pre-amble / social media ads.
	#range is -4 to remove unnecessary text
	range_start = 12
	for item in range(len(story)-4):
		if item < range_start:
			pass
		else:
			print(story[item].text)

	cprint("Press any key to return to Main Menu", 'red', attrs=['bold'], end='\n')
	input()

def main():
	get_headlines(1)
	article_id = input("select an article id or Q to quit\n")
	if article_id.lower() == 'q':
		cprint("Goodbye!", 'red', end='\n')
		sys.exit()
	
	else:
		partial_url = stories[int(article_id)]
		get_article_text(partial_url)

while __name__ == "__main__":
	main()
	
	
