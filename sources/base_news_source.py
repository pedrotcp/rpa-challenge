from abc import ABC, abstractmethod
from RPA.Browser.Selenium import Selenium, ElementNotFound
from robocorp import log

class BaseNewsSource(ABC):

    MANDATORY_LOCATORS = ['search_bar', 'search_button', 'search_results']
    
    def __init__(self, name,url, locators):

        log.info(f"Instantiating news source {name}")

        self.browser = Selenium()
        self.name = name
        self.url = url
        self.locators = locators
        self._check_locators()

    def _check_locators(self):
        for locator in self.MANDATORY_LOCATORS:
            if locator not in self.locators:
                raise ValueError(f"Locator missing: {locator}")

    def load_website(self):
        self.browser.open_available_browser(self.url)

    def close(self):
        self.browser.close_browser()