import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.google.com/")  # importing text from google.com
soup=BeautifulSoup(web.content,"html.parser")
# print(soup.select_one('div').get_text())



spanEle=soup.find('span')
print(str(spanEle))
print(spanEle.attrs)