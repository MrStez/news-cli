#!/usr/bin/env python
# coding: utf-8

# Imports
import requests
from bs4 import BeautifulSoup
from termcolor import colored, cprint
import sys

#vars
stories = ['null']

def get_soup(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")	
	return soup

def get_headlines(item_start_id, links_to_fetch):
	scrape_url = "http://feeds.bbci.co.uk/news/rss.xml"
	current_item = item_start_id
	#request and parse html
	soup = get_soup(scrape_url)
	#isolate the rest of the headlines (articles)
	articles = soup.find_all('item')
	#extract headlines and url from links on main page & print
	for item in range(links_to_fetch):
		articleurl = articles[item].guid.text
		articleheadline = articles[item].title.text
		stories.append(articleurl)
		cprint(f"[{current_item}]{articleheadline}:", 'red', attrs=['bold'],end='\n')
		current_item+=1

#partial url example ( /news/1072279 ) 
def get_article_text(article_url):
	soup = get_soup(article_url)
	story = soup.find_all('p')
	#range_start is set to 12 to ignore all the pre-amble / social media ads.
	range_start = 12
	for p_tag in range(len(story)):
		if p_tag < range_start:
			pass
		else:
			print(story[p_tag].text)

	cprint("Press any key to return to Main Menu", 'red', attrs=['bold'], end='\n')
	input()

def main():
	get_headlines(1, 10)
	article_id = input("select an article id or Q to quit\n")
	if article_id.lower() == 'q':
		cprint("Goodbye!", 'red', end='\n')
		sys.exit()
	
	else:
		article_url = stories[int(article_id)]
		get_article_text(article_url)

while __name__ == "__main__":
	main()
	
	
