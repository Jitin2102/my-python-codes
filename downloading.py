import requests
res=requests.get("https://www.gutenberg.org/cache/epub/1112/pg1112.txt")
res.raise_for_status()
playFile=open("RomeoAndJuliet.txt",'wb')
for chunk in res.iter_content(100000):
    print(chunk)