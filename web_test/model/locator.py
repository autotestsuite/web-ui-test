from __future__ import annotations

from typing import Callable

from selene import by, be
from selene.support.shared.jquery_style import ss


class LocatorConfig:
    locate_function: Callable[[str], str] = None

    def behind_label(self, label_value):
        by_, value = by.text(label_value)
        xpath = f'{self.locate_function(value)}//{self.tag}'
        return ss(by.xpath(xpath)).element_by(be.clickable)

    def s_behind_label(self, label_value):
        by_, value = by.text(label_value)
        xpath = f'{self.locate_function(value)}//{self.tag}'
        return ss(by.xpath(xpath))

    def __getattr__(self, tag: str):
        self.tag = tag
        return self
