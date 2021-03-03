import json
import os
import shutil

import scrapy
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "community"

    def start_requests(self):
        urls = [
            'https://placeholder.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Function grabs full html of page."""
        filename = 'homepage.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # copy html file
        pwd = os.getcwd()
        project_dir = os.path.dirname(pwd) 
        source_file_path = f"{project_dir}\serato\{filename}"
        # using double slashes to escape for proper file path
        dest_file_path = f"{project_dir}\\templates\copy.html"
        shutil.copyfile(source_file_path, dest_file_path)