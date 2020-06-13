'''
This file contains a function that will perform a search on microcenter and 
find the price of an item at its product page.
'''
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
def microcentersearch(searchstr:str):
    searchstr = searchstr.replace(' ','+') #replaces any spaces with + signs because URL uses + as spaces
    microcenter_url = "https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=" + searchstr + "&searchButton=search" #builds URl to grab from
    #print(microcenter_url)
    # Accesses HTML code
    URLRequest = uReq(microcenter_url)
    page_html = URLRequest.read()
    URLRequest.close()
    page_soup = soup(page_html, "html.parser")
    #
    container = page_soup.findAll("div",{"class": re.compile('^pDescription compressedNormal(\d)*$')}) #contains HTML info of computer part
    #loops through items in the HTML accessing their data
    #product_brand = container[0].a['data-brand']
    #product_name = container[0].a['data-name']
    product_price = container[0].a['data-price']
    product_link = container[0].a['href']
    #print(' Product Brand:',product_brand, "\n",'Product Name:', product_name,"\n",'Product Price:', product_price,"\n",product_link,"\n")
    return (float(product_price.strip(',')),'https://www.microcenter.com' + str(product_link))
    
print(microcentersearch('asus'))



