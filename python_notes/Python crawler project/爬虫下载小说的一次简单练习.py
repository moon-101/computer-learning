import requests
import cloudscraper
import random
from time import sleep
from bs4 import BeautifulSoup
from tqdm import tqdm

def __init__(self,url):
    self.url=url

def fetch_url(url, retries=3, delay=5):
    # 伪装请求头，避免被网站屏蔽
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    scraper = cloudscraper.create_scraper()
    
    for attempt in range(retries):
        try:
            response = scraper.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 502:
                print(f"502错误，第{attempt+1}次重试...")
                sleep(delay + random.uniform(0, 2))  # 随机延迟增加
            else:
                print(f"HTTP错误: {e}")
                break
        except Exception as e:
            print(f"请求失败: {e}")
            sleep(delay)
    return None

def clean_content(text):
    """深度清理文本内容"""
    #替换多种空白字符
    replacements = {
        'xa0':' ',
        'u3000':' ',
        '\r\n':'\n',
        '<br/>':'\n'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    #去除多余的空白字符

    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return '\n'.join(lines)


    # 使用示例
    html = fetch_url("https://www.bi09.cc/book/39452/1.html")
    server = fetch_url('https://m.bi09.cc/book/')
    book_name="天之下.txt"
    if html:
        print("成功获取页面内容")
    else:
        print("无法获取内容，请检查网络或目标网站状态。")

if __name__ == '__main__':
    target = 'https://www.bi09.cc/book/39452.html'

    if "Bad gateway" in html:
        print("错误，仍然被Cloudflare拦截,请检查反爬策略")
    else:
        bs = BeautifulSoup(html, 'lxml')
        content_div = bs.find('div',id='chaptercontent')

        if content_div:
            raw_text = content_div.get_text(separator='\n',strip=True)
            cleaned_text = clean_content(raw_text)
            print(cleaned_text)
            paragraphs = [p for p in cleaned_text.split('\n') if p]
        else:
            print("未找到章节内容")

    req =requests.get(url=target)
    req.encoding = 'utf-8'
    chapter_yuan = req.text
    chapter_yuan_bs = BeautifulSoup(chapter_yuan, 'lxml')
    chapter_name = chapter_yuan_bs.find('div', class_='book_last')
    chapters = chapter_name.find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = cleaned_text
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
    




