import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scrapy.crawler import CrawlerProcess
from input_module import load_urls_from_csv, load_urls_from_txt
from crawler_module import DomainCrawler
from settings import *
import os

def ensure_log_directory():
    """ Ensure the log directory exists. """
    log_dir = os.path.join(os.getcwd(), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def get_input_urls(input_type, input_path):
    """ Load URLs from the specified input file based on the input type. """
    if input_type == 'csv':
        try:
            urls = load_urls_from_csv(input_path)
            return urls
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
    elif input_type == 'txt':
        try:
            urls = load_urls_from_txt(input_path)
            return urls
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(e)
        except ValueError as e:
            print(e)
    else:
        print("Unsupported input type.")
        sys.exit(1)

def main():
    # Gather user input for configuration
    input_type = input("Enter input type (csv/txt): ")
    output_type = input("Enter output type (csv/jsonl/html): ")
    input_path = input("Enter path to input file: ")
    output_path = input("Enter path to output file/directory: ")
    ensure_log_directory()

    # Load URLs from the specified input
    urls = get_input_urls(input_type, input_path)

    # Set up the Scrapy crawler process with settings from settings.py
    process = CrawlerProcess(settings={
        'BOT_NAME': BOT_NAME,
        'USER_AGENT': USER_AGENT,
        'DOWNLOAD_DELAY': DOWNLOAD_DELAY,
        'DOWNLOAD_TIMEOUT': DOWNLOAD_TIMEOUT,
        'DEPTH_LIMIT': DEPTH_LIMIT,
        'CONCURRENT_REQUESTS': CONCURRENT_REQUESTS,
        'ROBOTSTXT_OBEY': ROBOTSTXT_OBEY,
        'COOKIES_ENABLED': COOKIES_ENABLED,
        'ITEM_PIPELINES': ITEM_PIPELINES,
        'LOG_LEVEL': LOG_LEVEL,
        'LOG_FILE': LOG_FILE
    })

    # Start the crawler with the given URLs and output settings
    process.crawl(DomainCrawler, domains=urls, output_type=output_type, output_path=output_path)
    process.start()

if __name__ == "__main__":
    main()
