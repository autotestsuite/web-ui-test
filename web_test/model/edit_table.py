import abc


class ABCEditTable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def input_text_after_label(self, label, text): pass

    @abc.abstractmethod
    def input_long_text_after_label(self, label, long_text): pass

    @abc.abstractmethod
    def input_text_after_label_and_select_self(self, label, text): pass

    @abc.abstractmethod
    def input_text_after_label_and_select_option(self, label, text, option): pass

    @abc.abstractmethod
    def click_input_box_after_label_and_select_option(self, label, option): pass

    @abc.abstractmethod
    def click_button_after_label(self, label): pass

    @abc.abstractmethod
    def click_button(self, button_text): pass
