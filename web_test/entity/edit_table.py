from typing import Callable

from loguru import logger
from selene import be, by, query
from selene.core.exceptions import TimeoutException
from selene.support.shared.jquery_style import s, ss
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.select import Select

from web_test.assist.selenium import new_by
from web_test.model.locator import LocatorConfig


class EditTable(LocatorConfig):
    locate_rule: Callable[[str], str] = None

    select_option: tuple = None

    def input_text_after_label(self, label, text):
        logger.info(f'输入{label}的内容：{text}')
        self.input_box.behind_label(label).click().clear().type(text)
        return self

    def input_long_text_after_label(self, label, long_text):
        logger.info(f'输入{label}的内容：{long_text}')
        self.textarea.behind_label(label).click().clear().type(long_text)
        return self

    def click_checkbox_after_label(self, label):
        logger.info(f'点击{label}多选框')
        self.input_box.behind_label(label).click()
        return self

    def input_text_after_label_and_select_self(self, label, text):
        logger.info(f'输入{label}的内容并选择：{text}')
        self.input_text_after_label(label, text)
        s(new_by.with_args(self.select_option, text)).should(be.clickable).click()
        return self

    def input_text_after_label_and_select_option(self, label, text, option):
        logger.info(f'输入{label}的内容{text}并选择：{option}')
        self.input_text_after_label(label, text)
        s(new_by.with_args(self.select_option, option)).should(be.clickable).click()
        return self

    def click_input_box_after_label_and_select_option(self, label, option):
        logger.info(f'点击{label}的内容并选择：{option}')
        self.input_box.behind_label(label).click()
        s(new_by.with_args(self.select_option, option)).should(be.clickable).click()
        return self

    def click_button_after_label(self, label):
        logger.info(f'点击{label}的按钮')
        self.button.behind_label(label).click()
        return self

    def select_dropdown_menu_after_label(self, label, option):
        logger.info(f'选择{label}的下拉菜单：{option}')
        Select(self.select.behind_label(label).locate()).select_by_visible_text(option)
        return self

    def click_button(self, button_text):
        logger.info(f'点击{button_text}按钮')
        elements = ss(
            new_by.with_args(by.xpath('//button[translate(normalize-space(), " ", "")="{}"]'), button_text)

        )
        clicked = False
        try:
            elements.element_by(be.clickable).click()
            clicked = True
        except TimeoutException:
            for element in elements.locate():
                try:
                    element.click()
                    clicked = True
                    break
                except ElementClickInterceptedException:
                    continue
        if not clicked:
            raise ElementClickInterceptedException
        return self

    def get_text_after_label(self, label):
        text = self.text.behind_label(label).get(query.text)
        logger.info(f'获取{label}的内容：{text}')
        return text
