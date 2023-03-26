from typing import Dict, Callable, Optional

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager

from web_test.assist.selenium.typing import WebDriverOptions
from web_test.assist.webdriver_manager import supported

installers: Dict[
    supported.BrowserName,
    Callable[[Optional[WebDriverOptions]], WebDriver]
] = {
    supported.chrome:
        lambda opts: webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=opts,
        ),
    supported.chromium:
        lambda opts: webdriver.Chrome(
            service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
            options=opts,
        ),
    supported.firefox:
        lambda opts: webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=opts,
        ),
    supported.ie:
        lambda opts: webdriver.Ie(
            service=Service(IEDriverManager().install()),
            options=opts,
        ),
    supported.edge:
        lambda ____: webdriver.Edge(
            service=Service(EdgeChromiumDriverManager().install()),
        )
}


def local(
        name: supported.BrowserName = 'chrome',
        options: WebDriverOptions = None
) -> WebDriver:
    return installers[name](options)
