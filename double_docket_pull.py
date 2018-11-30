import urllib3
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from selenium.webdriver.common.keys import Keys
import webbrowser
import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
from _datetime import datetime


driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
driver.get('https://www5.elawsoftware.com/eLawSecure.nsf/SecureLogin?ReadForm')#put here the address of your page

user1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[3]/input"
pass1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[2]/td[3]/input"
access_server_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[3]/td[1]/div/input"


#find the elements to click and interact with
user1 = driver.find_element_by_xpath(user1_XPATH)
pass1 = driver.find_element_by_xpath(pass1_XPATH)
access1 = driver.find_element_by_xpath(access_server_XPATH)
user1.send_keys("Leonard.martinez")
pass1.send_keys("51698")
access1.click()
urlform2 = "https://www5.elawsoftware.com/1217/1217_Criminal.nsf/DocketReportSelection?OpenForm&t=1"
urlform3 = "https://www5.elawsoftware.com/1217/1217_Criminal.nsf/DocketReportSelection?OpenForm&Seq=1&t=1"
driver.get(urlform2)

#date logic
dt = datetime.now()
tmrw_day_int = int(dt.day) + 1
tmrw_day = str(tmrw_day_int)
tmrw_month = str(dt.month)
tmrw_yr = str(dt.year)
ds = "/"
entered_date = tmrw_month + ds + tmrw_day + ds +tmrw_yr
docket_date1 = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[6]/td/font[1]/input")
docket_date2 = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[6]/td/font[2]/input")

def replace_values2():
    docket_date1.clear()
    docket_date1.send_keys(entered_date)
    docket_date2.clear()
    docket_date2.send_keys(entered_date)

replace_values2()
urlform3_XPATH = "//*[@id=\"menu0\"]"

driver.find_element_by_xpath(urlform3_XPATH).click()

def print2():
    keyboard.press_and_release('ctrl+shift+p')
    time.sleep(5)
#Print Elaw Docket
print2()
driver.close()
#Start TCDJ Docket search print

def tcdj1():
    driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
    url_tcdj = ("https://publiccourts.traviscountytx.gov/dsa/#/")
    driver.get(url_tcdj)
    wait = WebDriverWait(driver, 10)
    xpath_att1 = "/html/body/div/div/div/div[3]/div/span[2]/button"
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_att1)))
    attorney2 = driver.find_element_by_xpath(xpath_att1)
    attorney2.click()
    xpath_ln2 = "//*[@id=\"att-last-name\"]"
    xpath_fn2 = "//*[@id=\"att-first-name\"]"
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_ln2)))
    lastname2 = driver.find_element_by_xpath(xpath_ln2)
    lastname2.send_keys("Martinez")
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_fn2)))
    firstname2 = driver.find_element_by_xpath(xpath_fn2)
    firstname2.send_keys("Leonard")
    d2s1_xpath = "//*[@id=\"quick-date\"]"
    wait.until(EC.presence_of_element_located((By.XPATH, d2s1_xpath)))
    d2sbox = driver.find_element_by_xpath(d2s1_xpath)
    d2sbox.click()
    keyboard.press_and_release("down")
    keyboard.press_and_release("enter")
    xpath_search2 = "/html/body/div/div/div/form/fieldset/div[1]/div[3]/button"
    search2 = driver.find_element_by_xpath(xpath_search2)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_search2)))
    search2.click()
    xpath_checkbox = "/html/body/div/div/div/div[4]/div[2]/div/div/div[1]/div[1]/input"
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_checkbox)))
    check = driver.find_element_by_xpath(xpath_checkbox)
    check.click()
    keyboard.press_and_release('ctrl+shift+p')
    time.sleep(5)
tcdj1()
