from abc import ABC, abstractmethod
from RPA.Browser.Selenium import Selenium, ElementNotFound
from robocorp import log
from datetime import datetime, timedelta


class BaseNewsSource(ABC):

    LOCATORS = ['search_bar_activator','search_bar', 'search_button', 'search_results']
    DEFAULT_TIMEOUT = 10
    
    def __init__(self,name,url,locators,payload):

        log.info(f"Instantiating news source {name}")

        self.browser = Selenium()
        self.name = name
        self.url = url
        self.search_term = payload['search_term']
        self.category = payload['category']
        self.months = payload['months']
        self.locators = locators
        self._check_locators()

    def _check_locators(self):
        for locator in self.LOCATORS:
            if locator not in self.locators:
                raise ValueError(f"Locator missing: {locator}")

    @abstractmethod
    def run(self):
        """
        Each specific news source class should implement this method with the appropiarte calls. 
        
        For instance, Google News enables the search bar by default, while Reuters requires the 
        user to click the magnifying glass before showing the search bar, because why make it easy? 
        """
        pass
    
    def calculate_start_date()

    def load_website(self):
        try:
            self.browser.open_available_browser(self.url)
            log.info("Page loaded")
        except Exception as e:
            log.critical(f"Error navigating to url: {e}")

    def activate_search_bar(self):
        try:
            self.browser.wait_until_page_contains_element(self.locators['search_bar_activator'], timeout=self.DEFAULT_TIMEOUT)
            log.info("Locator search_bar_activator exists.")
        except AssertionError:
            raise ElementNotFound("Locator search_bar_activator could not be found.")

        try:
            self.browser.click_button_when_visible(self.locators['search_bar_activator'])
        except AssertionError:
            raise ElementNotFound("Locator search_bar_activator could bot be clicked because it was not visible.")
    
    def input_search_term(self):

        try:
            self.browser.wait_until_page_contains_element(self.locators['search_bar'], timeout=self.DEFAULT_TIMEOUT)
            log.info("Locator search_bar exists.")
        except AssertionError:
            raise ElementNotFound("Locator search_bar could not be found.")
        
        try:
            self.browser.input_text_when_element_is_visible(self.locators['search_bar'],self.search_term)
            log.info("Search term input.")
        except AssertionError:
            raise ElementNotFound("Search term could not be input.")
            
    def close(self):
        self.browser.close_browser()