'''
This file contains a function that will perform a search on microcenter and 
find the price of an item at its product page.
'''
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def microcenter_search(searchstr:str) -> (float,str):
    search_words = searchstr.split(' ') #Splits the search query into individual words to be used later when matching to the first result
    searchstr = searchstr.replace(' ','+') #replaces any spaces with + signs because URL uses + as spaces
    microcenter_url = "https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=" + searchstr + "&searchButton=search" #builds URl to grab from
    # Accesses HTML code
    URLRequest = uReq(microcenter_url)
    page_html = URLRequest.read()
    URLRequest.close()
    page_soup = soup(page_html, "html.parser")
    #
    parent_class = page_soup.find('li',{"id": 'pwrapper_0'})
    product_info = parent_class.find("div",{"class": re.compile('^pDescription compressedNormal(\d)*$')}) #contains HTML info of computer part, repattern because microcenter uses different classes on searches but with diff numbering only #POSSIBLE ERROR: NOT ALL PRODUCTS USE THE PATTERN BUT WE ARE ASSUMING

    stock = parent_class.find("div",{"class":'stock'})
    if stock.text.replace("\n","") == "Sold Out" or any(product_info.a.text.find(word) == -1 for word in search_words): #if item is out of stock or does not match the search query
        return (-1.0,"")
    else:
        product_price = product_info.a['data-price']
        product_link = product_info.a['href']
        return (float(product_price.replace(',' ,"")),'https://www.microcenter.com' + str(product_link), product_info.a.text) #returns a tuple of (price,url) types = (float,str)

