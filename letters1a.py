# USE CONTROL A FOR ALL SELECTING COMMANDS!!!!!

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
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
import datetime
import holidays

driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')


def business_day():
    ONE_DAY = datetime.timedelta(days=0)
    HOLIDAYS_US = holidays.US()
    # next day = today because renaming variables is hard
    next_day = datetime.date.today() + ONE_DAY
    while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_US:
        next_day += ONE_DAY
        day = str(next_day.day)
        d1 = " "
        c1 = ","
        month = str(next_day.month)
        yr = str(next_day.year)
        if month == "1" or "01":
            month1 = "January"
        elif month == "2" or "02":
            month1 = "February"
        elif month == "3" or "03":
            month1 = "March"
        elif month == "4" or "04":
            month1 = "April"
        elif month == "5" or "05":
            month1 = "May"
        elif month == "6" or "06":
            month1 = "June"
        elif month == "7" or "07":
            month1 = "July"
        elif month == "8" or "08":
            month1 = "August"
        elif month == "9" or "09":
            month1 = "September"
        elif month == "10" or "10":
            month1 = "October"
        elif month == "11" or "11":
            month1 = "November"
        else:
            month1 = "December"
    reformatted: str = month1 + d1 + day + c1 + d1 + yr
    return reformatted


wait = WebDriverWait(driver, 10)


def open_dochub():
    # open chrome driver at pdf page and login
    driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
    driver.get(
        'https://dochub.com/law-office0961bb88/prwy2p/client-contact-letter-english?gdiExists=true')  # put here the address of your page
    # find the elements to click and interact with
    user1_string = "lawofficeofleonardmartinezdocu@gmail.com"
    pass1_string = ""
    login_xpath = "//*[@id=\"ember3\"]/div[2]/div/p/a"
    user1_xpath = "//*[@id=\"ember47\"]"
    pass_xpath = "//*[@id=\"ember48\"]"
    signin_xpath = "//*[@id=\"dh-email-login-btn\"]"
    login = driver.find_element_by_xpath(login_xpath)
    user1 = driver.find_element_by_xpath(user1_xpath)
    pass1 = driver.find_element_by_xpath(pass_xpath)
    sign_in = driver.find_element_by_xpath(signin_xpath)
    user1.send_keys(user1_string)
    pass1.send_keys(pass1_string)
    sign_in.click()


booking_global = ""


# Open_amp -> apppointment_iteration ->find defendent info -> open gmail -> booker -> open dochub -> replace_dochub_values() -> print dochub letters()

def open_amp():
    driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
    driver.get(
        "window.open('https://idc.traviscountytx.gov/nidp/idff/sso?id=35&sid=2&option=credential&sid=2&target=https%3A%2F%2Fcourts.traviscountytx.gov%2Famp%2F');")
    user1_XPATH = "//*[@id=\"main_content\"]/div[2]/form/input[1]"
    pass1_XPATH = "//*[@id=\"main_content\"]/div[2]/form/input[2]"
    access_server_XPATH = "//*[@id=\"main_content\"]/div[2]/form/div/p/input"
    # find the elements to click and interact with
    wait.until(EC.presence_of_element_located((By.XPATH, user1_XPATH)))
    user1 = driver.find_element_by_xpath(user1_XPATH)
    wait.until(EC.presence_of_element_located((By.XPATH, pass1_XPATH)))
    pass1 = driver.find_element_by_xpath(pass1_XPATH)
    wait.until(EC.presence_of_element_located((By.XPATH, access_server_XPATH)))
    access1 = driver.find_element_by_xpath(access_server_XPATH)
    user1.send_keys("Sbn13142750")
    pass1.send_keys("*")
    access1.click()
    driver.get("https://courts.traviscountytx.gov/AMP/Cases/Search")
    xpath_startdate = "//*[@id=\"start\"]"
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_startdate)))
    sd = driver.find_element_by_xpath(xpath_startdate)
    sd.clear()
    # date logic
    dt = datetime.now()
    tmrw_day_int = int(dt.day)
    tmrw_day = str(tmrw_day_int)
    tmrw_month = str(dt.month)
    tmrw_yr = str(dt.year)
    ds = "/"
    entered_date = tmrw_month + ds + tmrw_day + ds + tmrw_yr
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_startdate)))
    sd.send_keys(entered_date)
    xpath_search4 = "//*[@id=\"case-search\"]/div[3]/div[2]/ul/li[1]/button"
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_search4)))
    search4 = driver.find_element_by_xpath(xpath_search4)
    search4.click()
    appointment_iteration()  # function that searches how many appointments there are and iterates through them


