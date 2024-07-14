from .base_news_source import BaseNewsSource


class ReutersSource(BaseNewsSource):
   
    def __init__(self,payload):

        name = "Reuters"
        url = "https://reuters.com/"
        locators = {
            'search_bar_activator':None,
            'search_bar': '//*[@class="Ax4B8 ZAGvjd"]',
            'search_button': '//*[@class="gb_ve"]',
            'search_results': "//*[@class='search-results']"
        }

        super().__init__(name,url,locators,payload)
    
    def run(self):
        self.load_website()
        self.input_search_term()

        self.close()