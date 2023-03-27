import abc
import dataclasses

from selene import query
from selene.support.shared.jquery_style import ss

from web_test.assist.selenium import new_by
from web_test.common.convert import zip_dict


@dataclasses.dataclass
class FormDataConfig:
    header_locator: tuple = None
    row_locator: tuple = None

    @property
    def form_header(self):
        header = ss(self.header_locator)
        return [field.get(query.text) for field in header]

    def locate_form_row(self, row_keyword):
        return ss(new_by.with_args(self.row_locator, row_keyword))


class FormData(FormDataConfig):

    def build_row_data_dict(self, row_keyword: str) -> dict:
        header = self.form_header
        return (
            zip_dict(header, self.locate_form_row(row_keyword))
            if header
            else None
        )

    def get_element_by_row_keyword_and_column_name(self, row_keyword: str, column_name: str):
        row_data_dict = self.build_row_data_dict(row_keyword)
        return (
            row_data_dict.get(column_name)
            if row_data_dict
            else None
        )


class ABCForm(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def row_keyword_should_be_visible(self, row_keyword): pass

    @abc.abstractmethod
    def row_keyword_should_not_be_visible(self, row_keyword): pass

    @abc.abstractmethod
    def click_row_keyword(self, row_keyword): pass

    @abc.abstractmethod
    def get_column_text_by_row_index(self, row_index, column_name): pass

    @abc.abstractmethod
    def get_column_text_by_row_keyword(self, row_keyword, column_name): pass
