from typing import Optional, Any

from selene import browser


class Assert:

    @staticmethod
    def assert_true(condition: bool, msg: Optional[str] = None) -> None:
        """
        Asserts that a condition is true. If not, throws an AssertionError with the given message.

        :param condition: condition to be checked
        :param msg: message to be displayed in case of failure
        """

        assert_with_hook_failure(condition, msg)

    @staticmethod
    def assert_false(condition: bool, msg: Optional[str] = None) -> None:
        """
        Asserts that a condition is false. If not, throws an AssertionError with the given message.

        :param condition: condition to be checked
        :param msg: message to be displayed in case of failure
        """
        assert_with_hook_failure(not condition, msg)

    @staticmethod
    def assert_equal(actual: object, expected: object, msg: Optional[str] = None) -> None:
        """
        Asserts that two objects are equal. If not, throws an AssertionError with the given message.

        :param actual: actual object
        :param expected: expected object
        :param msg: message to be displayed in case of failure
        """
        assert_with_hook_failure(actual == expected, msg)

    @staticmethod
    def assert_not_equal(actual: object, expected: object, msg: Optional[str] = None) -> None:
        """
        Asserts that two objects are not equal. If not, throws an AssertionError with the given message.

        :param actual: actual object
        :param expected: expected object
        :param msg: message to be displayed in case of failure
        """
        assert_with_hook_failure(actual != expected, msg)

    @staticmethod
    def assert_is_none(obj: object, msg: Optional[str] = None) -> None:
        """
        Asserts that an object is None. If not, throws an AssertionError with the given message.

        :param obj: object to be checked
        :param msg: message to be displayed in case of failure
        """
        assert_with_hook_failure(obj is None, msg)

    @staticmethod
    def assert_is_not_none(obj: object, msg: Optional[str] = None) -> None:
        """
        Asserts that an object is not None. If not, throws an AssertionError with the given message.

        :param obj: object to be checked
        :param msg: message to be displayed in case of failure
        """
        assert_with_hook_failure(obj is not None, msg)

    @staticmethod
    def assert_in(obj: object, container: object, msg: Optional[str] = None) -> None:
        """
        Asserts that an object is in a container. If not, throws an AssertionError with the given message.

        :param obj: object to be checked
        :param container: container to check
        :param msg: message to be displayed in case of failure
        """
        assert_with_hook_failure(obj in container, msg)

    @staticmethod
    def assert_not_in(obj: object, container: object, msg: Optional[str] = None) -> None:
        """
        Asserts that an object is not in a container. If not, throws an AssertionError with the given message.

        :param obj: object to be checked
        :param container: container to check
        :param msg: message to be displayed in case of failure
        """
        assert_with_hook_failure(obj not in container, msg)


def assert_with_hook_failure(condition: bool, msg: Optional[str] = None) -> None:
    """
    Asserts that a condition is true. If not, throws an AssertionError.

    :param condition: condition to be checked
    :param msg: message to be displayed in case of failure
    """

    def fn(entity: Any):
        if not condition:
            raise AssertionError(msg)

    browser.with_(timeout=0).wait.for_(fn)
