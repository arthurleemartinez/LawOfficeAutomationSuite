import urllib3
import selenium
import requests
from selenium.webdriver.common.keys import Keys
import webbrowser
import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup

# specify the url for travis appointments
webbrowser.open('https://publiccourts.traviscountytx.gov/dsa/#/')

#ELEMENTAL XPATHS
LASTNAME_ID = "att-last-name"
LASTNAME_XPATH = "//*[@id=\"att-last-name\"]"
FIRSTNAME_ID = "att-first-name"
FIRSTNAME_XPATH = "//*[@id=\"att-first-name\"]"
DATES_XPATH = "//*[@id=\"quick-date\"]/option[1]"
SUBMIT_XPATH = "/html/body/div/div/div/form/fieldset/div[1]/div[3]/button"
CHECKBOX_XPATH = "/html/body/div/div/div/div[4]/div[2]/div/div/div[1]/div[1]/input"
PRINT_XPATH = "/html/body/div/div/div/form/fieldset/div[3]/div[1]/button"

driver = webdriver.Chrome()
driver.get('https://publiccourts.traviscountytx.gov/dsa/#/')#put here the address of your page
elem_attorney = driver.find_elements_by_xpath("/html/body/div/div/div/div[3]/div/span[2]/button")#put here the content you have put in Notepad, ie the XPath
elem_attorney.click()
#elem_attorney.sendKeys(Keys.ENTER);

#find the elements to click and interact with
lnbox = driver.find_element_by_xpath(LASTNAME_XPATH)
fnbox = driver.find_element_by_xpath(FIRSTNAME_XPATH)
search = driver.find_element_by_xpath(SUBMIT_XPATH)
dates = driver.find_element_by_xpath(DATES_XPATH)
checker = driver.find_element_by_xpath(CHECKBOX_XPATH)
print = driver.find_element_by_xpath(PRINT_XPATH)

#send name and set date
dates.click()
lnbox.send_keys("Martinez")
fnbox.send_keys("Leonard")

#Search and select defendants for attorney
search.click()
checker.click()
#Print defendants
print.click()
keyboard.press_and_release(Keys.ENTER)
keyboard.press_and_release(Keys.ENTER)
driver.close()
