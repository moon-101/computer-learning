import requests
import random
from bs4 import BeautifulSoup
import lxml
from time import sleep
from tqdm import tqdm


#请求数据

url = 'https://movie.douban.com/subject/34780991/comments'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}

#抓取前100个评论
for page in range(0,100,20):
    params = {
        'start':page,
        'limit':20,

    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # 检查请求状态



        #解析数据
        soup = BeautifulSoup(response.text, 'lxml')

        comments = soup.find_all('p', class_='comment-content')

        with open('comments1.txt', 'a', encoding='utf-8') as f:
            for comment in tqdm(comments):
                content = comment.text.strip()
                f.write(content + '\n')

                #保存数据
                sleep(random.uniform(1, 4))  # 随机延时

    except Exception as e:
        print(f'请求失败：{str(e)}')
        break

