
from robocorp.tasks import task
from robocorp import log, workitems
from sources.source_factory import get_news_source
from . import setup_log
from .util import check_connection,check_work_item


@task
def capture():
    
    setup_log()
    log.info("'Capture News' task started.")
    check_connection()
     
    #This loop can run only once, because after an item is reserved and released, it cannot be accessed anymore? (Check docs) 
    for item in workitems.inputs: 
        check_work_item(item)
        news_source = get_news_source(item.payload,headless=True)
        news_dict,term = news_source.run()
        workitems.outputs.create(payload={"news_dict":news_dict,"search_term":term})