def open_gmail():
    driver.get(html_1url)
    wait.until(EC.presence_of_element_located(By.XPATH, login5path))
    login5 = driver.find_element_by_xpath(login5path)
    login5.send_keys("lawofficeofleonardmartinezdocu@gmail.com")
    wait.until(EC.presence_of_element_located(By.XPATH, pass5path))
    pass5 = driver.find_element_by_xpath(pass5path)
    pass5.send_keys("")
    wait.until(EC.presence_of_element_located(By.XPATH, gmail_next_path))
    driver.find_element_by_xpath(gmail_next_path).click()


booking_global1 = ""
booking_global2 = ""
booking_global3 = ""
booking_global4 = ""
booking_global5 = ""
DOB_global1 = ""
DOB_global2 = ""
DOB_global3 = ""
DOB_global4 = ""
DOB_global5 = ""
legalname_global1 = ""
legalname_global2 = ""
legalname_global3 = ""
legalname_global4 = ""
legalname_global5 = ""
lnf_name_global1 = ""
lnf_name_global2 = ""
lnf_name_global3 = ""
lnf_name_global4 = ""
lnf_name_global5 = ""
last_name_global1 = ""
def_DOB = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[23]/span[2]"
last_name_global2 = ""
last_name_global3 = ""
last_name_global4 = ""
last_name_global5 = ""
html_1url = "https://mail.google.com/mail/?ui=html"
login5path = "//*[@id=\"identifierId\"]"
pass5path = "//*[@id=\"password\"]/div[1]/div/div[1]/input"
first_appointment_xpath = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[1]/td[5]/menu[1]/a/i"
second_appointment_xpath = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[2]/td[5]/menu[1]/a/i"

gmailht_searchbtnpath = "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/input[2]"
emailpath = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]/a/span/font[1]/font"
gmailht_searchpath = "//*[@id=\"sbq\"]"
gmail_apt_email_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[21]/span[3]"
booking_phone_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[19]/span[2]"
alternate_phone_xpath = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[20]/span[3]"
arrest_date_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[18]/span[2]"
sep = ','
gmail_next_path = "//*[@id=\"passwordNext\"]"
third_appointment_xpath = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[3]/td[5]/menu[1]/a/i"
fourth_appointment_xpath = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[4]/td[5]/menu[1]/a/i"
fifth_appointment_xpath = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[5]/td[5]/menu[1]/a/i"
booking_global_xpath = "//*[@id=\"appt-detail\"]/div[2]/div[1]/p[3]/span"


