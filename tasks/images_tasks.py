from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
from . import setup_log

@task
def images():
    setup_log()
    log.info("Images task started.")
    lib = Selenium()
    lib.open_available_browser("https://microsoft.com")
    for item in workitems.inputs:
        log.info(item)

