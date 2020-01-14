from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import csv

# SaveTable
def SaveTable (DataTable):

   # Open File And set mode Write
    with open('mrudTables.csv', 'w',encoding='utf-8', newline='') as csvfile:
        
        # Head
        fieldnames = ['مشخصه', 'نام درس', 'مقطع کلاس', 'نظری', 'نوع عملی', 'جنسیت', 'گروه کلاس', 
        'باقي مانده', 'ساعت کلاس', 'sساعت امتحان', 'ت امتحان', 'نام استاد', 'گروه بندی', '', '', "", ""]
        
        # Config head
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write Head
        writer.writeheader()
        
        for row in DataTable:
            # Write Row
            writer.writerow({fieldnames[0]: row[0], fieldnames[1]: row[1], fieldnames[2]: row[2],
             fieldnames[3]: row[3], fieldnames[4]: row[4], fieldnames[5]: row[5], fieldnames[6]: row[6],
              fieldnames[7]: row[7], fieldnames[8]: row[8], fieldnames[9]: row[9], fieldnames[10]: row[10],
              fieldnames[11]: row[11], fieldnames[12]: row[12], fieldnames[13]: row[13], fieldnames[14]: row[14],
              fieldnames[15]: row[15], fieldnames[16]: row[16], fieldnames[17]: row[17] })




# value
SubjectCorse = 'معماری'
table = []
i = 1
tempHash = hash('start')
MaxLen = 10
url = 'http://edu.kiau.ac.ir'
Mode = 0
user = '962097617'
pasw = 'pass'

# config drive
driver = webdriver.Firefox()

# GoTo url
driver.get(url)

# Wating Load
assert "سیستم ثبت نام" in driver.title

# Insert UserName And Password
driver.find_element_by_name("txtUserName").clear()
driver.find_element_by_name("txtUserName").send_keys(user)
driver.find_element_by_name("txtPassword").clear()
driver.find_element_by_name("txtPassword").send_keys(pasw)

# Input Key for Captcha
Captcha = input("\n\n\n\n PLS ENTER CAPTCHA NUMBER: ")

# Set Captcha Number
driver.find_element_by_name("texttasvir").send_keys(Captcha)

# Select login
driver.find_element_by_name("LoginButton0").click()

# /////////////////////////HOME PAGE////////////////////////// #

"""********************
    Start Scipts
********************"""
# Value Script
scripts = [
    'location.replace("http://edu.kiau.ac.ir/SelectCourse.aspx?h=2")', #لیست دروس ارئه شده ۱
    "__doPostBack('ctl00$ContentPlaceHolder1$grdCourseList','Page$", #تغییر شماره صفحه 2
    "$('#ctl00_ContentPlaceHolder1_Button6').click()", #3 رفتن به صفحه لیست
    "$('#ctl00_ContentPlaceHolder1_TextBox1').val('معماری')",
    "$('#ctl00_ContentPlaceHolder1_btnSave4').click()",
]

"""********************
    Stop Scipts
********************"""



# Got add page
driver.execute_script(scripts[Mode])
time.sleep(2)

# Goto List Page
driver.execute_script(scripts[2])

time.sleep(2)

# Set Value
driver.execute_script(scripts[3])


while 1 :
    try:
        # Serch click
        driver.execute_script(scripts[4])

        # Wating
        driver.implicitly_wait(5)

        # Get row
        rows = driver.find_elements_by_css_selector('tr .GridViewRow_listara')
        
        rows.extend(driver.find_elements_by_css_selector('tr .GridViewAlternatingRow'))
        
        for row in rows :
            colsTemp = row.find_elements_by_css_selector("td")
            cols = list(map(lambda x: x.text , colsTemp))
            print(cols)
            table.append(cols)

    except:
        print('Exeption')


exit()

