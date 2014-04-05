from scrapy.spider import Spider

from fangraphs.items import *

import sys

class FanGraphsSpider(Spider):
    name = "fangraphs"
    allowed_domains = ["www.fangraphs.com"]
    start_urls = [
        'http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=6&season=2014&month=0&season1=2014&ind=0&team=11&rost=0&age=0&filter=&players=0'
    ]

    def parse(self, response):
        with open('FOO.txt', 'wb') as fh:
            fh.write("PARSING RESPONSE")
        return

        sel = Selector(response)
        cells =  sel.xpath("//td[@class='grid_line_regular']")

        def next_string():
            cell = cells.next()
            return cell.xpath('text()').extract()

        def next_float():
            cell = cells.next()
            return float(cell.xpath('text()').extract())

        def next_link_text():
            cell = cells.next()
            return cell.xpath('a/text()').extract()

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

                item = FangraphsItem()
                item['name'] = name
                item['rar'] = rar
                out.append(item)

            except StopIteration:
                return out
