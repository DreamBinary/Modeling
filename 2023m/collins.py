import scrapy


class CollinsSpider(scrapy.Spider):
    name = "collins"
    allowed_domains = ["www.collinsdictionary.com"]
    start_urls = ["http://www.collinsdictionary.com/"]

    def parse(self, response):

        xpath_parse = response.xpath("/html/body/main/div[3]/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/span")
        print(xpath_parse)
