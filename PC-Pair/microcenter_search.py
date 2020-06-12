'''
This file contains a function that will perform a search on microcenter and 
find the price of an item at its product page.
'''
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
def microcentersearch(searchstr:str):
    searchstr = searchstr.replace(' ','+') #replaces any spaces with + signs because URL uses + as spaces
    print('searchstr=', searchstr) #tests searchstr
    microcenter_url = "https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=" + searchstr + "&searchButton=search" #builds URl to grab from
    print("microcenter_url=",microcenter_url) #tests microcenterURL
    
microcentersearch('RTX 2080')
microcentersearch('RTX2080')
microcentersearch('RTX  2080')


