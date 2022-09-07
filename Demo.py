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
            executable_path="drivers/chromedriver", options=options)

    # Obtain the Google Map URL
    url = "http://maps.google.com/maps?z=12&t=m&q=loc:"+lat+"+"+lng
    # Open the Google Map URL
    browser.get(url)
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "LCF4w")))
    title = browser.find_element(By.CLASS_NAME, "LCF4w")
    print(title.text)
    return title.text

i=0

fields=['ID', 'Lat', 'Long', 'Address']
rows=[]

with open('Sample_lat_long.csv', mode='r') as file:
    csvreader = csv.reader(file)
    for lines in csvreader:
        if lines[-1]=='':
            lines[-1]=reverseGeocoder(str(lines[1]),str(lines[2]))
            rows.append(lines)
            i+=1
            print(str(i)+" points complete")

print("Publishing Files")

with open('Results.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)

print("Success")





