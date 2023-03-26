from __future__ import annotations

from selene import browser, by, have

from web_test.assist.allure.report import step


class Google:

    def __init__(self):
        self.results = browser.all('#search .g')

    @step()
    def open(self) -> Google:
        browser.open('https://google.com/ncr')
        return self

    @step()
    def search(self, text) -> Google:
        browser.element(by.name('q')).type(text).press_enter()
        return self

    @step()
    def should_have_result(self, index, text) -> Google:
        self.results[index].should(have.text(text))
        return self

    @step()
    def should_have_results_amount_at_least(self, number) -> Google:
        self.results.should(have.size_greater_than_or_equal(number))
        return self
