import sys
import requests
import webbrowser
import bs4


if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    
    print('Googling...') 
    res = requests.get('https://www.google.com/search?q=' + query)
    res.raise_for_status()
    
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select('a')
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        webbrowser.open('https://www.google.com' + linkElems[i].get('href'))
else:
    print('Usage: python lucky.py <search terms>')

