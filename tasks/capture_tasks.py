from pathlib import Path
from robocorp.tasks import task
from robocorp import log, workitems
from sources.source_factory import get_news_source
from RPA.Browser.Selenium import Selenium,ElementNotFound
from . import setup_log
from .util import check_connection,check_work_items

@task
def capture():
    """
    Instructions
    """
    
    setup_log()
    log.info("Capture task started.")
    check_work_items(workitems)
    check_connection()

    news_source = get_news_source()

    # log.console_message("Page loaded.",kind="stdout")

    # try:
    #     browser.wait_until_page_contains_element("//*[@aria-label='search button']", timeout=10)
    #     log.console_message("Element search button exists.",kind="stdout")
    # except AssertionError:
    #     raise ElementNotFound("Search bar element could not be found.")
    

    # try:
    #     browser.wait_until_element_is_visible("//*[@aria-label='search button']", timeout=10)
    # except AssertionError:
    #     raise ElementNotFound("Search bar element not visible.")

    # # Perform actions on the element, if needed
    # browser.click_element("//*[@aria-label='search button']")


    for item in workitems.inputs:
        log.info(item)
        payload = {
            "Name":"Name"
        }
        workitems.outputs.create(payload)

