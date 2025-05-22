
import requests
from bs4 import BeautifulSoup
import lxml
if __name__ == '__main__':
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'
}

    target = 'https://www.bi09.cc/book/39452/1.html'
    req = requests.get(target,headers)
    req.encoding = 'utf-8'
    bs = BeautifulSoup(req.text, 'lxml')
    print(bs)
    texts = bs.find_all('div',id='chaptercontent')

