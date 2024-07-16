from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
from . import setup_log

@task
def excel():
    setup_log()
    
    log.info("Excel task started.")
    
    item = workitems.inputs.current
    news_dict = item.payload['news_dict']
    log.info(news_dict)

