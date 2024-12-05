from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import string
import time

def build_driver():
    # Set up the driver
    return webdriver.Chrome() #(ChromeDriverManager().install())



#handle welcome page button 
def welcome_page(driver):
    #click next button
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()

#handle demopage0 
def demopage_0(driver):
    
#handle end page 
def end_page(driver):
    #click submit answers 
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()


#link to the current session being tested 
link = 'http://localhost:8000/join/juhimija'

#method to run the bots n times over the survey 
def run_bots(runs,link):
    driver = build_driver()  # initialize the driver
    for i in range(runs):
        driver.get(link)
    
        #order of pages shown
        welcome_page(driver)
        end_page(driver)


    #after completion, print success in the console
    print("Sucess!")

#run the bots
run_bots(runs=20, link=link)