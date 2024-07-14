from .base_news_source import BaseNewsSource
from datetime import datetime


class GoogleNewsSource(BaseNewsSource):

    def __init__(self,payload):

        name = "Google News"
        url = "https://news.google.com/"
        locators = {
            'search_bar_activator':None,
            'search_bar': '//*[@class="Ax4B8 ZAGvjd"]',
            'search_button': '//*[@class="gb_ve"]',
            'search_results': "//*[@class='search-results']"
        }

        super().__init__(name,url,locators,payload)

    def update_date_range(self):
        # Google news allows you to use a date delta filter together 
        # with the search term, with the following format:
        # "when:XY" where X = number and Y=time unit.
        # I.e.: "inflation" when:20d would return results for the 
        # last 20 days. I could not find any official docs, but 
        # tested with h for hours, d for days and y for years.

        delta = datetime.today() - self.start_date
        date_filter = f" when:{delta.days}d"
        self.search_term = '"' + self.search_term + '"' + date_filter


    def run(self):
        self.load_website()
        self.update_date_range()
        self.input_search_term()
        self.browser.wait_until_page_contains_element('//*[@class="gb_rfvesdf"]', timeout=60)
        self.close()