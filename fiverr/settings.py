# Scrapy settings for joaki project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "fiverr"

SPIDER_MODULES = ["fiverr.spiders"]
NEWSPIDER_MODULE = "fiverr.spiders"


FEEDS = {
    'C:/PROYECTO/output.csv': {
        'format': 'csv',
        'overwrite': True,
    },
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "joaki (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)

# CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:

# CONCURRENT_REQUESTS_PER_DOMAIN = 16


# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)

COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS ={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9'}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "joaki.middlewares.JoakiSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "joaki.middlewares.JoakiDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}



DOWNLOADER_MIDDLEWARES = {
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620
}


# pongo esto en el archivo settings.py


ROTATING_PROXY_LIST_PATH = 'joako.txt'


# RANDOMIZE_DOWNLOAD_DELAY = True

# DOWNLOAD_DELAY = 0.1

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html


ITEM_PIPELINES = {
   "fiverr.pipelines.FiverrPipeline": 300,
}

DOWNLOAD_TIMEOUT = 30

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html

# AUTOTHROTTLE_ENABLED = True

# The initial download delay

# AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies

# AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server


# AUTOTHROTTLE_TARGET_CONCURRENCY = 10

RETRY_ENABLED = True

# DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

# CONCURRENT_REQUESTS_PER_DOMAIN = 4
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

RETRY_TIMES = 5  
RETRY_HTTP_CODES = [500, 502, 503, 504, 403, 407, 408]

LOG_LEVEL = 'DEBUG'