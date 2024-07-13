from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium

@task
def open_browser():
    log.info("Images task started.")
    lib = Selenium()
    lib.open_available_browser("https://microsoft.com")

