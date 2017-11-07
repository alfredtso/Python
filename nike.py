from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# site to be scraped

myurl = 'https://www.nike.com.hk/best_sellers/list.htm'

# opening connection and grabbing the page
uClients = uReq(myurl)
page_html = uClients.read()
uClients.close()

# html parsing
page_soup = soup(page_html, "html.parser")

shoes = page_soup.findAll("li", {"class" : "style_liborder_new"})
print(shoes)

# testing
name_container = page_soup.findAll('span', {"class" : "up"})
name = name_container[10].text

#getting all the names
#for details in name_container:
#    print(details.text)

price_container = page_soup.findAll('dd', {"class" : "color666"})
price = price_container[10].text
print(price)

for details in price_container:


#for details in shoes:
#    name_container = details.findAll('span', {"class" : "up"})
