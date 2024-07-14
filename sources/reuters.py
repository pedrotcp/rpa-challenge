from .base_news_source import BaseNewsSource


class ReutersSource(BaseNewsSource):

    def __init__(self):

        url = "https://reuters.com/"

        locators = {
            'search_bar': "//*[@aria-label='Search']",
            'search_button': "//*[@aria-label='Search']",
            'search_results': "//*[@class='search-results']"
        }

        super().__init__(url, locators)