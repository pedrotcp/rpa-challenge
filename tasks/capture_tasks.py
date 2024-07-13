from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium

@task
def capture():
    log.setup_log()
    log.info("Capture task started.")
    lib = Selenium()
    lib.open_available_browser("https://google.com")

