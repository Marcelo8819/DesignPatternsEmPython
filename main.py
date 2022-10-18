from urllib import response
from factory import MysqlFactory
import usecase

usecase = MysqlFactory.create()
response = usecase.do_something(True)

print(response)
