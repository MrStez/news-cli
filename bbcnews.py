#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from termcolor import colored, cprint

# In[4]:


baseurl = "https://www.bbc.co.uk"
scrape_url = "https://www.bbc.co.uk/news"


# In[5]:


response = requests.get(scrape_url)


# In[6]:


soup = BeautifulSoup(response.text, "html.parser")


# In[29]:


headlineouter = soup.find('a', class_ = "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor")
headlineinner = headlineouter.find('h3')


# In[32]:


#print the main headline and accompanying url
cprint(f"{headlineinner.text}", 'red', attrs=['bold'], end=' ')
cprint(f"({baseurl}{headlineouter['href']})", 'blue', end='\n')


# In[71]:


articles = soup.find_all('a',class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")
i = 0
links_to_fetch = 10
while i < links_to_fetch:
    articleurl = articles[i].get('href')
    articleheadline = articles[i].h3.text
    cprint(f"{articleheadline}:", 'red', attrs=['bold'],end='')
    cprint(f"({baseurl}{articleurl})", 'blue', end='\n')
    i+=1

