from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform
import csv

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
            executable_path="/usr/bin/chromedriver", options=options)

    # Obtain the Google Map URL
    url = "http://maps.google.com/maps?z=12&t=m&q=loc:"+lat+"+"+lng
    # Open the Google Map URL
    browser.get(url)
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "LCF4w")))
    title = browser.find_element(By.CLASS_NAME, "LCF4w")
    print(title.text)
    return title.text

i=0



fields=['FeatureID', 'AIM_Postal', 'AIM_Addres', 'Near_POI', 'Country', 'Admin_l1', 'Admin_l2', 'Direction', 'Street_Nm', 'Latitude', 'Longitude', 'Address']

with open('Results.csv', 'w') as csvfile:
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerow(fields)

with open('Muscat_Data.csv', mode='r') as file:
    csvreader = csv.reader(file)
    for lines in csvreader:
        if lines[-1]=='':
            lines[-1]=reverseGeocoder(str(lines[-3]),str(lines[-2]))
            i+=1

            print("Publishing to File")

            with open('Results.csv', 'a') as csvfile: 
                csvwriter = csv.writer(csvfile) 
                csvwriter.writerow(lines) 


            print("Success")

            print(str(i)+" points complete")







