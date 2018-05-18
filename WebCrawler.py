import requests
from bs4 import BeautifulSoup

def trade_spider(max_pge):
    page = 1
    while page <= max_pge:
        #take the url of the website from where you want to crawl and add page to it as it will loop through it
        url = 'https://www.flipkart.com/books/fiction-nonfiction-books/literature-fiction-books/pr?page=' + str(page) + '&sid=bks%2Cfnf%2Cgld&viewType=grid'
        
        #connection is need therefore using below code connection is made to given url
        src = requests.get(url)
        
        #to get only necessary text
        plain_txt = src.text
        
        #creating object of beautifulsoup
        soup = BeautifulSoup(plain_txt)

        #using object of beautifulsoup from anchors ('a') unique class name is imported ({'class':'name'})
        for link in soup.findAll('a', {'class': '_2cLu-l'}):
            #here href in imported n displayed along with the link
            href = "https://www.flipkart.com" + link.get('href')
            print(href)
        page += 1

#function is called
trade_spider(1)
