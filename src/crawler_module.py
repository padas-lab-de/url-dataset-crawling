import scrapy
import os
from hashlib import md5
from output_module import save_to_csv, save_to_jsonl, save_html_content

class DomainCrawler(scrapy.Spider):
    """
    A Scrapy Spider for crawling domains and saving data in various formats.
    
    Attributes:
        domains (list): A list of domain URLs to crawl.
        output_type (str): The format of the output ('csv', 'jsonl', 'html').
        output_path (str): The base path where the output should be saved.
    """
    name = "domain_crawler"

    def __init__(self, domains, output_type, output_path):
        """
        Initialize the spider with domain list, output type, and output path.
        
        Args:
            domains (list): List of domains to crawl.
            output_type (str): Type of output to generate.
            output_path (str): Path where the output should be saved.
        """
        super().__init__()
        self.domains = domains
        self.output_type = output_type
        self.output_path = output_path
        self.data_collected = []

    def start_requests(self):
        """Generates Scrapy Requests for each domain in the list."""
        for domain in self.domains:
            if not domain.startswith('http://') and not domain.startswith('https://'):
                domain = f"http://{domain}"
            yield scrapy.Request(domain, self.parse, errback=self.handle_error)

    def parse(self, response):
        """
        Handle the response downloaded for each of the requests made.
        
        Args:
            response (scrapy.http.Response): The response received from the server.
        """
        uid = self.generate_uid(response.url)
        data = {
            'url': response.url,
            'html': response.text,
            'uid': uid
        }
        self.data_collected.append(data)

        # Dispatch to appropriate output handling based on the specified output type
        if self.output_type == 'csv':
            save_to_csv([data], self.output_path)
        elif self.output_type == 'jsonl':
            save_to_jsonl([data], self.output_path)
        elif self.output_type == 'html':
            save_html_content([data], os.path.dirname(self.output_path), self.output_path)

    def handle_error(self, failure):
        """
        Handle any errors that occur while making HTTP requests.
        
        Args:
            failure (twisted.python.failure.Failure): The error encountered.
        """
        self.logger.error(f"Error crawling {failure.request.url}: {failure.value}")

    def close(self, reason):
        """
        Perform cleanup operations when the spider closes.
        
        Args:
            reason (str): The reason why the spider was closed.
        """
        if self.output_type == 'html':
            index_csv = os.path.join(os.path.dirname(self.output_path), 'index.csv')
            save_to_csv(self.data_collected, index_csv)

    def generate_uid(self, url):
        """
        Generate a unique identifier for a given URL.
        
        Args:
            url (str): The URL to generate a UID for.
        
        Returns:
            str: A unique identifier based on the URL.
        """
        # Create a UID based on a hash of the URL
        return md5(url.encode('utf-8')).hexdigest()
