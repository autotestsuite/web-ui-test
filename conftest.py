from typing import List

import allure
import allure_commons
import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from selene import Browser
from selene import browser, support
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

import config
from web_test.assist.allure import report
from web_test.assist.python import monkey
from web_test.assist.selenium.typing import WebDriverOptions
from web_test.assist.webdriver_manager import supported, set_up


@pytest.fixture(scope='session', autouse=True)
def add_reporting_to_selene_steps():
    original_open = Browser.open

    @monkey.patch_method_in(Browser)
    def open(self, relative_or_absolute_url: str):
        return report.step(original_open)(self, relative_or_absolute_url)


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.base_url = config.settings.base_url
    browser.config.timeout = config.settings.timeout
    browser.config.save_page_source_on_failure = (
        config.settings.save_page_source_on_failure
    )
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = _driver_from(config.settings)
    browser.config.hold_browser_open = config.settings.hold_browser_open

    yield

    if not config.settings.hold_browser_open:
        browser.quit()


def _driver_from(settings: config.Settings) -> WebDriver:
    driver_options = _driver_options_from(settings)
    driver = (
        set_up.local(
            name=settings.browser_name,
            options=driver_options,
        )
        if settings.debugging_mode
        else webdriver.Remote(
            command_executor=settings.remote_url,
            options=driver_options
        )
    )

    return driver


def _driver_options_from(settings: config.Settings) -> WebDriverOptions:
    options = None

    if settings.browser_name in [supported.chrome, supported.chromium]:
        options = _chrome_options_from(settings)
    if settings.browser_name == supported.chromium:
        pass
    if settings.browser_name == supported.firefox:
        pass
    if settings.browser_name == supported.ie:
        pass
    if settings.browser_name == supported.edge:
        pass

    if not settings.debugging_mode:
        options.set_capability('enableVNC', settings.remote_enableVNC)
        options.set_capability('enableVideo', settings.remote_enableVideo)
        options.set_capability('enableLog', settings.remote_enableLog)
        options.set_capability('browserName', settings.browser_name)
        options.set_capability('browserVersion', settings.browser_version)
        options.set_capability(
            'selenoid:options', {
                "enableVNC": settings.remote_enableVNC,
                "enableVideo": settings.remote_enableVideo,
                "enableLog": settings.remote_enableLog,
            }
        )

    return options


def _chrome_options_from(settings: config.Settings) -> WebDriverOptions:
    options = webdriver.ChromeOptions()
    if settings.maximize_window:
        options.add_argument('--start-maximized')
    else:
        options.add_argument(f'--window-size={settings.window_width},{settings.window_height}')

    if settings.headless:
        options.add_argument('--headless')

    if settings.incognito:
        options.add_argument('--incognito')

    _arguments: List[str] = [
        '--no-sandbox',
        '--disable-gpu',
        '--disable-notifications',
        '--disable-extensions',
        '--disable-dev-shm-usage',
        '--disable-setuid-sandbox',
        '--ignore-certificate-errors',
        '--hide-scrollbars',
        '--page-load-strategy=normal',
    ]
    for argument in _arguments:
        options.add_argument(argument)

    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    return options


prev_test_screenshot = None
prev_test_page_source = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    yield

    global prev_test_screenshot
    prev_test_screenshot = browser.config.last_screenshot
    global prev_test_page_source
    prev_test_page_source = browser.config.last_page_source


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    outcome = (
        yield
    )

    result = outcome.get_result()

    if result.when == 'call' and result.failed:
        last_screenshot = browser.config.last_screenshot
        if last_screenshot and not last_screenshot == prev_test_screenshot:
            allure.attach.file(
                source=last_screenshot,
                name='screenshot',
                attachment_type=allure.attachment_type.PNG,
            )

        last_page_source = browser.config.last_page_source
        if last_page_source and not last_page_source == prev_test_page_source:
            allure.attach.file(
                source=last_page_source,
                name='page source',
                attachment_type=allure.attachment_type.HTML,
            )
