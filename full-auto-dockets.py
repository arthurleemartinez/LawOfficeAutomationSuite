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
    ONE_DAY = datetime.timedelta(days=1)
    HOLIDAYS_US = holidays.US()
    global next_day
    next_day = datetime.date.today() + ONE_DAY
    while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_US:
        next_day += ONE_DAY
    return next_day
next_business_day()
def converto():
    day = str(next_day.day)
    d1 = "/"
    month = str(next_day.month)
    yr = str(next_day.year)
    asd = month + d1 + day + d1 + yr
    return asd



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
pass1.send_keys("")
access1.click()
urlform2 = "https://www5.elawsoftware.com/1217/1217_Criminal.nsf/DocketReportSelection?OpenForm&t=1"
urlform3 = "https://www5.elawsoftware.com/1217/1217_Criminal.nsf/DocketReportSelection?OpenForm&Seq=1&t=1"
driver.get(urlform2)
entered_date = converto()
docket_date1 = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[6]/td/font[1]/input")
docket_date2 = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[6]/td/font[2]/input")

def replace_values2():
    docket_date1.clear()
    docket_date1.send_keys(entered_date)
    docket_date2.clear()
    docket_date2.send_keys(entered_date)
    keyboard.press_and_release('enter')
replace_values2()

urlform3_xpath = "//*[@id=\"menu0\"]"
wait = WebDriverWait(driver, 10)
xpath_texto = "/html/body/form/div[3]/table/tbody/tr[1]/td/div/b/font"
wait.until(EC.presence_of_element_located((By.XPATH, xpath_texto)))
texto = driver.find_element_by_xpath(xpath_texto)
texto.click()
wait.until(EC.presence_of_element_located((By.XPATH, urlform3_xpath)))

driver.find_element_by_xpath(urlform3_xpath).click()

def print2():
    time.sleep(2)
    keyboard.press_and_release('ctrl+shift+p')
    time.sleep(5)
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')

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
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')
    time.sleep(15)
    driver.close()
tcdj1()
