from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
from RPA.Excel.Files import Files
from . import setup_log

@task
def excel():
    setup_log()
    
    log.info("Excel task started.")
    item = workitems.inputs.current
    news_dict = item.payload['news_dict']
   
    lib = Files()
    lib.create_workbook(path="output/NewsList.xlsx", fmt="xlsx")
    lib.create_worksheet(name="News",content=news_dict)
    lib.save_workbook()
