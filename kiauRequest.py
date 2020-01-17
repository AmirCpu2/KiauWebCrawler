from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import time
import re

#---------------------InitializeValue--------------------------
SubjectCorse = 'معماری'
url = 'http://edu.kiau.ac.ir'
user = '962097617'
pasw = '*********'
sessionId 	= ''
captchaCode = []
sessionIdHistory = []
payload = {
"__EVENTTARGET": '' ,
"__EVENTARGUMENT": '' ,
"__VIEWSTATE": '' ,
"__VIEWSTATEGENERATOR": '' ,
"__EVENTVALIDATION": '' ,
"txtUserName": user ,
"txtPassword": pasw ,
"texttasvir": captchaCode ,
"LoginButton0":"ورود دانشجو"
}
payloadTable = {
"ctl00$ScriptManager1": 'ctl00$UpdatePanel1|ctl00$ContentPlaceHolder1$grdCourseList' ,
"__EVENTTARGET": 'ctl00$ContentPlaceHolder1$grdCourseList' ,
"__EVENTARGUMENT": 'Page$1' ,
"__LASTFOCUS": '',
"__VIEWSTATE": '' ,
"__VIEWSTATEGENERATOR": '' ,
"__VIEWSTATEENCRYPTED": '',
"__EVENTVALIDATION": '' ,
"ctl00$ContentPlaceHolder1$a1":"RadioButton1",
"__ASYNCPOST": True
}

# --------------------Functions---------------------
def ocr_space_file(filename, overlay=False, api_key='55c76e3c7d88957', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()

def GetValueById(object,element,id):
	try:
		return object.xpath('//{}[@id="{}"]/@value'.format(element,id))[0]
	except:
		return ''
		
def GetValueByName(object,name):
	try:
		return object.xpath('//{}[@name="{}"]/@value'.format(element,id))[0]
	except:
		return ''

def InitializeValue():
	# Get Value And Settion Temp
	BasePage = requests.get(url+"/login.aspx")
	sessionId = BasePage.cookies.get('ASP.NET_SessionId')
	sessionIdHistory.append(sessionId)
	tree = html.fromstring(BasePage.content)
	payload['__VIEWSTATE'] = GetValueById(tree,'input','__VIEWSTATE')
	payload['__VIEWSTATEGENERATOR'] = GetValueById(tree,'input','__VIEWSTATEGENERATOR')
	payload['__EVENTTARGET'] = GetValueById(tree,'input','__EVENTTARGET')
	payload['__EVENTARGUMENT'] = GetValueById(tree,'input','__EVENTARGUMENT')
	payload['__EVENTVALIDATION'] = GetValueById(tree,'input','__EVENTVALIDATION')

def GetNewSession():
	InitializeValue()
	GetNewCapcha()

def GetNewCapcha():
	try:
		cookiesTemp = dict({'ASP.NET_SessionId':str(sessionIdHistory[-1])})
		r = requests.get(url+"/captcha.aspx",cookies=cookiesTemp)
		f=open('yourcaptcha.png','wb')
		f.write(r.content)
		f.close()
		time.sleep(2)
		test_file = ocr_space_file(filename='yourcaptcha.png' ,language='pol').replace('false','False')
		captchaCode.append( eval(test_file)["ParsedResults"][0]["ParsedText"] )
		payload['texttasvir'] = str(int(captchaCode[-1]))
	except:
		GetNewCapcha()

def SetPayloadList(object,page):
	# Get Value And Settion Temp
	tree = html.fromstring(object.content)
	payloadTable['__VIEWSTATE'] = GetValueById(tree,'input','__VIEWSTATE')
	payloadTable['__VIEWSTATEGENERATOR'] = GetValueById(tree,'input','__VIEWSTATEGENERATOR')
	payloadTable['__EVENTTARGET'] = GetValueById(tree,'input','__EVENTTARGET')
	payloadTable['__EVENTARGUMENT'] = 'Page${}'.format(page)
	payloadTable['__EVENTVALIDATION'] = GetValueById(tree,'input','__EVENTVALIDATION')
	
# ----------------------Main------------------------

# Update Session
GetNewSession()

# Get Main Cookies
cookies = dict({'ASP.NET_SessionId':str(sessionIdHistory[-1])})
login = requests.post(url+"/login.aspx",data=payload,cookies=cookies)
headers = login.headers
# set cookies
# cookies = login.cookies

print(login.text)
print(str(login.history[0].cookies.get('ASP.NET_SessionId')))

# First Page List
lists = requests.post(url+"/list_ara.aspx",data=payload,cookies=cookies)

print(lists.text)

SetPayloadList(lists,2)
lists2 = requests.post(url+"/list_ara.aspx",data=payloadTable,cookies=cookies)

print(lists2.text)

SetPayloadList(lists2,3)
lists3 = requests.post(url+"/list_ara.aspx",data=payloadTable,cookies=cookies)

print(lists3.text)
