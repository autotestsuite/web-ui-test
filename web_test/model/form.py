import abc


class ABCForm(metaclass=abc.ABCMeta):

    def check_row_keyword_visible(self, row_keyword): pass
