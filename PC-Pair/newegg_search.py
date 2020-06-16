''''
This file contains a function that will perform a search on microcenter and 
find the price of an item at its product page.
'''

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def newegg_search(searchstr:str) -> (float, str, str):
    search_words = searchstr.lower().split(' ') #Splits the search query into individual words to be used later when matching to the first result
    searchstr = searchstr.replace(' ','+') #replaces any spaces with + signs because URL uses + as spaces
    newegg_url = "https://www.newegg.com/p/pl?d=" + searchstr #builds URl to grab from
    #print(newegg_url)
    # Accesses HTML code
    URLRequest = uReq(newegg_url)
    page_html = URLRequest.read()
    URLRequest.close()
    page_soup = soup(page_html, "html.parser")
    #
    try:
        parent_class = page_soup.find("div", {"class": "items-view is-grid"})
        first_result = parent_class.findAll("div", {"class": "item-container"})[0]
        container = first_result.find("div",{"class": 'item-info'}) #contains HTML info of computer part,
        #print(container)
        #uses index 4 because the first 3 indexes are 'recommended products' not actual 1st item
        price = container.find("li",{"class": 'price-current'})
        link = container.find("a",{"class": 'item-title'})
        if container.p.text == "OUT OF STOCK" or any(link.text.lower().find(word) == -1 for word in search_words) or price.text == '\n': #if item is out of stock or does not match the search query
            return(-1.0,"", "")
        else:
            product_link = link['href'] 
            product_price = price.text
            product_price = (product_price.lstrip('\n')).split("\xa0")
            product_price = product_price[0].replace('$',"")
            return (float(product_price.replace(',' ,"")), product_link, link.text) #returns a tuple of (price,url, name) types = (float,str, str)
    except AttributeError:
        return(-1.0,"", "")