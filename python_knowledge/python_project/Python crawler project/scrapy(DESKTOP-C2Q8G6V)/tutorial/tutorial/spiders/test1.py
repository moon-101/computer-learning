import scrapy
class Test1BookSpider(scrapy.Spider):
    name="test1"
    start_urls=["https://www.d21d965.top/index/39520/5.html"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chapter_count = 0
        self.max_chapters = 10

    def parse(self,response):
        if self.chapter_count >= self.max_chapters:
            return
        self.chapter_count += 1
        filename=response.css("h1.wap_none::text").get()
        content = response.css("div#chaptercontent::text").getall()
        # 合并所有段落
        content = "\n".join(content)
        yield {'filename':f"{filename}.txt",'content':content}

        next_chapter= response.css("div.Readpage.pagedown a::attr(href)").getall()[2]
        self.logger.info(f"next_chapter: {next_chapter}")
        
        if next_chapter:
            next_chapter_url = response.urljoin(next_chapter)
            yield scrapy.Request(next_chapter_url, callback=self.parse)

