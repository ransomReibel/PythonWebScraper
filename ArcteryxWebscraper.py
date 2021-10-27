from urllib.request import Request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


#opens connection 

req = Request('https://tacticalgear.com/arcteryx-leaf', headers={'User-Agent': 'Mozilla/5.0'})
webpage = uReq(req).read()


page_soup = soup(webpage, "html.parser")

containers = page_soup.findAll("li",{"class":"c5-sm-active"})

filename = "T_G_Prices.csv"
f = open(filename, "w")

headers = "Product, Price\n"
f.write(headers)


for container in containers:


        pricesup = container.findAll("span",{"class":"price"})
        price = pricesup[0]
        title = container.findAll("span",{"class":"product-title"})
        id= title[0]
        final_price = price.text
        final_id = id.text
        print(final_id)
        print(final_price)
        f.write(final_id + "," + final_price + "\n")
       
       
