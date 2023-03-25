from __future__ import annotations

from selene import browser, by


class Google:

    def open(self) -> Google:
        browser.open('https://google.com/ncr')
        return self

    def search(self, text) -> Google:
        browser.element(by.name('q')).type(text).press_enter()
        return self
