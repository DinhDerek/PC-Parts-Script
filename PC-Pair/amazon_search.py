'''
This file contains a function that will perform a search on amazon and 
find the price of an item at its product page.
'''
import re
import requests
from bs4 import BeautifulSoup


def amazon_search(query : str) -> (float, str):
    query = query.replace(' ','+')  #Formatting the search string by replacing spaces with "+" to be inserted into the url 
    amazon_url = "https://www.amazon.com/s?k=" + query.lower() + "&ref=nb_sb_noss"  #Building the url

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}  #Headers need to be created because amazon requires them to complete the http request
    
    amazon_searchpage = requests.get(amazon_url, headers=headers)   #Performing the http request
    page_soup = BeautifulSoup(amazon_searchpage.content, 'lxml')    #Gathering page information with BeautifulSoup
    print(page_soup.text)
    #
    first_result = page_soup.findAll("div", {"data-index": "1"})[0] #Grabbing the first result of the page
    price = first_result.findAll("span", {"class" : "a-offscreen"}) #Getting the price from the result
    if len(price) == 0: #If no price exists, the product is out of stock
        return((-1.0, ""))  #Return a tuple with -1.0 to represent OOS and an empty URL string
    else:   #Else, return the proper tuple 
        product_link = "https://www.amazon.com" + first_result.a['href']    #Create the product link
        product_price = price[0].get_text().replace(',','').lstrip('$')     #Get the product price and convert to a float
        return((float(product_price), product_link))


print(amazon_search('EVGA GeForce GTX 1650 SUPER SC ULTRA GAMING'))