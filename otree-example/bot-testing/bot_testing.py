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
def demopage_0(driver,run_number):
#fill out age question (random 1 to 40)
    xpath_age  = '//*[@id="id_age_question"]'
    age = random.randint(1,40)
    driver.find_element(By.XPATH, xpath_age).send_keys(str(age))
     
     #randomly select a gender 
    gender = driver.find_elements(By.NAME, 'gender_question')
    rand_selection = random.randint(0, len(gender) - 1)
    gender[rand_selection].click()
    # next
    
    #write a name 
    xpath_name = '//*[@id="id_name_question"]'
    #give the bots different names according to their current run through the survey
    name_input = f'Bot_{run_number}'
    driver.find_element(By.XPATH, xpath_name).send_keys(str(name_input))

    #test if demo is passed correctly
    print("passed demopage_0")


#handle end page 
def end_page(driver):
    #click submit answers 
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()


#link to the current session being tested 
link = 'http://localhost:8000/join/fubivadu'

#method to run the bots n times over the survey 
def run_bots(runs,link):
    driver = build_driver()  # initialize the driver
    for i in range(runs):
        driver.get(link)
    
        #order of pages shown
        welcome_page(driver)
        demopage_0(driver,i)
        end_page(driver)


    #after completion, print success in the console
    print("Sucess!")

#run the bots
run_bots(runs=19, link=link)