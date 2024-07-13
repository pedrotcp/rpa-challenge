from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium

@task
def open_browser():
    """Insert the sales data for the week and export it as a PDF"""
    lib = Selenium()

    lib.open_available_browser("https://google.com")

