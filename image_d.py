import requests
import urllib.request
from bs4 import BeautifulSoup


url = input("Enter the url bro: ")
#url ='https://www.greaterkashmir.com/'

headers = {
     'Accept-Encoding': 'gzip, deflate, sdch',
     'Accept-Language': 'en-US,en;q=0.8',
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'Referer': 'http://www.wikipedia.org/',
     'Connection': 'keep-alive',
}

r = requests.get(url=url, headers=headers)
print(r)

soup = BeautifulSoup(r.text, 'html.parser')
i = 0
for img in soup.findAll('img'):
    i += 1
    image_temp = img.get('src')
    if image_temp[:1] == '/':
        image_path = url + image_temp
    else:
        image_path = image_temp

    if '.jpg' in image_path:
        with open("images/{}.jpg".format(i), 'wb') as f:
            f.write(requests.get(url=image_path).content)
    else:
        pass
