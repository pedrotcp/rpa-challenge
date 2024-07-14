from pathlib import Path
from robocorp import log, workitems
from robocorp.tasks import task, get_output_dir
from RPA.Browser.Selenium import Selenium
from . import setup_log

@task
def capture():
    """
    Instructions
    """
    output = get_output_dir() 
    setup_log()
    log.info("Capture task started.")
    lib = Selenium()
    lib.open_available_browser("https://google.com")
    for item in workitems.inputs:
        print(item)
        workitems.outputs.create(item)