def appointment_iteration():
    wait = WebDriverWait(driver, 10)

    # define locations for angular elements in table of defendents

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def find_defendent_info():
        lnf_name_global_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[5]/span[2]"
        if (check_exists_by_xpath(first_appointment_xpath) == True):
            wait.until(EC.presence_of_element_located(By.XPATH, first_appointment_xpath))
            appointment = driver.find_element_by_xpath(first_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            booking_global1 = booker
            open_gmail()
            def booker_tool():  # must follow open gmail function call
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchpath))
                gmailht_search = driver.find_element_by_xpath(gmailht_searchpath)
                gmailht_search.click().clear().send_keys(booker)
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchbtnpath))
                gmail_srch_button = driver.find_element_by_xpath(gmailht_searchbtnpath)
                gmail_srch_button.click()
            booker_tool()
            wait.until(EC.presence_of_element_located(By.XPATH, lnf_name_global_path))
            lnf_name_global1 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            DOB_global1 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global1 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global1 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            dochub1()
        elif (check_exists_by_xpath(second_appointment_xpath) == True):
            wait.until(EC.presence_of_element_located(By.XPATH, second_appointment_xpath))
            appointment = driver.find_element_by_xpath(second_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            booking_global2 = booker
            open_gmail()

            def booker_tool():  # must follow open gmail function call
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchpath))
                gmailht_search = driver.find_element_by_xpath(gmailht_searchpath)
                gmailht_search.click().clear().send_keys(booker)
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchbtnpath))
                gmail_srch_button = driver.find_element_by_xpath(gmailht_searchbtnpath)
                gmail_srch_button.click()

            booker_tool()
            wait.until(EC.presence_of_element_located(By.XPATH, lnf_name_global_path))
            lnf_name_global2 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            DOB_global2 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global2 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global2 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            dochub2()
        elif (check_exists_by_xpath(third_appointment_xpath) == True):
            wait.until(EC.presence_of_element_located(By.XPATH, third_appointment_xpath))
            appointment = driver.find_element_by_xpath(third_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            booking_global3 = booker
            open_gmail()

            def booker_tool():  # must follow open gmail function call
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchpath))
                gmailht_search = driver.find_element_by_xpath(gmailht_searchpath)
                gmailht_search.click().clear().send_keys(booker)
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchbtnpath))
                gmail_srch_button = driver.find_element_by_xpath(gmailht_searchbtnpath)
                gmail_srch_button.click()

            booker_tool()
            wait.until(EC.presence_of_element_located(By.XPATH, lnf_name_global_path))
            lnf_name_global3 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            DOB_global3 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global3 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global3 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            dochub3()
        elif (check_exists_by_xpath(fourth_appointment_xpath) == True):
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_appointment_xpath))
            appointment = driver.find_element_by_xpath(fourth_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            booking_global4 = booker
            open_gmail()

            def booker_tool():  # must follow open gmail function call
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchpath))
                gmailht_search = driver.find_element_by_xpath(gmailht_searchpath)
                gmailht_search.click().clear().send_keys(booker)
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchbtnpath))
                gmail_srch_button = driver.find_element_by_xpath(gmailht_searchbtnpath)
                gmail_srch_button.click()

            booker_tool()
            wait.until(EC.presence_of_element_located(By.XPATH, lnf_name_global_path))
            lnf_name_global4 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            DOB_global4 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global4 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global4 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            dochub4()
        elif (check_exists_by_xpath(fifth_appointment_xpath) == True):
            wait.until(EC.presence_of_element_located(By.XPATH, fifth_appointment_xpath))
            appointment = driver.find_element_by_xpath(fifth_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            booking_global5 = booker
            open_gmail()
            def booker_tool():  # must follow open gmail function call
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchpath))
                gmailht_search = driver.find_element_by_xpath(gmailht_searchpath)
                gmailht_search.click().clear().send_keys(booker)
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchbtnpath))
                gmail_srch_button = driver.find_element_by_xpath(gmailht_searchbtnpath)
                gmail_srch_button.click()
            booker_tool()
            wait.until(EC.presence_of_element_located(By.XPATH, lnf_name_global_path))
            lnf_name_global5 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            DOB_global5 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global5 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global5 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            dochub5()
        
        else:
            pass

    find_defendent_info()


entered_date = business_day()

