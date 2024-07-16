from .base_news_source import BaseNewsSource
from RPA.Browser.Selenium import ElementNotFound
from robocorp import log
from datetime import datetime,timezone
import math



class LosAngelesTimesSource(BaseNewsSource):

    def __init__(self,payload,headless):

        name = "Los Angeles Times"
        url = "https://www.latimes.com/"
        
        locators = {
            'search_bar_activator'  : '//button[@data-element="search-button"]',
            'search_bar'            : '//input[@data-element="search-form-input"]',
            'search_button'         : '//button[@data-element="search-submit-button"]',
            'see-all'               : '//span[@class="see-all-text"]',
            'category_container'    : '//ul[@class="search-filter-menu" and @data-name="Topics"]',
            'sort_container'        : '//select[@class="select-input"]',
            'sort_option'           : 'xpath:(//select[@class="select-input"])/option[1]',
            'news_element'          : '//div[@class="promo-wrapper"]',
            'loading_element'       : None,
            'title'                 : '[{i}]/div[@class="promo-content"]/div[@class="promo-title-container"]/h3/a', 
            'description'           : '[{i}]/div[@class="promo-content"]/p[@class="promo-description"]',
            'date'                  : '[{i}]/div[@class="promo-content"]/p[@class="promo-timestamp"]',
            'picture_url'           : '[{i}]/div[@class="promo-media"]/a/picture/img',
            'modal_dismiss'         : '//div[@class="met-container "]//a[@class="met-flyout-close"]',
            'total_results'         : '//span[@class="search-results-module-count-mobile"]'
        }

        super().__init__(name,url,locators,payload,headless)

    def filter_category(self):
        
        self.dismiss_modal()

        try:
            self.browser.scroll_element_into_view(self.locators['see-all'])
            self.dismiss_modal()
            self.browser.click_element_when_clickable(self.locators['see-all'],self.default_timeout)
            self.browser.click_element_when_clickable(self.locators['category_container'] + f'//span[text()="{self.category}"]',self.default_timeout)
        except:
            raise ElementNotFound(f"Error on selecting news category: {self.category}")

    def sort_results(self):
         
        try:
            url = self.browser.get_location().replace("s=0","s=1&p=1")
            self.browser.go_to(url)
            log.info("Results sorted by newest.")
        except:
            raise ElementNotFound(f"Error on sorting news results: {self.category}")

    def next_page(self,current_page):
        try:
            url = self.browser.get_location().replace(f"s=1&p={current_page}",f"s=1&p={current_page + 1}")
            self.browser.go_to(url)
        except:
            raise ElementNotFound(f"Error on changing page.")
    
    def is_date_invalid(self,article_date_str):
        try:
            epoch_time = math.floor(int(article_date_str)/ 1000)
            article_date = datetime.fromtimestamp(epoch_time, tz=timezone.utc)
            return article_date < self.start_date
        
        except (ValueError, TypeError, OSError) as e:
            raise ValueError(f"Date conversion error: {e}")

    def parse_results(self):
        
        self.dismiss_modal()

        try:
            self.news_element_list = self.browser.find_elements(self.locators['news_element'])
            self.total_results = int(self.browser.find_element(self.locators['total_results']).get_attribute("innerHTML").replace(" results","").replace(",",""))
        except ElementNotFound as e:
            log.warn(f"No news container elements were found: {e}")
        except Exception as e:
            log.critical(f"The following exception was found when trying to capture the news list: {e}")
        log.info(f"Total results: {self.total_results}\n")

        done = False
        for page in range(1,math.ceil(self.total_results/10) + 1):
            for index in range(1,len(self.news_element_list) + 1):
                xpath_title =       ("xpath:("+self.locators['news_element'] +")"+ self.locators['title']).replace("{i}",str(index))
                xpath_description = ("xpath:("+self.locators['news_element'] +")"+ self.locators['description']).replace("{i}",str(index))
                xpath_date =        ("xpath:("+self.locators['news_element'] +")"+ self.locators['date']).replace("{i}",str(index))
                xpath_picture =     ("xpath:("+self.locators['news_element'] +")"+ self.locators['picture_url']).replace("{i}",str(index))

                title = (lambda: self.browser.find_element(xpath_title).get_attribute('text') if True else None)() if (lambda: True)() else None
                description = (lambda: self.browser.find_element(xpath_description).get_attribute("innerHTML") if True else None)() if (lambda: True)() else None
                date = (lambda: self.browser.find_element(xpath_date).get_attribute('data-timestamp') if True else None)() if (lambda: True)() else None
                picture_url = (lambda: self.browser.find_element(xpath_picture).get_attribute('src') if True else None)() if (lambda: True)() else None
   
                if self.is_date_invalid(date):
                    done = True
                    break
                    
                self.news_parsed_dict.append({
                    "title":title,
                    "description":description,
                    "date": datetime.datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d'),
                    "picture_url":picture_url
                })
            
            if done:
                break

            self.next_page(page)
 
    def run(self):
        self.load_website()
        self.activate_search_bar()
        self.input_search_term()
        self.filter_category()
        self.sort_results()
        self.parse_results()
        self.download_images()
        self.close()

        return self.news_parsed_dict