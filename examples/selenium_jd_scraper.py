#!/usr/bin/env python3
"""
# 示例：使用 Selenium 抓取京东商品（教学/示例用途，仅用于学习，遵守 robots.txt 与服务条款）
# 依赖: selenium, webdriver-manager, pandas

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 基本配置
SEARCH_KEYWORD = "笔记本"
MAX_ITEMS = 50  # 本示例抓取的最大商品数量
OUTPUT_CSV = "examples/sample_jd_products.csv"

def make_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.set_page_load_timeout(30)
    return driver

def parse_search_results(driver):
    items = []

    # 等待商品列表加载
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#J_goodsList .gl-item, .gl-item")))

    product_nodes = driver.find_elements(By.CSS_SELECTOR, "#J_goodsList .gl-item, .gl-item")

    for node in product_nodes:
        try:
            title_el = node.find_element(By.CSS_SELECTOR, ".p-name em")
            title = title_el.text.strip()
        except Exception:
            title = ""

        try:
            price_el = node.find_element(By.CSS_SELECTOR, ".p-price strong i")
            price = price_el.text.strip()
        except Exception:
            price = ""

        try:
            shop_el = node.find_element(By.CSS_SELECTOR, ".p-shop a, .p-shop .J_im_icon")
            shop = shop_el.text.strip()
        except Exception:
            shop = ""

        try:
            comments_el = node.find_element(By.CSS_SELECTOR, ".p-commit a")
            comments = comments_el.text.strip()
        except Exception:
            comments = ""

        try:
            link_el = node.find_element(By.CSS_SELECTOR, ".p-img a")
            link = link_el.get_attribute("href")
        except Exception:
            link = ""

        items.append({
            "title": title,
            "price": price,
            "shop": shop,
            "comments": comments,
            "link": link,
        })

        if len(items) >= MAX_ITEMS:
            break

    return items

def save_to_csv(rows):
    keys = ["title", "price", "shop", "comments", "link"]
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

def main():
    driver = make_driver(headless=True)
    try:
        url = f"https://search.jd.com/Search?keyword={SEARCH_KEYWORD}"
        driver.get(url)
        time.sleep(2)  # 初始等待，实际项目中建议使用显式等待

        all_items = []
        page = 1
        while len(all_items) < MAX_ITEMS and page <= 3:
            print(f"Scraping page {page} ...")
            items = parse_search_results(driver)
            all_items.extend(items)

            # 翻页：尝试点击下一页
            try:
                next_btn = driver.find_element(By.CSS_SELECTOR, ".pn-next")
                driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(2)
                page += 1
            except Exception:
                break

        # 去重并保存（简单去重）
        unique = {i['link']: i for i in all_items if i.get('link')}
        rows = list(unique.values())[:MAX_ITEMS]
        save_to_csv(rows)
        print(f"Saved {len(rows)} items to {OUTPUT_CSV}")

    finally:
        driver.quit()


if __name__ == '__main__':
    main()