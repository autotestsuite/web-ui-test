from loguru import logger
from selene import by, be, query
from selene.support.shared.jquery_style import s

from web_test.model.form import ABCForm, FormData


class FormEntity(ABCForm):
    header_locator: tuple = None

    row_locator_by_index: tuple = None

    row_locator_by_keyword: tuple = None

    def __init__(self):
        self.form_data_by_index = FormData(self.header_locator, self.row_locator_by_index)
        self.form_data_by_keyword = FormData(self.header_locator, self.row_locator_by_keyword)

    def check_row_keyword_visible(self, row_keyword):
        visible = s(by.text(row_keyword)).wait_until(be.visible)
        logger.info(f'检查表单信息{row_keyword}是否可见：{visible}')
        return visible

    def click_row_keyword(self, row_keyword):
        logger.info(f'点击{row_keyword}的信息')
        s(by.text(row_keyword)).should(be.clickable).click()
        return self

    def get_column_text_by_row_index(self, row_index, column_name):
        element = self.form_data_by_index.get_element_by_row_keyword_and_column_name(row_index, column_name)
        column_text = element.should(be.visible).get(query.text) if element else None
        logger.info(f'获取指定行索引{row_index}的指定列名{column_name}的值：{column_text}')
        return column_text

    def get_column_text_by_row_keyword(self, row_keyword, column_name):
        element = self.form_data_by_keyword.get_element_by_row_keyword_and_column_name(row_keyword, column_name)
        column_text = element.should(be.visible).get(query.text) if element else None
        logger.info(f'获取指定行关键字{row_keyword}的指定列名{column_name}的值：{column_text}')
        return column_text
