from turtle import pos, position
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform

import os
import csv

filename=str(input("Enter the Filename:  ")).strip()


def reverseGeocoder(lat,lng):

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')

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

position=0
posfile_name = "position_"+filename[0:-4]+".txt"

if os.path.exists(posfile_name)==True:
    with open(posfile_name, "r") as fpos:
        position = int(fpos.read())
else:
    with open(posfile_name, "w") as posup:
                    posup.write(str(0))


position_current=position
position_immutable = position + 1

i=0



fields=['FeatureID', 'AIM_Postal', 'AIM_Addres', 'Near_POI', 'Country', 'Admin_l1', 'Admin_l2', 'Direction', 'Street_Nm', 'Latitude', 'Longitude', 'Address']

if os.path.exists('Results_'+filename)!=True:
    with open('Results_'+filename, 'w') as csvfile:
                    csvwriter = csv.writer(csvfile) 
                    csvwriter.writerow(fields)

prev=[]


with open(filename, mode='r') as file:
    csvreader = csv.reader(file)
    for lines in csvreader:
        if position==0:
            if lines[-1]=='':
                prev=lines
                try:
                    lines[-1]=reverseGeocoder(str(lines[-3]),str(lines[-2]))  #errors happen here 
                    i+=1                                                      #Try Except to avoid this exact thing
                except:
                    lines[-1]=reverseGeocoder(str(lines[-3]),str(lines[-2]))

                print("Updating Progress")
                position_current+=1
                position_immutable+=1
                with open(posfile_name, "w") as posup:
                    posup.write(str(position_current))

                print("Publishing to File")
                with open('Results_'+filename, 'a') as csvfile: 
                    csvwriter = csv.writer(csvfile) 
                    csvwriter.writerow(lines) 


                print("Success")

                print(str(i)+" points complete")

                with open(posfile_name, "w") as posup:
                    posup.write(str(position_immutable))
        else:
            position_current-=1
            position-=1






