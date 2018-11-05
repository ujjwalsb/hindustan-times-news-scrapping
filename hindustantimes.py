import requests 
import csv
import pandas as pd
from bs4 import BeautifulSoup 

def htnews(): 
    url1='https://www.hindustantimes.com/latest-news'
    # url2='https://www.hindustantimes.com/top-news'
    
    web_response = requests.get(url1) 
    
    if web_response.status_code==200:     
        soup=BeautifulSoup(web_response.text,'html.parser')	 
        newslist=soup.find("ul",{"class":"latest-news-bx"}) 
        # newslist=soup.find("ul",{"class":"latestnews-topblk"}) 
        # print(newslist)
        with open("Top_News.csv",'w') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow(['News','Link'])
            for news in newslist.findAll("a"):
                # if news.text != ' read more' or news.text != 'read more':
                if news.text.startswith(" read more") or news.text.startswith("read more") :
                    pass
                else:
                    print(news.text)
                    row = news
                    writer.writerow(row)
        f.close()
        df = pd.read_csv('Top_News.csv')
        df.drop('Link', axis = 1, inplace = True)
        df.to_csv('Top_News.csv', index = False)
    else: 
        print("Webpage Error: Please try again...") 
    
        
htnews()
