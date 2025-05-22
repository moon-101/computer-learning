
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://www.bi09.cc/book/39452/1.html'
    req = requests.get(target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    texts = bs.find('div',id='chaptercontent')
    print(texts)
