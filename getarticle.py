#!/user/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup as bs

def get_article_text(article_url):
	base_url = "https://www.bbc.co.uk"
	complete_url = base_url + partial_url
	response = requests.get(complete_url)
	soup = bs(response.text, "html.parser")
	story = soup.find_all('p')
	i = 12
	while i < (len(story)-4):
		print(story[i].text)
		i+=1

