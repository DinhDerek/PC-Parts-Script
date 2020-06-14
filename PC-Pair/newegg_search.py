'''
This file contains a function that will perform a search on microcenter and 
find the price of an item at its product page.
'''

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def newegg_search(searchstr:str) -> (float,str):
    searchstr = searchstr.replace(' ','+') #replaces any spaces with + signs because URL uses + as spaces
    newegg_url = "https://www.newegg.com/p/pl?d=" + searchstr #builds URl to grab from
    #print(newegg_url)
    # Accesses HTML code
    URLRequest = uReq(newegg_url)
    page_html = URLRequest.read()
    URLRequest.close()
    page_soup = soup(page_html, "html.parser")
    #
    parent_class = page_soup.findAll("div", {"class": "item-container"})
    container = parent_class[4].find("div",{"class": 'item-info'}) #contains HTML info of computer part,
    #print(container)
    #uses index 4 because the first 3 indexes are 'recommended products' not actual 1st item
    price = container.find("li",{"class": 'price-current'})
    link = container.find("a",{"class": 'item-title'})
    if container.p.text == "OUT OF STOCK": #if item is out of stock
        return(-1.0,"")
    else:
        product_link = link['href'] 
        product_price = price.text
        product_price = (product_price.lstrip('\n')).split("\xa0")
        product_price = product_price[0].replace('$',"")
        return (float(product_price.replace(',' ,"")),product_link) #returns a tuple of (price,url) types = (float,str)
