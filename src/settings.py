# Configuration settings for the Scrapy crawler
import os

BOT_NAME = 'domain_crawler'

SPIDER_MODULES = ['crawler_module']
NEWSPIDER_MODULE = 'crawler_module'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.05

# The download timeout setting
DOWNLOAD_TIMEOUT = 10

# The amount of time (in secs) that the downloader will wait before timing out
DOWNLOAD_TIMEOUT = 10

# The user agent string to use for all requests
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# The maximum depth that will be allowed to crawl for any site
DEPTH_LIMIT = 10

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'crawler_module.DomainPipeline': 300,
}

# Log configuration
LOG_LEVEL = 'DEBUG'  # Can be CRITICAL, ERROR, WARNING, INFO, DEBUG
LOG_FILE = os.path.join(os.getcwd(), 'logs', 'crawler.log')