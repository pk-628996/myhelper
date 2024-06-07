from requests import post 
from bs4 import BeautifulSoup
 
def shorturl_at(url):
    response=post("https://www.shorturl.at/shortener.php",data={"u":url})
    if response.status_code == 200:
        soup=BeautifulSoup(response.text,"html.parser")
        return soup.find(id="shortenurl")["value"]
    else:
       print('An Unknown error occured')