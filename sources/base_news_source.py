from abc import ABC, abstractmethod
from RPA.Browser.Selenium import Selenium, ElementNotFound
from robocorp import log
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time


class BaseNewsSource(ABC):

    BASE_LOCATORS = ['search_bar_activator','search_bar', 'search_button', 'category_container','search_results','loading_element']
    DEFAULT_TIMEOUT = 10
    
    def __init__(self,name,url,locators,payload):

        log.info(f"Instantiating news source {name}")

        self.browser = Selenium()
        self.name = name
        self.url = url
        self.search_term = payload['search_term']
        self.category = payload['category']
        self.months = payload['months']
        self.start_date = self.get_cut_date(self.months)
        self.locators = locators
        self._check_locators()

        self.browser.set_selenium_speed(1)
        self.browser.set_selenium_page_load_timeout(15)


    def _check_locators(self):
        for locator in self.BASE_LOCATORS:
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
    
    def get_cut_date(self,months,whole_month=True):
        #Calculates the first day of the Nth month back. 
        # I'm assuming past months before current one should be considered whole. 
        # If not, call this method parameter 'whole_month' as False.
        # Might be a good idea to also check the max number of months, otherwise 
        # the tasks might take too long to complete for large values. Assuming max = 12.

        try:
            months_int = int(months)
        except:
            raise ValueError("Months parameter should be a valid integer.")
        
        if months_int < 0 or months_int > 12:
            raise ValueError("Months parameter must be greater than or equals 0 and less than or equals 12.")

        if months_int < 1:
            months_int = 1

        start_day = datetime.today() - relativedelta(months=months_int-1)
        
        if whole_month:
            start_day = start_day.replace(day=1)

        log.info(f"Start date for current iteration ({months_int} months): {start_day}")

        return start_day

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
            log.info("Search term inserted.")
        except AssertionError:
            raise ElementNotFound("Search term could not be inserted.")
        
        try:
            self.browser.click_element_when_clickable(self.locators['search_button'],self.DEFAULT_TIMEOUT)
        except AssertionError:
            raise ElementNotFound("Search button could not be found or never became clickable.")
        
        try:
            self.browser.wait_until_page_contains_element(self.locators['search_results'],self.DEFAULT_TIMEOUT)
            log.info("Results page loaded.")
        except AssertionError:
            raise ElementNotFound("Timed out while waiting for results page.")

    @abstractmethod 
    def filter_category(self):
        # Too specific to have a base method.
        pass
    
    def scroll(self,mode="end_element"):
        # Method to handle result pages with infinite scrolling, where 
        # the results are all store on the same page. Has 2 modes:

        # - "end_element" = Assumes no more results are availabe when an end 
        # of list element exists and is visible, like a div with a message "no more results".
        # 
        # - "loading_element" = Assumes no more results are available when a loading visual cue
        #   no longer appears upon scrolling to the bottom, like those spinner thingies.
        
        if mode == "loading_element":
            try:
                while True:
                    self.browser.execute_javascript("window.scrollBy(0, 5000);")
                    
                    self.browser.wait_until_element_is_visible(self.locators['loading_element'],timeout=10)
                    self.browser.wait_until_element_is_not_visible(self.locators['loading_element'],timeout=10)
                #last = self.browser.find_elements(self.locators['search_results'])[-1]
            except Exception as e:
                print(e)

        else:
            raise NotImplementedError("Scroll mode not implemented.")
        
    def parse_results(self):
        
        try:
            self.browser.page_should_contain
        except:
            pass

    def close(self):
        self.browser.close_browser()

