import requests
import cloudscraper
import random
from time import sleep
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urljoin

def fetch_url(url, retries=3, delay=5):
    """获取网页内容，支持重试和反爬虫绕过"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    scraper = new_func()
    
    for attempt in range(retries):
        try:
            response = scraper.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 502:
                print(f"502 错误，第 {attempt+1}/{retries} 次重试...")
                sleep(delay + random.uniform(0, 2))
            else:
                print(f"HTTP 错误: {e}")
                break
        except Exception as e:
            print(f"请求失败: {e}")
            sleep(delay)
    return None

def new_func():
    scraper = cloudscraper.create_scraper()
    return scraper

def clean_content(text):
    """深度清理文本内容"""
    replacements = {
        '\xa0': ' ',
        '\u3000': ' ',
        '\r\n': '\n',
        '<br/>': '\n'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return '\n'.join(lines)

def parse_chapters(html, base_url):
    """解析章节列表"""
    soup = BeautifulSoup(html, 'lxml')
    chapters = []
    
    # 根据实际网页结构调整选择器
    chapter_list = soup.find('div', class_='book_last') or soup.find('div', id='list')
    if chapter_list:
        for a in chapter_list.find_all('a'):
            chapter_url = urljoin(base_url, a.get('href'))
            chapters.append((a.text.strip(), chapter_url))
    
    return chapters

def fetch_chapter_content(url):
    """获取并清理章节内容"""
    html = fetch_url(url)
    if not html:
        return None
    
    soup = BeautifulSoup(html, 'lxml')
    content_div = soup.find('div', id='chaptercontent') or soup.find('div', class_='content')
    if not content_div:
        return None
    
    raw_text = content_div.get_text(separator='\n', strip=True)
    return clean_content(raw_text)

def main():
    target_url = 'https://m.bi09.cc/book/39452/list.html'
    base_url = 'https://m.bi09.cc/book/39452/1.html'
    book_name = "天之下.txt"
    
    # 获取目录页
    catalog_html = fetch_url(target_url)
    if not catalog_html:
        print("无法获取目录页面")
        return
    
    # 解析章节列表
    chapters = parse_chapters(catalog_html, base_url)
    if not chapters:
        print("未找到章节列表")
        return
    
    print(f"共找到 {len(chapters)} 章")
    
    # 创建进度条
    with tqdm(chapters, desc="下载进度", unit="章") as pbar:
        for chapter_name, chapter_url in pbar:
            pbar.set_postfix_str(chapter_name[:10])  # 显示当前章节名前10字
            
            # 获取章节内容
            content = fetch_chapter_content(chapter_url)
            if not content:
                print(f"\n章节获取失败: {chapter_name}")
                continue
            
            # 写入文件
            with open(book_name, 'a', encoding='utf-8') as f:
                f.write(f"\n\n{chapter_name}\n\n")
                f.write(content)
            
            # 随机延迟防止被封
            sleep(random.uniform(0.5, 1.5))

if __name__ == '__main__':
    main()