import scrapy

class SearchSpider(scrapy.Spider):
    name = "search_spider"

    def start_requests(self):
        search_query = ""
        url = f"https://www.google.com/search?q={search_query}"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract URLs from search results
        links = response.css('div.yuRUbf a::attr(href)').extract()
        num_results = 20  # Set the number of results you want
        result_urls = links[:num_results]
        print(result_urls)

# To run the spider, you can use the following command in your terminal:
# scrapy runspider your_spider_file.py
