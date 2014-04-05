# Scrapy settings for fangraphs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fangraphs'

SPIDER_MODULES = ['fangraphs.spiders']
NEWSPIDER_MODULE = 'fangraphs.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fangraphs (+http://www.yourdomain.com)'
