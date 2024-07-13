from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium

@task
def excel():
    log.info("Excel task started.")
    lib = Selenium()
    lib.open_available_browser("https://apple.com")

