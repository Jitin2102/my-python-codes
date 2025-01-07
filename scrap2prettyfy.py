import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.wikihow.com/")
web.content
print(web.status_code==requests.codes.ok)
soup=BeautifulSoup(web.content,'html.parser') 
print(soup.a)