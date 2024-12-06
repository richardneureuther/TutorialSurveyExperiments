from asyncio import wait
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

def check_exists_by_xpath(driver, xpath):
    try:
        x = driver.find_element(By.XPATH, xpath)
        if x.is_displayed():
            return 1
    except NoSuchElementException:
        return 0

#handle welcome page button 
def welcome_page(driver):
    #click next button
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()
    print (" welcome passed")
    


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
    print(" demopage_0 passed")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()


#handle demopage_1
def demopage_1(driver):
    xPath_study ='/html/body/div/form/div/div/div/input'
    input_options = ["SEDS", "PolVer", "WiWi", "Jura", "Soziologie", 123]
    #choose input value
    input =  random.choice(input_options)
    #test whether strings and integer are both accepted 
    driver.find_element(By.XPATH, xPath_study).send_keys(input if isinstance(input, str) else str(input))

    #print the input that was  passed successfully 
    print(f" demopage_1 passed. Input: {input}")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()

#handle demopage_2
def demopage_2(driver):
    satisfaction = driver.find_elements(By.NAME, 'satisfaction')
    rand_selection = random.randint(0, len(satisfaction) - 1)
    satisfaction[rand_selection].click()
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()

    print(" demopage_2 passed")


#handle demopage_3
def demopage_3(driver):
    xPath_additional ='/html/body/div/form/div/div/div/input'
    input_options = ["no", "no comment", "Hello", 123]
    input =  random.choice(input_options)
    driver.find_element(By.XPATH, xPath_additional).send_keys(input if isinstance(input, str) else str(input))
    print(f" demopage_3 passed. Input: {input}")
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()


#handle interface rating pages
def demopage_4(driver):
    
    #implement a scroller so the radio question can be proberly accessed on the page 
    def scroller(driver, element):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.3)  #short scroll timer 
        element.click()

    #extract src attribute to handle the detect the images 
    image_element = driver.find_element(By.XPATH, '//img')
    image_src = image_element.get_attribute('src')
    
    #check which image is displayed and assign the correct name 
    if 'windows_phone.png' in image_src:
        print("Windows Phoneis shown.")
        name = 'windows_interface'

    elif 'IOS_10_phone.png' in image_src:
        print("iOS Phone is shown.")
        name = 'iOS_interface'
    
    #randomly select one button in the radio question 
    interface_options = driver.find_elements(By.NAME, name)
    rand_selection = random.randint(0, len(interface_options) - 1)
    scroller(driver, interface_options[rand_selection])

    #next page
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()
    print(" demopage_4 passed")


#handle popout questions
def popout(driver):
    yes = '//*[@id="UniYes"]'
    no = '//*[@id="UniNo"]'
    select = random.randint(0, 1)
    input_text = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 10)))
    
    if select == 0:
        driver.find_element(By.XPATH, yes).click()
        driver.find_element(By.XPATH, '//*[@id="divYes"]/input').send_keys(input_text)

    else:
        driver.find_element(By.XPATH, no).click()
        driver.find_element(By.XPATH, '//*[@id="divNo"]/input').send_keys(input_text)

    # next button
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()
    print(" popout passeed")


#handle end page 
def end_page(driver):
    #click submit answers 
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()


#method to run the bots n times over the survey 
def run_bots(runs,link):
    driver = build_driver()  # initialize the driver
    for i in range(runs):
        driver.get(link)
        if check_exists_by_xpath(driver, '//*[@id="form"]/div/button') == 1:
            x = welcome_page(driver) # check whether they are eligible
            if x == 1:  # then they are not eligible, otherwise no next page
                continue

        #order of pages shown
        welcome_page(driver)
        demopage_0(driver,i)
        demopage_1(driver)
        demopage_2(driver)
        demopage_3(driver)
        demopage_4(driver)
        popout(driver)
        end_page(driver)
        
        #print the current bot run 
        print(f'Bot_{i} passed')

    #after completion, print success in the console
    print("Success!")


#link to the current session being tested 
link = 'http://localhost:8000/join/tanabusu'

#run the bots
run_bots(runs=20, link=link)
