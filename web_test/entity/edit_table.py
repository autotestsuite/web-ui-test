from typing import Callable

from selene import be, by
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.support.select import Select

from web_test.assist.selenium import new_by
from web_test.model.locator import LocatorConfig


class EditTable(LocatorConfig):
    locate_rule: Callable[[str], str] = None

    select_option: tuple = None

    def input_text_after_label(self, label, text):
        self.input_box.behind_label(label).click().clear().type(text)
        return self

    def input_long_text_after_label(self, label, long_text):
        self.textarea.behind_label(label).click().clear().type(long_text)
        return self

    def input_text_after_label_and_select_self(self, label, text):
        self.input_text_after_label(label, text)
        s(new_by.with_args(self.select_option, text)).should(be.clickable).click()
        return self

    def input_text_after_label_and_select_option(self, label, text, option):
        self.input_text_after_label(label, text)
        s(new_by.with_args(self.select_option, option)).should(be.clickable).click()
        return self

    def click_input_box_after_label_and_select_option(self, label, option):
        self.input_box.behind_label(label).click()
        s(new_by.with_args(self.select_option, option)).should(be.clickable).click()
        return self

    def click_button_after_label(self, label):
        self.button.behind_label(label).click()
        return self

    def select_dropdown_menu_after_label(self, label, option):
        Select(self.select.behind_label(label).locate()).select_by_visible_text(option)
        return self

    def click_button(self, button_text):
        ss(
            new_by.with_args(by.xpath('//button//*[translate(normalize-space(), " ", "")="{}"]'), button_text)

        ).element_by(be.clickable).click()
        return self
