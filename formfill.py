#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver.v2 as uc
from colorama import Fore
from getpass import getpass
import os
import time

os.system("")
form_url = 'https://www.google.com/url?q=https://docs.google.com/forms/d/1_XyTRmCotkVFmU_V83Mma9uGUMY460CDFEe64-QgYM0/edit&sa=D&source=editors&ust=1625133094923000&usg=AFQjCNH3OrJO5iLaUxIMd5UsjAC8x61Qaw'
driver = uc.Chrome(executable_path = 'webdrivers/chromedriver')


def google_signIn_requirement():
    global email
    with driver:
        print(Fore.BLUE+'Complete Google Sign In requirement to fill google form'.upper())

        email = input(Fore.GREEN+'email:')
        passwd = getpass(prompt = Fore.RED+'Password [hidden]: ')
    
        driver.implicitly_wait(1000)
        driver.get(form_url)
        sign_in_el = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span')
        sign_in_el.click()

        email_text_area_el = driver.find_element_by_xpath('//*[@id="identifierId"]')

        email_text_area_el.clear()
        email_text_area_el.send_keys(email)
        email_text_area_el.send_keys(Keys.RETURN)

        pswd_el = driver.find_element_by_name('password')
        pswd_el.send_keys(passwd)
        pswd_el.send_keys(Keys.RETURN)

def fillform():
    info = {'name':'William Akuffo','gender':'//*[@id="i9"]/div[3]/div','email':email,
            'school': 'Ashesi University','address':'West Hill, Weija - Accra',
            'phone':'0551021866','comment': 'all good!'}

    with driver:
        name_el = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        name_el.send_keys(info['name'])

        gender_el = driver.find_element_by_xpath(info['gender'])
        gender_el.click()

        email_el = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        email_el.send_keys(info['email'])

        next_btn = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        next_btn.click()
        
        time.sleep(2)

        school_el = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        school_el.send_keys(info['school'])

        addr_el = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
        addr_el.send_keys(info['address'])

        phone_el = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        phone_el.send_keys(info['phone'])

        com_el = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
        com_el.send_keys(info['comment'])
        
        #submit
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span').click()

        
if __name__ == '__main__':
    google_signIn_requirement()
    fillform()


