import json

from web_test.assist.project import abs_path_from_project
from web_test.assist.requests.http import HttpRequest as request
from web_test.assist.requests.method import post

data_json_file = abs_path_from_project('web_test/mock/data.json')


# mock send data
class MockSendData(object):
    """
    模拟发送数据
    """

    def __init__(self):
        self.base_url = ''
        self.header = {

        }

        self.data = lambda key: json.load(open(data_json_file)).get(key)

    @request(url='', method=post)
    def send_example_value(self, value):
        json_data = self.data('example')
        json_data['key'] = value
        return {'json': json_data}


mock_send_data = MockSendData()
