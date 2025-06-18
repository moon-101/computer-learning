#引入第三方库
import requests#发送html请求的
import random#随机数
from bs4 import BeautifulSoup#解析html内容
import lxml#便于解析
from time import sleep#程序暂停
from tqdm import tqdm#循环可视化

#请求数据
#发送请求的网站网址
url = 'https://movie.douban.com/subject/34780991/comments'
#请求头、反反爬虫机制
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
        response.raise_for_status()  #状态码 检查请求状态



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

