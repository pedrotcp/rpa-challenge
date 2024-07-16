from .base_news_source import BaseNewsSource
from robocorp import log
from datetime import datetime


class GoogleNewsSource(BaseNewsSource):

    def __init__(self,payload,headless):

        name = "Google News"
        url = "https://news.google.com/"
        locators = {
            'search_bar_activator': None,
            'search_bar': '//*[@class="Ax4B8 ZAGvjd"]',
            'search_button': '//*[@class="gb_ve"]',
            'category_container': '//a[@class="brSCsc" and text()="{category_placehoder}"]',
            'news_element': '//article[@class="IFHyqb DeXSAc"]',
            'loading_element':  '//*[@jsname="LbNpof" and @role="progressbar"]',
            'title': '//a[@class="JtKRv"]', 
            'description': None,
            'date': '//time[@class="hvbAAd"]',
            'picture_url': '//img[@class="Quavad vwBmvb"]',
        }

        super().__init__(name,url,locators,payload,headless)

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

    def parse_results(self):
        
        if not self.news_element_list:
            raise ValueError("News list is empty.")
        
        for news_element in self.news_element_list:
            try:
                title = self.browser.find_element(self.locators['title'],news_element).get_attribute('text') #if self.locators['title'] is not None else ''
                description = self.browser.get_element_attribute(self.browser.find_element(self.locators['title'],news_element),"text")
                date = self.browser.find_element(self.locators['date'],news_element).get_attribute('datetime') if self.locators['date'] is not None else ''
                picture = self.browser.find_element(self.locators['picture_url'],news_element).get_attribute('srcset') if self.locators['picture_url'] is not None else ''

                print(f"title:{title}")
                print(f"description:{description}")


                self.news_parsed_dict.append({
                    "title":title,
                    "description":description,
                    "date":date,
                    "picture_url":picture
                })
                    
            except Exception as e:
                log.warn(f"Error while parsing news element: {e}")

            print(self.news_parsed_dict)

    def run(self):
        self.load_website()
        self.update_date_range()
        self.input_search_term()
        self.filter_category()
        self.scroll(mode="loading_element")
        self.capture_news()
        #self.parse_results()

        log.info("Waiting")
        #self.browser.wait_until_page_contains_element('//*[@class="gb_rfvesdf"]', timeout=5)
        self.close()