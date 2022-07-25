from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import subprocess
import os

def url(lat, lng):
    url = "http://maps.google.com/maps?z=12&t=m&q=loc:"+lat+"+"+lng
    return url

def create_torbrowser_webdriver_instance():
    tor_binary_path_driver =  '/Applications/Tor\ Browser.app/Contents/MacOS/firefox'
    geckodriver_path = 'drivers/geckodriver'

    os.popen(tor_binary_path_driver)
    options = Options()
    options.headless = True

    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['proxy'] = {
        "proxyType": "MANUAL",
        'socksProxy': '127.0.0.1:9150',
        "socksVersion": 5
    }

    driver = webdriver.Firefox(capabilities=firefox_capabilities, options=options, executable_path=geckodriver_path)
    return driver

if __name__ == '__main__':
    os.system("""osascript -e 'tell app "Tor Browser" to open'""")
    driver = create_torbrowser_webdriver_instance()
    driver.get(url('0','0'))

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "LCF4w")))
    title = driver.find_element(By.CLASS_NAME, "LCF4w")


    print(title.text)


    driver.close()
    subprocess.call(['osascript', '-e', 'tell application "Tor Browser" to quit'])


create_torbrowser_webdriver_instance()