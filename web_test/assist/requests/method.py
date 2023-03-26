from typing import Literal, Final

RequestMethod = Literal['get', 'post', 'put', 'delete', 'head', 'options', 'trace']

get: Final[RequestMethod] = 'get'
post: Final[RequestMethod] = 'post'
put: Final[RequestMethod] = 'put'
delete: Final[RequestMethod] = 'delete'
head: Final[RequestMethod] = 'head'
options: Final[RequestMethod] = 'options'
trace: Final[RequestMethod] = 'trace'