# define rendered locations on webpage for pdf
edit_template_path = "//*[@id=\"js-toolbar\"]/div[1]/ul[3]/li[1]/button"
lnf_name_global_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[5]/span[2]"
date_xpath = "//*[@id=\"ember776\"]"
printer_hub_selector = "#ember540"
printer_path = "//*[@id=\"ember540\"]"
defendent_lnf_name_xpath = "//*[@id=\"ember492\"]"
defendent_name_xpath = "//*[@id=\"ember499\"]"
DOB_XPATH = "//*[@id=\"ember502\"]"
booking_xpath = "//*[@id=\"ember129\"]/div[2]"
last_name_xpath = "//*[@id=\"ember512\"]"

documents_xpath = "//*[@id=\"appt_actions\"]/ul/li[1]/a"


def dochub1():
    open_dochub()
    wait.until(EC.presence_of_element_located(By.XPATH, edit_template_path))
    driver.find_element_by_xpath(edit_template_path).click()
    wait.until(EC.presence_of_element_located(By.XPATH, date_xpath))
    # define elements in webpage pdf
    date = driver.find_element_by_xpath(date_xpath)
    date.clear().send_keys(business_day())
    defendent_lnf_name = driver.find_element_by_xpath(defendent_lnf_name_xpath)
    defendent_lnf_name.clear().send_keys(lnf_name_global1)
    defendent_name = driver.find_element_by_xpath(defendent_name_xpath)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    defendent_name.clear().send_keys(legalname_global1)
    DOB = driver.find_element_by_xpath(DOB_XPATH)
    DOB.clear().send_keys(DOB_global1)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    booking = driver.find_element_by_xpath(booking_xpath)
    booking.clear().send_keys(booking_global1)
    last_name = driver.find_element_by_xpath(last_name_xpath)
    last_name.clear().send_keys(last_name_global1)
    wait.until(EC.presence_of_element_located(By.XPATH, printer_path))
    print1 = driver.find_element_by_xpath(printer_path)
    print1.click()
    print2 = "//*[@id=\"print-header\"]/div/button[1]"
    wait.until(EC.presence_of_element_located(By.XPATH, print2))
    printy = driver.find_element_by_xpath(print2).click()
    time.sleep(3)

def dochub2():
    open_dochub()
    wait.until(EC.presence_of_element_located(By.XPATH, edit_template_path))
    driver.find_element_by_xpath(edit_template_path).click()
    wait.until(EC.presence_of_element_located(By.XPATH, date_xpath))
    # define elements in webpage pdf
    date = driver.find_element_by_xpath(date_xpath)
    date.clear().send_keys(business_day())
    defendent_lnf_name = driver.find_element_by_xpath(defendent_lnf_name_xpath)
    defendent_lnf_name.clear().send_keys(lnf_name_global2)
    defendent_name = driver.find_element_by_xpath(defendent_name_xpath)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    defendent_name.clear().send_keys(legalname_global2)
    DOB = driver.find_element_by_xpath(DOB_XPATH)
    DOB.clear().send_keys(DOB_global2)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    booking = driver.find_element_by_xpath(booking_xpath)
    booking.clear().send_keys(booking_global2)
    last_name = driver.find_element_by_xpath(last_name_xpath)
    last_name.clear().send_keys(last_name_global2)
    wait.until(EC.presence_of_element_located(By.XPATH, printer_path))
    print1 = driver.find_element_by_xpath(printer_path)
    print1.click()
    print2 = "//*[@id=\"print-header\"]/div/button[1]"
    wait.until(EC.presence_of_element_located(By.XPATH, print2))
    printy = driver.find_element_by_xpath(print2).click()
    time.sleep(3)
