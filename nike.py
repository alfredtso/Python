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

# getting all the products

products_containers = page_soup.findAll("ul", {"class" : "products_list clearfix"})


for products in products_containers :
    name_container = page_soup.findAll('span', {"class" : "up"})

    price_container = page_soup.findAll('dd', {"class" : "color666"})

# testing
name_container = page_soup.findAll('span', {"class" : "up"})
name = name_container.text

print(name)

#getting all the names
#for details in name_container:
#    print(details.text)

price_container = page_soup.findAll('dd', {"class" : "color666"})
price = price_container[10].text

print(price)
