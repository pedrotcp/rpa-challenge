from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
from . import setup_log

@task
def excel():
    setup_log()
    log.info("Excel task started.")
    lib = Selenium()
    lib.open_available_browser("https://apple.com")
    for item in workitems.inputs:
        print(item)
        workitems.outputs.create(item)

