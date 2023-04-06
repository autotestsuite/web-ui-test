from __future__ import annotations

from selene import query, Collection, have, by, browser, be
from selene.support.shared.jquery_style import s

from web_test.common.convert import zip_dict


class FormTable:
    thead: Collection = None
    tbody: Collection = None

    @property
    def ths(self):
        return [th.get(query.text) for th in self.thead]

    def get_row_attribute_by_index(self, index, attribute):
        td = zip_dict(
            self.ths,
            self.tbody.element(index).all(by.xpath('*'))
        ).get(attribute)
        return td.get(query.text)

    def get_row_attribute_by_text(self, text, attribute):
        td = zip_dict(
            self.ths,
            self.tbody.by(have.text(text)).all(by.xpath('*'))
        ).get(attribute)
        return td.get(query.text)

    def should_have_size_at_least(self, amount) -> FormTable:
        self.tbody.should(have.size_greater_than_or_equal(amount))
        return self

    def should_have_text(self, text) -> FormTable:
        s(by.text(text)).should(be.visible)
        return self

    def should_have_text_by_index(self, index, text) -> FormTable:
        self.tbody.element(index).should(have.text(text))
        return self

    def should_have_row_attribute(self, text, name, value) -> FormTable:
        td = zip_dict(
            self.ths,
            self.tbody.by(have.text(text)).all(by.xpath('*'))
        ).get(name)

        def fn(entity):
            actual_value = td.get(query.text) if td else ...
            if actual_value != value:
                raise AssertionError(
                    f'row attribute was wrong:'
                    f'\texpected: {value}'
                    f'\t  actual: {actual_value}'
                )

        browser.wait.for_(fn)
        return self

    def should_have_text_and_display_color(self, text, color):
        self.tbody.by(have.text(text)).should(have.css_property('color', color))
        return self
