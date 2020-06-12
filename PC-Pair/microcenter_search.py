'''
This file contains a function that will perform a search on microcenter and 
find the price of an item at its product page.
'''
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
def microcentersearch(searchstr:str):
    searchstr = searchstr.replace(' ','+') #replaces any spaces with + signs because URL uses + as spaces
    for brand in ['evga','asus','msi']: #grabs brand name from str
        if brand in searchstr.lower():
            brand_name = brand
    microcenter_url = "https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=" + searchstr + "&searchButton=search" #builds URl to grab from
    # Accesses HTML code
    URLRequest = uReq(microcenter_url)
    page_html = URLRequest.read()
    URLRequest.close()
    page_soup = soup(page_html, "html.parser")
    #
    container = page_soup.findAll("div",{"class":"pDescription compressedNormal2"}) #contains HTML info of computer part
    #loops through items in the HTML accessing their data
    for item in container:
        product_brand = item.a['data-brand']
        if brand_name.lower() == product_brand.lower():
            product_name =item.a['data-name']
            product_price = item.a['data-price']
            print(' Product Brand:',product_brand, "\n",'Product Name:', product_name,"\n",'Product Price:', product_price,"\n")
   
    
microcentersearch('EVGA RTX 2080')
#microcentersearch('msi RTX 2080')
#microcentersearch('AsUS RTX  2080')

