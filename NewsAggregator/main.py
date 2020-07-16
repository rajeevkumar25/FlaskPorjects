import requests
from bs4 import BeautifulSoup

class NewsAggregator():
    
    
    def __init__(self):
        self.toilink='https://timesofindia.indiatimes.com/briefs'
        self.htlink='https://www.hindustantimes.com/india-news/'
        self.googlelink='https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen' #Google India news

    
    def getToiNews(self):
        toi_news=[]
        try:
            site_content=requests.get(self.toilink)
            soup=BeautifulSoup(site_content.content,'html.parser')
            toi_headings=soup.find_all('h2')
            toi_headings=toi_headings[2:-13] #removing footer links
            #print(headings)
            for th in toi_headings:
                toi_news.append(th.text)
            #print(toi_news)    
            return toi_news
                

        except Exception as ex:
            print(ex)

       
    def getHtNews(self):
        ht_news=[]
        try:
            site_content=requests.get(self.htlink)
            soup=BeautifulSoup(site_content.content,'html.parser')
            ht_headings=soup.findAll('div',{'class':'headingfour'})
            #print(ht_headings)
            ht_headings=ht_headings[2:] # removing header links

            for ht in ht_headings:
                ht_news.append(ht.text)
            return ht_news    

        except Exception as ex:
            print(ex)

        
    def getGoogleNews(self):
        google_news=[]
        try:
            site_content=requests.get(self.googlelink)
            soup=BeautifulSoup(site_content.content,'html.parser')
            google_headings=soup.findAll('h3',{'class':'ipQwMb ekueJc gEATFF RD0gLb'})
            #print(google_headings)
            for heading in google_headings:
                google_news.append(heading.text)
                
            return google_news

        except Exception as ex:
            print(ex)

obj=NewsAggregator()
#obj.getToiNews()
#obj.getHtNews()
obj.getGoogleNews()
