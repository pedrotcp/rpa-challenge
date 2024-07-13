from robocorp import log, workitems
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium

@task
def open_browser():
    log.setup_log(
        output_log_level='info',
        output_stream={'info': 'stdout','warn': 'stdout', 'critical': 'stderr'}
    )
    log.info("Capture task started.")
    lib = Selenium()
    lib.open_available_browser("https://google.com")

