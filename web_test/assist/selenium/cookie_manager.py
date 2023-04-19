from selene import Browser


def current_browser_cookie(browser: Browser):
    """
    获取当前浏览器的cookie

    :param browser: 浏览器对象
    :return: cookie
    """
    cookies = browser.config.driver.get_cookies()

    cookies_dict = {}

    for cookie in cookies:
        cookies_dict[cookie['name']] = cookie['value']

    cookie_val = '; '.join([f"{name}={value}" for name, value in cookies_dict.items()])
    return cookie_val
