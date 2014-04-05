from scrapy.spider import Spider

class FanGraphsSpider(Spider):
    name = "fangraphs"
    allowed_domains = ["www.fangraphs.com"]
    start_urls = [
        'http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=6&season=2014&month=0&season1=2014&ind=0&team=11&rost=0&age=0&filter=&players=0'
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)