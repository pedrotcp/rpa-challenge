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
    news_dict_body = item.payload['news_dict']

    news_dict_header ={
        "title":"title",
        "description":"description",
        "date": "date",
        "url" : "url",
        "picture_filename": "picture_filename"
    }

    news_dict = {**news_dict_header, **news_dict_body}
   
    lib = Files()
    lib.create_workbook(path="output/NewsList.xlsx", fmt="xlsx")
    lib.create_worksheet(name="News",content=news_dict)
    lib.save_workbook()
