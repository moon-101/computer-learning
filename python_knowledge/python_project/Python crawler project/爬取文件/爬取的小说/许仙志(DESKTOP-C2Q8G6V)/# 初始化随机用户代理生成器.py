import requests
from bs4 import BeautifulSoup
import lxml
import chardet
import time
import random
import os
import json
from fake_useragent import UserAgent
from tqdm import tqdm
import string
# 初始化随机用户代理生成器

headers = {
    'User-Agent': UserAgent().random,  # 每次请求生成随机UA
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.22biqu.com/',
    'DNT': '1'  # 禁止追踪
}

# 基准目录
base_directory = r'D:\games\computer-learning\爬取的小说'
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# 目标目录
target_directory = os.path.join(base_directory, '许仙志')
if not os.path.exists(target_directory):
    os.makedirs(target_directory)
    print(f"{target_directory}已创建")
else:
    print("已存在")
min_interval = 1
max_interval = 5

for i in tqdm(range(12278419, 12278429), 
             desc="正在爬取小说", 
             unit="章",
             ncols=100,
             dynamic_ncols=True):

    # 测试异常
    try:
        url = f"https://www.22biqu.com/biqu13446/{i}.html"
        url2 = f"https://www.22biqu.com/biqu13446/{i}_2.html"
        # 请求网站，获取原始内容
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # 自动检测编码
        det = chardet.detect(response.content)
        actual_encoding = det['encoding']
        # print(f"编码：{actual_encoding}")  # 注释掉

        # 使用正确编码解码
        response.encoding = actual_encoding
        html_content = response.text

        # 解析内容
        soup = BeautifulSoup(html_content, 'lxml')

        # 确定好随机访问时间间隔
        interval = random.uniform(min_interval, max_interval)

        # 获取章节标题
        title_tag = soup.find("h1", class_='title')
        raw_title = title_tag.get_text().strip() if title_tag else f"第{i-12278418}章"
        # print(raw_title)  # 注释掉
        cleaned_title = raw_title
        """     clean_filename=raw_title
        # 加强版文件名清理
        def clean_filename(title):
            # 替换常见非法字符
            title = title.replace('\n', '').replace('\r', '').strip()
            # 只保留允许的字符
            valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
            cleaned = ''.join(c for c in title if c in valid_chars)
            # 确保不为空
            return cleaned or f"第{i-12278418}章"
        """
        # 是否有下一页
        response_2 = requests.get(url2, headers=headers)
        # 确保目录存在
        os.makedirs(target_directory, exist_ok=True)

        # 获取正文内容
        content_div = soup.find("div", id='content')
        print(content_div)  # 只保留这一行输出

        if content_div:
            # 清理文本内容
            text_content = content_div.get_text()
            # 优化后的处理逻辑
            # 步骤1: 清理原始文本（移除Windows换行符\r）
            cleaned_text = text_content.replace('\r', '')

            # 步骤2: 按双换行符分割成段落（识别段落分隔）
            paragraphs = cleaned_text.split('\n\n')

            # 步骤3: 创建空列表存储处理后的段落
            processed_paragraphs = []

            # 步骤4: 遍历所有段落
            for para in paragraphs:
                # 移除段落首尾的空白字符（但保留段内格式）
                stripped_para = para.strip()
                
                # 跳过空段落（避免处理空白行）
                if not stripped_para:
                    continue
                
                # 步骤5: 为每个非空段落添加首行缩进
                # 关键：只处理段落首行，保持段内换行不变
                indented_para = '　　' + stripped_para.replace('\n', '\n')  # 保持段内换行
                
                processed_paragraphs.append(indented_para)

            # 步骤6: 用单换行符合并所有段落（符合中文排版规范）
            cleaned_content = '\n'.join(processed_paragraphs)

            # 保存为单独文件
            filename = os.path.join(target_directory, f"{cleaned_title}.txt")
            with open(filename, encoding='utf-8', mode='w') as f:
                f.write(cleaned_content)
            
            if response_2:
                soup_2 = BeautifulSoup(response_2.text, 'lxml')
                houxu = soup_2.find("div", id='content').get_text()
                houxu = '\n'.join(
                    ('　　' + line.strip() if i == 0 else line.strip())  # 仅首行缩进
                    for i, line in enumerate(
                        text_content.replace('\r', '').split('\n\n')  # 按段落分割
                    ) if line.strip()
                )

                with open(filename, encoding='utf-8', mode='a') as f:
                    f.write(houxu)   
            else:         
                print(f"小说{cleaned_title}保存完成")  # 注释掉
        else:
            print("未完成")  # 注释掉
        
        time.sleep(interval)
    except Exception as e:
        tqdm.write((f"处理{url}发生错误：{e}"))  # 注释掉
        continue
