from typing import Callable

from selene import by, be
from selene.support.shared.jquery_style import ss


class LocatorConfig:
    locate_rule: Callable[[str], str] = None

    def get_element(self, tag):
        return self.Label(self.locate_rule, tag)

    @property
    def input_box(self):
        return self.get_element('input')

    @property
    def select(self):
        return self.get_element('select')

    @property
    def textarea(self):
        return self.get_element('textarea')

    @property
    def text(self):
        return self.get_element('span')

    @property
    def button(self):
        return self.get_element('button')

    class Label:

        def __init__(self, locate_function: Callable[[str], str], tag: str):
            self.locate_function = locate_function
            self.tag = tag

        def behind_label(self, label_value):
            by_, value = by.text(label_value)
            xpath = f'{self.locate_function(value)}//{self.tag}'
            return ss(by.xpath(xpath)).element_by(be.clickable)

        def s_behind_label(self, label_value):
            by_, value = by.text(label_value)
            xpath = f'{self.locate_function(value)}//{self.tag}'
            return ss(by.xpath(xpath))
