import allure
from selene import browser
from selene.core.exceptions import TimeoutException


def attach_snapshots_on_failure(error: TimeoutException) -> Exception:
    last_screenshot = browser.config.last_screenshot
    if last_screenshot:
        allure.attach.file(source=last_screenshot,
                           name='screenshot on failure',
                           attachment_type=allure.attachment_type.PNG)

    last_page_source = browser.config.last_page_source
    if last_page_source:
        allure.attach.file(source=last_page_source,
                           name='page source on failure',
                           attachment_type=allure.attachment_type.HTML)
    return error