def dochub3():
    open_dochub()
    wait.until(EC.presence_of_element_located(By.XPATH, edit_template_path))
    driver.find_element_by_xpath(edit_template_path).click()
    wait.until(EC.presence_of_element_located(By.XPATH, date_xpath))
    # define elements in webpage pdf
    date = driver.find_element_by_xpath(date_xpath)
    date.clear().send_keys(business_day())
    defendent_lnf_name = driver.find_element_by_xpath(defendent_lnf_name_xpath)
    defendent_lnf_name.clear().send_keys(lnf_name_global3)
    defendent_name = driver.find_element_by_xpath(defendent_name_xpath)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    defendent_name.clear().send_keys(legalname_global3)
    DOB = driver.find_element_by_xpath(DOB_XPATH)
    DOB.clear().send_keys(DOB_global3)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    booking = driver.find_element_by_xpath(booking_xpath)
    booking.clear().send_keys(booking_global3)
    last_name = driver.find_element_by_xpath(last_name_xpath)
    last_name.clear().send_keys(last_name_global3)
    wait.until(EC.presence_of_element_located(By.XPATH, printer_path))
    print1 = driver.find_element_by_xpath(printer_path)
    print1.click()
    print2 = "//*[@id=\"print-header\"]/div/button[1]"
    wait.until(EC.presence_of_element_located(By.XPATH, print2))
    printy = driver.find_element_by_xpath(print2).click()
    time.sleep(3)    
def dochub4():
    open_dochub()
    wait.until(EC.presence_of_element_located(By.XPATH, edit_template_path))
    driver.find_element_by_xpath(edit_template_path).click()
    wait.until(EC.presence_of_element_located(By.XPATH, date_xpath))
    # define elements in webpage pdf
    date = driver.find_element_by_xpath(date_xpath)
    date.clear().send_keys(business_day())
    defendent_lnf_name = driver.find_element_by_xpath(defendent_lnf_name_xpath)
    defendent_lnf_name.clear().send_keys(lnf_name_global4)
    defendent_name = driver.find_element_by_xpath(defendent_name_xpath)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    defendent_name.clear().send_keys(legalname_global4)
    DOB = driver.find_element_by_xpath(DOB_XPATH)
    DOB.clear().send_keys(DOB_global4)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    booking = driver.find_element_by_xpath(booking_xpath)
    booking.clear().send_keys(booking_global4)
    last_name = driver.find_element_by_xpath(last_name_xpath)
    last_name.clear().send_keys(last_name_global4)
    wait.until(EC.presence_of_element_located(By.XPATH, printer_path))
    print1 = driver.find_element_by_xpath(printer_path)
    print1.click()
    print2 = "//*[@id=\"print-header\"]/div/button[1]"
    wait.until(EC.presence_of_element_located(By.XPATH, print2))
    printy = driver.find_element_by_xpath(print2).click()
    time.sleep(3)
def dochub5():
    open_dochub()
    wait.until(EC.presence_of_element_located(By.XPATH, edit_template_path))
    driver.find_element_by_xpath(edit_template_path).click()
    wait.until(EC.presence_of_element_located(By.XPATH, date_xpath))
    # define elements in webpage pdf
    date = driver.find_element_by_xpath(date_xpath)
    date.clear().send_keys(business_day())
    defendent_lnf_name = driver.find_element_by_xpath(defendent_lnf_name_xpath)
    defendent_lnf_name.clear().send_keys(lnf_name_global5)
    defendent_name = driver.find_element_by_xpath(defendent_name_xpath)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    defendent_name.clear().send_keys(legalname_global5)
    DOB = driver.find_element_by_xpath(DOB_XPATH)
    DOB.clear().send_keys(DOB_global5)
    wait.until(EC.presence_of_element_located(By.XPATH, defendent_name_xpath))
    booking = driver.find_element_by_xpath(booking_xpath)
    booking.clear().send_keys(booking_global5)
    last_name = driver.find_element_by_xpath(last_name_xpath)
    last_name.clear().send_keys(last_name_global5)
    wait.until(EC.presence_of_element_located(By.XPATH, printer_path))
    print1 = driver.find_element_by_xpath(printer_path)
    print1.click()
    print2 = "//*[@id=\"print-header\"]/div/button[1]"
    wait.until(EC.presence_of_element_located(By.XPATH, print2))
    printy = driver.find_element_by_xpath(print2).click()
    time.sleep(3)    
open_amp()
time.sleep(15 * 60)
driver.close()
