from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.com/global/hk/Desktop-Graphics-Cards/SubCategory/ID-48?nm_mc=KNC-GooglehkAdwords&cm_mmc=KNC-GooglehkAdwords-_-Sitelink-Hong-Kong-_-VGA-Cards-_-Global&gclid=EAIaIQobChMIv6nh1ImU1wIVVR9oCh1aUABZEAAYASACEgIHnfD_BwE'

# opening connection and grabbing the page
uClients = uReq(myurl)
page_html = uClients.read()
uClients.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabbing each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "graphics_card.csv"
f = open(filename, "w")

headers = "brand, product_name, features\n"

f.write(headers)


#for loop
for contain in containers:
	brand = contain.div.div.a.img["title"]

	title_container = contain.findAll("a",{"class" : "item-title"})
	product_name = title_container[0].text

	feature_container = contain.findAll("ul", {"class" : "item-features"})
	features = feature_container[0].text

	print("brand: " + brand )
	print("product_name: " + product_name)
	print("features: " + features)

	f.write(brand + "," + product_name.replace(",", "|") + "," + features + "\n")

f.close()


