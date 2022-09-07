from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform

def reverseGeocoder(lat,lng):

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    # Created the webdriver object
    if platform.system()=="Windows":
        browser = webdriver.Chrome(
            executable_path="drivers/chromedriver.exe", options=options)

    elif platform.system()=="Darwin":
        browser = webdriver.Chrome(
            executable_path="/usr/local/bin/chromedriver", options=options)

    else:
        browser = webdriver.Chrome(
            executable_path="drivers/chromedriver", options=options)

    # Obtain the Google Map URL
    url = "http://maps.google.com/maps?z=12&t=m&q=loc:"+lat+"+"+lng
    # Open the Google Map URL
    browser.get(url)
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "LCF4w")))
    title = browser.find_element(By.CLASS_NAME, "LCF4w")
    print(title.text)
    return title.text

l=[[2.03309773, 45.32264565], [2.04079502, 45.30499841], [2.07687304, 45.25457644], [2.05326028, 45.29406460], [2.07376117, 45.26852418]]


for i in l:
    reverseGeocoder(str(i[0]), str(i[1]))

