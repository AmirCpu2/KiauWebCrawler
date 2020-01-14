from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import csv

# Function Whate of Load 100%
def Whating (id,val,mode):
    while 1 :
        if mode == True:
            if( str(val) == str(driver.find_element_by_id(id).get_attribute("value")).strip() ):
                print("-----------------------------------------------------------")                
                print(driver.find_element_by_id(id).get_attribute("value").strip())
                print("-----------------------------------------------------------")
                break

        if mode == False:
            if( str(val) != str(driver.find_element_by_id(id).text).strip() ):
                print("-----------------------------------------------------------")
                print(driver.find_element_by_id(id).text)
                print("-----------------------------------------------------------")
                break
        
        if mode == 3 :
            if(table[-1] != driver.find_element_by_id(id).text) :
                break

def SaveTable (DataTable):

   # Open File And set mode Write
    with open('KiauTables.csv', 'w',encoding='utf-8', newline='') as csvfile:
        
        # Head
        fieldnames = ['مشخصه', 'نام درس', 'مقطع کلاس', 'نظری', 'نوع عملی', 'نوع عملی', 'جنسیت', 'گروه کلاس', 
        'باقي مانده', 'ساعت کلاس', 'ساعت امتحان', 'ت امتحان', 'نام استاد', 'گروه بندی']
        
        # Config head
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write Head
        writer.writeheader()
        
        for row in DataTable:
            # Write Row
            try:
                writer.writerow({
		fieldnames[0]: row[0],
		fieldnames[1]: row[1],
		fieldnames[2]: row[2],
		fieldnames[3]: row[3],
		fieldnames[4]: row[4],
	 	fieldnames[5]: row[5],
	 	fieldnames[6]: row[6],
		fieldnames[7]: row[7],
	 	fieldnames[8]: row[8], 
		fieldnames[9]: row[9], 
		fieldnames[10]: row[10],
		fieldnames[11]: row[11], 
		fieldnames[12]: row[12], 
		fieldnames[13]: row[13] })
            except:
                pass


table = []
i = 1
tempHash = hash('start')
MaxLen = 15
url = 'http://edu.kiau.ac.ir'
Mode = 0
user = "962097617"
pasw = "pass"

# config drive
driver = webdriver.Firefox()

# GoTo url
driver.get(url)

# Wating Load
assert "سیستم ثبت نام" in driver.title

# Insert UserName And Password
driver.find_element_by_name("txtUserName").send_keys(user)
driver.find_element_by_name("txtPassword").send_keys(pasw)

# Input Key for Captcha
Captcha = input("\n\n\n\n PLS ENTER CAPTCHA NUMBER: ")

# Set Captcha Number
driver.find_element_by_name("texttasvir").send_keys(Captcha)

# Select login
elem = driver.find_element_by_name("LoginButton0").click()

"""********************
    Start Scipts
********************"""
# Value Script
scripts = [
    'location.replace("http://edu.kiau.ac.ir/list_ara.aspx")', #لیست دروس ارئه شده 1
    "__doPostBack('ctl00$ContentPlaceHolder1$grdCourseList','Page$", #تغییر شماره صفحه 2
]

"""********************
    Stop Scipts
********************"""

# Goto Page
driver.execute_script(scripts[Mode])

# Load wating time
time.sleep(2)
driver.implicitly_wait(2)


# Get Table
while i <= MaxLen :
    try:
        # Get Table
        Tb = driver.find_element_by_id('ctl00_ContentPlaceHolder1_grdCourseList')
        
        # Get row
        rows = Tb.find_elements_by_css_selector('tr')
        
        for row in rows :
            colsTemp = row.find_elements_by_css_selector("td")
            cols = list(map(lambda x: x.text , colsTemp))
            print(cols)
            table.append(cols)
        
        # Next Page
        print(scripts[1]+str(i)+';')
        driver.execute_script(scripts[1]+str(i)+'\');')
        
        if(i == 2):
            time.sleep(10)
            
        # Status
        print('Page: ',i)

        # Print
        print(table[i])

        i += 1
        
    except:
        pass
        print('Exception')
    
SaveTable(table)

driver.close()


