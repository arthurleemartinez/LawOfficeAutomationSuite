import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import keyboard
from selenium import webdriver
from _datetime import datetime
import datetime
import holidays

ONE_DAY = datetime.timedelta(days=1)
HOLIDAYS_US = holidays.US()


def next_business_day():
    next_day = datetime.date.today() + ONE_DAY
    global reformatted
    reformatted = ""
    while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_US:
        next_day += ONE_DAY
        day = str(next_day.day)
        d1 = "/"
        month = str(next_day.month)
        yr = str(next_day.year)
        asd = month + d1 + day + d1 + yr
        reformatted = asd
    return reformatted

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
    time.sleep(15)
tcdj1()
