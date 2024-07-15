from .base_news_source import BaseNewsSource
from robocorp import log
from datetime import datetime


class GoogleNewsSource(BaseNewsSource):

    def __init__(self,payload):

        name = "Google News"
        url = "https://news.google.com/"
        locators = {
            'search_bar_activator':None,
            'search_bar': '//*[@class="Ax4B8 ZAGvjd"]',
            'search_button': '//*[@class="gb_ve"]',
            'category_container': '//a[@class="brSCsc" and text()="{category_placehoder}"]',
            'search_results': '//article[@class="IFHyqb DeXSAc"]',
            'loading_element':  '//*[@jsname="LbNpof" and @role="progressbar"]',
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

    def filter_category(self):
        log.info("This news source does not allow filtering by category")
        # self.locators['category_container'] = self.locators['category_container'].replace("{category_placehoder}",self.category)

        # try:
        #     self.browser.click_element_when_clickable(self.locators['category_container'])
        # except AssertionError:
        #     raise AssertionError(f"Could not set category '{self.category}' on results page.")

    def run(self):
        self.load_website()
        self.update_date_range()
        self.input_search_term()
        self.filter_category()
        self.scroll(mode="loading_element")

        log.info("Waiting")
        self.browser.wait_until_page_contains_element('//*[@class="gb_rfvesdf"]', timeout=15)
        self.close()