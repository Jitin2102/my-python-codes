import requests
from bs4 import BeautifulSoup
web = requests.get("https://www.tutorialsfreak.com/")
soup = BeautifulSoup(web.content, "html.parser")
print(soup.p.string)
