from scrapy.spider import Spider
from scrapy.selector import Selector

from fangraphs.items import *

class FanGraphsSpider(Spider):
    name = "fangraphs"
    allowed_domains = ["www.fangraphs.com"]
    start_urls = [
        'http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=6&season=2014&month=0&season1=2014&ind=0&team=11&rost=0&age=0&filter=&players=0'
    ]

    def parse(self, response):
        sel = Selector(response)
        cells =  sel.xpath("//td[@class='grid_line_regular' or @class='grid_line_break']")
        it = iter(cells)

        def next_string():
            s = it.next().xpath('text()').extract()[0]
            return s

        def next_float():
            s = next_string().strip()
            if s:
                return float(s)
            else:
                return 0.0

        def next_link_text():
            s = it.next().xpath('a/text()').extract()[0]
            return s

        out = []

        while True:
            try:
                idx = next_float()
                name = next_link_text()
                batting = next_float()
                base_running = next_float()
                fielding = next_float()
                positional = next_float()
                offense = next_float()
                defense = next_float()
                league = next_float()
                replacement = next_float()
                rar = next_float()
                war = next_float()
                dollars = next_string()

                print name, rar
                item = FangraphsItem()
                item['name'] = name
                item['rar'] = rar
                out.append(item)

            except StopIteration:
                return out

