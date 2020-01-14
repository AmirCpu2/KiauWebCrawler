import requests
import re
from bs4 import BeautifulSoup
# from PIL import Image
# from StringIO import StringIO
#import mysql.connector
#from sklearn import tree
#from unidecode import unidecode

# Json To dctr
import json
class Payload(object):
	def __init__(self, j):
		self.__dict__ = json.loads(j)

# value
SubjectCorse = 'معماری'
table = []
i = 1
tempHash = hash('start')
MaxLen = 10
url = 'http://edu.kiau.ac.ir'
Mode = 0
user = '962097617'
pasw = '440729300'


payload = {
"__EVENTTARGET":"",
"__EVENTARGUMENT":"",
"__VIEWSTATE":"/wEPDwULLTE1NjEwNjU3MTcPZBYCAgMPZBYCAgMPZBYOAgEPDxYCHgRUZXh0BTTYr9in2YbYtNqv2KfZhyDYotiy2KfYryDYp9iz2YTYp9mF24wt2YjYp9it2K8g2qnYsdisZGQCAw8PFgIfAAUE2K/ZimRkAgUPDxYCHwAFAjIyZGQCBw8PFgIfAAUM2YrZg9i02YbYqNmHZGQCJQ8PFgIfAAUIMjI6MTQ6MThkZAInDw8WAh8ABQg5OC8xMC8yMmRkAikPDxYCHwAFD0lQOjUuMTE1LjE5Ny4yOWRkZGRNoXbfRzZ6QK1ycx5b+mWK1opFOAdD+GkNkPCYS8PO"
,"__VIEWSTATEGENERATOR":"C2EE9ABB"
,"__EVENTVALIDATION":"/wEdAAnxFiP58N/x+G0k2ByFkDtxY3plgk0YBAefRz3MyBlTcHY2+Mc6SrnAqio3oCKbxYagRg8D1wl3DJW96NwHqfmRl6qwaMJiTL4nII9SPDK0X9ypqPqLgdpphNzIPTIm7G6/X7pAi+pEIw57kY0UjHH+P1jLJHiqNfRsonZfptdXU6VW8D6NY9Ur5cwFEXJj1xT7dvZfqEa6Irc2JqbFXz9N2aCjjZjj42u4LtI7vtXGgQ=="
,"txtUserName":"962097617"
,"txtPassword":"440729300"
,"texttasvir":"7534"
,"LoginButton0":"ورود دانشجو"
}

cookies = dict({'ASP.NET_SessionId':'g0tcbsbn2q44gfgb2isxzgnw'})
login = requests.post(url+"/login.aspx",data=payload,cookies=cookies)

print(login.text)
print(login.cookies)
