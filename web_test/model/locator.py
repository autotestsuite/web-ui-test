from __future__ import annotations

from typing import Callable

from selene import by, be
from selene.support.shared.jquery_style import ss


class LocatorConfig:
    locate_rule: Callable[[str], str] = None

    input_box: Label = (lambda: Label(LocatorConfig.locate_rule, 'input'))
    textarea: Label = (lambda: Label(LocatorConfig.locate_rule, 'textarea'))
    text: Label = (lambda: Label(LocatorConfig.locate_rule, 'span'))
    select: Label = (lambda: Label(LocatorConfig.locate_rule, 'select'))
    button: Label = (lambda: Label(LocatorConfig.locate_rule, 'button'))


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
