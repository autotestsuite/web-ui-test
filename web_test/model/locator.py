from __future__ import annotations

from typing import Callable

from selene import by, be
from selene.support.shared.jquery_style import ss


class LocatorConfig:
    locate_function: Callable[[str], str] = None

    def behind_label(self, label_value):
        return self.s_behind_label(label_value).element_by(be.clickable)

    def s_behind_label(self, label_value):
        elements = ss(by.xpath(f'{self.locate_function(label_value)}//{self.tag}'))
        elements.matching(be.visible)
        return elements

    def __getattr__(self, tag: str):
        self.tag = tag
        return self
