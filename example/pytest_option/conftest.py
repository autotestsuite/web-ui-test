import pytest

from web_test.alternative.pytest.project.settings import Option


class Config:

    def __init__(self, request):
        self.request = request

    @Option.default(6.0)
    def timeout(self): pass

    @Option.default('gu xin')
    def author(self): pass


def pytest_addoption(parser):
    Option.register_all(from_cls=Config, in_parser=parser)


@pytest.fixture
def config(request):
    return Config(request)


@pytest.fixture(scope='function', autouse=True)
def timeout_management(config):
    timeout = config.timeout
    yield timeout


@pytest.fixture(scope='function', autouse=True)
def author_management(config):
    author = config.author
    yield author
