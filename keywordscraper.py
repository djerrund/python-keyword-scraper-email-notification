#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import smtplib, ssl

#Adding these options makes sure the chrome browser is opened without UI. Therefore allowing you to launch the process in the background. 
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#Download the Chrome Driver here: https://chromedriver.chromium.org/ 
driver = webdriver.Chrome(executable_path='YOUR PATH TO YOUR CHROME DRIVER', chrome_options=options) 

#Setup your email client. https://realpython.com/python-send-email/ for easy instructions on how to do it.
port=465
password = "YOUR EMAIL PASSWORD"
context = ssl.create_default_context()
sender_email = "YOUR EMAIL ADRESS"

#A list of email adresses which you want to notify when the keywords have changed.
emails = ["EMAIL1@ADRESS.COM","EMAIL2@ADRESS.COM"]

#Define the urls that you want to scrape.
websites = ["URL1","URL2","URL3"]

#Setup the keywords you are looking for to change on the website. 
status = "KEYWORD1"
status2 = "KEYWORD2"

#This function gets called anytime the keyword you are scraping for has changed on the live website. (aka website = updated)
#Function sends an email with info to receiver.
#change variables up to your taste: i used title, floor and availability as I was scraping a real estate website for changes.
def send_Mail(title, floor, availability):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email,password)
            message = "Subject: type a cool message here " + title + " on floor: " + floor + " has a new status of: " + availability
            for mail in emails:
                server.sendmail(sender_email,mail,message)

#For every url you defined --> Open website, wait 2 seconds (allow website to be fully loaded), scrape the content you defined, check if keywords match, otherwise send email.
for website in websites:
    driver.get(website) 
    time.sleep(2)
    #I use Xpath to find the correct elements that i want to check for changes. For an introduction I advice to read: https://towardsdatascience.com/how-to-use-python-and-xpath-to-scrape-websites-99eaed73f1dd 
    title= driver.find_element_by_xpath('ENTER XPATH HERE').get_attribute('innerHTML')
    availability = driver.find_element_by_xpath('ENTER XPATH HERE').get_attribute('innerHTML')
    floor = driver.find_element_by_xpath('ENTER XPATH HERE').get_attribute('innerHTML')
    if availability != status and availability != status2:
        send_Mail(title,floor,availability)            

#Stop the process.      
driver.quit()
