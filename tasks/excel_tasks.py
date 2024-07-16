from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
from RPA.Excel.Files import Files
from . import setup_log
import re

@task
def excel():
    setup_log()
    
    log.info("Excel task started.")
    item = workitems.inputs.current
    news_dict_body = item.payload['news_dict']
    term = item.payload['search_term']

    news_dict_header = {
        "title":"title",
        "description":"description",
        "date": "date",
        "url" : "url",
        "picture_filename": "picture_filename"
    }
    # Add headers

    if isinstance(news_dict_body, list) and all(isinstance(d, dict) for d in news_dict_body):
        news_dict = [news_dict_header] + news_dict_body
    else:
        log.error("news_dict_body is not a list of dictionaries.")
        news_dict = [news_dict_header]

    for article in news_dict:
        if article['title'] == 'title':
            article['count'] = 'count'
            article['contains_amount'] = 'contains_amount'
        else:
            article['count'] = article['title'].count(term) + article['description'].count(term)
            article['contains_amount'] = count_terms(article['title'],article['description'])

    
   
    lib = Files()
    lib.create_workbook(path="output/NewsList.xlsx", fmt="xlsx")
    lib.create_worksheet(name="News",content=news_dict)
    lib.save_workbook()
    lib.delete_columns("D")
    lib.save_workbook()
    lib.delete_columns("G")
    lib.save_workbook()
    
def count_terms(title,description):
    regex_money = re.compile(r'\$\d{1,3}(,\d{3})*(\.\d{2})?|(\d+(\.\d{1,2})?\s?(dollars|USD))', re.IGNORECASE)

    return bool(regex_money.search(title) or regex_money.search(description))
