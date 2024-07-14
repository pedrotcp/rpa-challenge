from .base_news_source import BaseNewsSource


class GoogleNewsSource(BaseNewsSource):

    locators = {}

    def __init__(self):

        name = "Google News"
        url = "https://news.google.com/"
        locators = {
            'search_bar': "//*[@aria-label='Search']",
            'search_button': "//*[@aria-label='Search']",
            'search_results': "//*[@class='search-results']"
        }

        super().__init__(name,url,locators)