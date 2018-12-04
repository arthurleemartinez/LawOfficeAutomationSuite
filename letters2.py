# USE CONTROL A FOR ALL SELECTING COMMANDS!!!!!

from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
from selenium import webdriver
import datetime
from holidays import WEEKEND, US
import re


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
global_datenamez1 = ""
global_datenamez2 = ""
global_datenamez3 = ""
global_datenamez4 = ""
global_datenamez5 = ""
global_homephone_1 = ""
global_homephone_2 = ""
global_homephone_3 = ""
global_homephone_4 = ""
global_homephone_5 = ""
global_alternate_1 = ""
global_alternate_2 = ""
global_alternate_3 = ""
global_alternate_4 = ""
global_alternate_5 = ""
global_email1 = ""
global_email2 = ""
global_email3 = ""
global_email4 = ""
global_email5 = ""
firstline_address1 = ""
firstline_address2 = ""
firstline_address3 = ""
firstline_address4 = ""
firstline_address5 = ""
globalcity_1 = ""
globalcity_2 = ""
globalcity_3 = ""
globalcity_4 = ""
globalcity_5 = ""
globalstate_1 = ""
globalstate_2 = ""
pn1 = "Mr. "
global_pronoun = pn1
pn2 = "Ms. "
global_pronoun_1 = ""
global_pronoun_2 = ""
path_print_def = "//*[@id=\"print-header\"]/div/button[2]"
global_pronoun_3 = ""
global_pronoun_4 = ""
normal_pages_path = "//*[@id=\"page-settings\"]/div[2]/div/div[1]/label/input"
global_pronoun_5 = ""
first_case_number = ""
second_case_number = ""
third_case_number = ""
fourth_case_number = ""
fifth_case_number = ""
first_case_court = ""
second_case_court = ""
third_case_court = ""
fourth_case_court = ""
fifth_case_court = ""
first_case_date = ""
second_case_date = ""
third_case_date = ""
fourth_case_date = ""
fifth_case_date = ""
booker = ""
first_case_time = ""
second_case_time = ""
third_case_time = ""
fourth_case_time = ""
fifth_case_time = ""
first_case_offense = ""
second_case_offense = ""
third_case_offense = ""
fourth_case_offense = ""
fifth_case_offense = ""
orig_date = "Date:"
orig_legalname = "v."
global_lastName = ""
orig_lnf = "Defendant:"
custom_pages_path = "//*[@id=\"page-settings-custom-input\"]"
orig_dob = "DOB:"
orig_booking = "Booking No."
orig_salutations = "Dear"
globalstate_3 = ""
globalstate_4 = ""
globalstate_5 = ""
globalzip_1 = ""
globalzip_2 = ""
globalzip_3 = ""
globalzip_4 = ""
globalzip_5 = ""
global_booking_address1 = ""
global_booking_address2 = ""
global_booking_address3 = ""
global_booking_address4 = ""
global_booking_address5 = ""
lnf_name_global5 = ""
gender_global1 = ""
gender_global2 = ""
gender_global3 = ""
gender_global4 = ""
legal = ""
birthday = ""
lnf = ""
salutations = ""
lasto = ""
booking44 = ""
gender_global5 = ""
jail_status_global1 = ""
jail_status_global2 = ""
jail_status_global3 = ""
jail_status_global4 = ""
jail_status_global5 = ""
jail_status = ""
last_name_global1 = ""
def_DOB = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[23]/span[2]"
last_name_global2 = ""
last_name_global3 = ""
last_name_global4 = ""
last_name_global5 = ""
sep = ','
gmail_next_path = "//*[@id=\"passwordNext\"]"
third_appointment_xpath = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[3]/td[5]/menu[1]/a/i"
fourth_appointment_xpath = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[4]/td[5]/menu[1]/a/i"
fifth_appointment_xpath = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[5]/td[5]/menu[1]/a/i"
booking_global_xpath: str = "//*[@id=\"appt-detail\"]/div[2]/div[1]/p[3]/span"
gender_global_path = "//*[@id=\":eq\"]/div[1]/div[2]/div[2]/div/div[2]/div/p[24]/span[2]"
sheriff_booking_path = "//*[@id=\"InmateCharges\"]/text()[1]"
documents_xpath = "//*[@id=\"appt_actions\"]/ul/li[1]/a"
open_docs_url = "https://docs.google.com/document/d/15Qk0UM2f9G7glB0BOL-hPeN86o_YN9YjfRvj53riBMQ/edit?usp=sharing"
sign_in_docs_path = "//*[@id=\"gb\"]/div/div/a"
docs_email_path = "//*[@id=\"identifierId\"]"
docs_pass_path = "//*[@id=\"password\"]/div[1]/div/div[1]/input"
docs_next_path = "//*[@id=\"passwordNext\"]"
more_options_path = "//*[@id=\"docs-findbar-button-more-options\"]"
firstname = ""
user1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[3]/input"
pass1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[2]/td[3]/input"
access_server_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[3]/td[1]/div/input"
html_1url = "https://mail.google.com/mail/?ui=html"
signin_gmail_path = "/html/body/nav/div/a[2]"
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
booking_address_xpath = "//*[@id=\":f0\"]/div[1]/div[2]/div[2]/div/div[2]/div/p[17]/span[2]"
defendant_notes_xpath = "//*[@id=\":f0\"]/div[1]/div[2]/div[2]/div/div[2]/div/p[28]/span[1]/text()"
driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
pass00 = "LM13142750"
user01 = "Leonard.martinez"
pass01 = "51698"
user00 = "lawofficeofleonardmartinezdocu@gmail.com"
case_elaw_save_close_path: str = "/html/body/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/a[1]"

global wait
wait = WebDriverWait(driver, 10)
global am9
am9 = "9:00 AM"
global am830
am830 = "8:30 AM"

def sign_elaw_open_new_client():
    driver.get(elaw_1_url)
    user1 = driver.find_element_by_xpath(user1_XPATH)
    pass1 = driver.find_element_by_xpath(pass1_XPATH)
    access1 = driver.find_element_by_xpath(access_server_XPATH)
    user1.send_keys(user01)
    pass1.send_keys(pass01)
    access1.click()
    create_hover_path = "//*[@id=\"qmim2\"]"
    hover = ActionChains(driver).move_to_element(create_hover_path)
    hover.perform()
    new_apt_path: str = "//*[@id=\"qmitemhl2_0\"]"
    wait.until(ec.presence_of_element_located(By.XPATH, new_apt_path))
    new_apt = driver.find_element_by_xpath(new_apt_path)
    new_apt.click()

def sign_elaw_open_old_client():
    path_create2 = "//*[@id=\"qmim2\"]"
    path_open_create_case = "//*[@id=\"qmitemhl2_0\"]"
    hover = ActionChains(driver).move_to_element(path_create2)
    hover.perform()
    wait.until(ec.presence_of_element_located(By.XPATH, path_open_create_case))
    open_create_case = driver.find_element_by_xpath(path_open_create_case)
    open_create_case.click()


def business_day():
    one_day = datetime.timedelta(days=0)
    holidays_us = US()
    # next day = today because renaming variables is hard
    next_day = datetime.date.today() + one_day
    while next_day.weekday() in WEEKEND or next_day in holidays_us:
        next_day += one_day
        day = str(next_day.day)
        global d1
        d1 = " "
        global c1
        c1: str = ","
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

entered_date = business_day()
wait = WebDriverWait(driver, 10)

booking_global = ""


def open_gmail():
    driver.get(html_1url)
    signin_gmail = driver.find_element_by_xpath(signin_gmail_path)
    wait.until(ec.presence_of_element_located(By.XPATH, signin_gmail_path))
    signin_gmail.click()
    wait.until(ec.presence_of_element_located(By.XPATH, login5path))
    login5 = driver.find_element_by_xpath(login5path)
    login5.send_keys(user00)
    wait.until(ec.presence_of_element_located(By.XPATH, pass5path))
    pass5 = driver.find_element_by_xpath(pass5path)
    pass5.send_keys(pass00)
    wait.until(ec.presence_of_element_located(By.XPATH, gmail_next_path))
    driver.find_element_by_xpath(gmail_next_path).click()
    driver.get(html_1url)



def open_docs():
    driver.get(open_docs_url)
    wait.until(ec.presence_of_element_located(By.XPATH, sign_in_docs_path))
    sign_in_docs = driver.find_element_by_xpath(sign_in_docs_path)
    sign_in_docs.click()
    wait.until(ec.presence_of_element_located(By.XPATH, docs_email_path))
    docs_email1 = driver.find_element_by_xpath(docs_email_path)
    docs_email1.send_keys(user00)
    wait.until(ec.presence_of_element_located(By.XPATH, docs_pass_path))
    docs_pass = driver.find_element_by_xpath(docs_pass_path)
    docs_pass.send_keys(pass00)
    wait.until(ec.presence_of_element_located(By.XPATH, docs_next_path))
    driver.find_element_by_xpath(docs_next_path).click()


def getpronoun():
    if gender_global1 == "Female":
        global_pronoun = pn2
    elif gender_global2 == "Female":
        global_pronoun = pn2
    elif gender_global3 == "Female":
        global_pronoun = pn2
    elif gender_global4 == "Female":
        global_pronoun = pn2
    elif gender_global5 == "Female":
        global_pronoun = pn2
    else:
        global_pronoun = pn1
    return global_pronoun

def replace_doc_values_and_print():
    getpronoun()
    global global_pronoun
    global_pronoun = getpronoun()
    
    open_docs()

    def get_legal():
        if booking_global1 == booker:
            legal = legalname_global1
        elif booking_global2 == booker:
            legal = legalname_global2
        elif booking_global3 == booker:
            legal = legalname_global3
        elif booking_global4 == booker:
            legal = legalname_global4
        elif booking_global5 == booker:
            legal = legalname_global5
        return legal
    global legal
    legal = get_legal()

    def get_birthday():
        if booking_global1 == booker:
            birthday = DOB_global1
        elif booking_global2 == booker:
            birthday = DOB_global2
        elif booking_global3 == booker:
            birthday = DOB_global3
        elif booking_global4 == booker:
            birthday = DOB_global4
        elif booking_global5 == booker:
            birthday = DOB_global5
        return birthday
    birthday = get_birthday()

    def get_lnf():
        if booking_global1 == booker:
            lnf = lnf_name_global1
        elif booking_global2 == booker:
            lnf = lnf_name_global2
        elif booking_global3 == booker:
            lnf = lnf_name_global3
        elif booking_global4 == booker:
            lnf = lnf_name_global4
        elif booking_global5 == booker:
            lnf = lnf_name_global5
        return lnf
    global lnf
    lnf = get_lnf()

    def get_lasto():
        if booking_global1 == booker:
            lasto = last_name_global1
        elif booking_global2 == booker:
            lasto = last_name_global2
        elif booking_global3 == booker:
            lasto = last_name_global3
        elif booking_global4 == booker:
            lasto = last_name_global4
        elif booking_global5 == booker:
            lasto = last_name_global5
        return lasto
    global lasto
    lasto = get_lasto()

    def get_firstname():
        if booking_global1 == booker:
            firstname = global_firstname1
        elif booking_global2 == booker:
            firstname = global_firstname2
        elif booking_global3 == booker:
            firstname = global_firstname3
        elif booking_global4 == booker:
            firstname = global_firstname4
        elif booking_global5 == booker:
            firstname = global_firstname5
        return firstname
    global firstname
    firstname = get_firstname()

    def getJailStatus():
        sheriff_url = "https://public.co.travis.tx.us/sips/default.aspx"
        sheriff_lastname_path = "//*[@id=\"LastName\"]"
        sheriff_firstname_path = "//*[@id=\"FirstInitial\"]"
        sheriff_search_path = "//*[@id=\"SubmitNameSearch\"]"
        wait.until(ec.presence_of_element_located(By.XPATH, sheriff_lastname_path))
        sheriff_lastname = driver.find_element_by_xpath(sheriff_lastname_path)
        sheriff_lastname.send_keys(lasto)
        wait.until(ec.presence_of_element_located(By.XPATH, sheriff_firstname_path))
        sherrif_firstname = driver.find_element_by_xpath(sheriff_firstname_path)
        sherrif_firstname.send_keys(firstname)
        wait.until(ec.presence_of_element_located(By.XPATH, sheriff_search_path))
        sheriff_search = driver.find_element_by_xpath(sheriff_search_path)
        sheriff_search.click()

        def level2():
            path_list0 = "//*[@id=\"ListOfInmates_0\"]"
            path_submit0 = "//*[@id=\"SubmitInmate\"]"
            path_notfound0 = "//*[@id=\"notFound\"]"

            def check_exists_by_xpath(xpath):
                try:
                    driver.find_element_by_xpath(xpath)
                except NoSuchElementException:
                    return False
                return True

            if check_exists_by_xpath(path_list0) == True:
                wait.until(EC.presence_of_element_located(By.XPATH, path_list0))
                driver.find_element_by_xpath(path_list0).click()
                submit = driver.find_element_by_xpath(path_submit0)
                wait.until(EC.presence_of_element_located(By.XPATH, path_list0))
                submit.click()
                wait.until(EC.presence_of_element_located(By.XPATH, sheriff_booking_path))
                sheriff_booking = driver.find_element_by_xpath(sheriff_booking_path).text
                if sheriff_booking == booker:
                    keyboard.press_and_release("ctrl+p")
                    keyboard.press_and_release("enter")
                    jail_status = "Yes"
                    return jail_status
                    time.sleep(5)

            else:
                jail_status = "No"
                return jail_status
        global jail_status
        jail_status = level2()
        return jail_status
    getJailStatus()

    # 44 suffix means final replacement values per defendant
    date44 = orig_date + " " + entered_date
    legalname44 = orig_legalname + " " + legal
    birthday44 = orig_dob + " " + birthday
    lnf44 = orig_lnf + " " + lnf
    salutations44 = orig_salutations + " " + global_pronoun + lasto + ","
    booking44 = orig_booking + " " + booker
    open_docs()
    keyboard.press_and_release('ctrl+f')
    path_closer1 = "/html/body/div[61]/div[1]/span[2]"
    path_replace_what: str = "//*[@id=\"docs-findandreplacedialog-input\"]"
    path_replace_with: str = "//*[@id=\"docs-findandreplacedialog-replace-input\"]"
    path_replace_all: str = "//*[@id=\"docs-findandreplacedialog-button-replace-all\"]"
    # date44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what = driver.find_element_by_xpath(path_replace_what)
    replace_what.clear()
    replace_what.send_keys(orig_date)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with = driver.find_element_by_xpath(path_replace_with)
    replace_with.clear()
    replace_with.send_keys(date44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all = driver.find_element_by_xpath(path_replace_all)
    replace_all.click()
    # legalname44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_legalname)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(legalname44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    # birthday44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_dob)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(birthday44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    # lnf44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_lnf)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(lnf44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    # salutations44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_salutations)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(salutations44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    # booking44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_booking)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(booking44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    driver.find_element_by_xpath(path_closer1).click()

    # start printing
    keyboard.press_and_release("ctrl+p")
    wait.until(EC.presence_of_element_located(By.XPATH, normal_pages_path))
    normal_pages = driver.find_element_by_xpath(normal_pages_path)
    normal_pages.click()
    wait.until(EC.presence_of_element_located(By.XPATH, path_print_def))
    print_def = driver.find_element_by_xpath(path_print_def)
    print_def.click()
    time.sleep(2.5)
    keyboard.press_and_release("ctrl+p")
    wait.until(EC.presence_of_element_located(By.XPATH, custom_pages_path))
    custom_pages = driver.find_element_by_xpath(custom_pages_path)
    custom_pages.click()
    custom_pages.send_keys("1")
    wait.until(EC.presence_of_element_located(By.XPATH, path_print_def))
    print_def.click()
    time.sleep(2.5)
    # RESET VALUES TO DEFAULT
    # date44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what = driver.find_element_by_xpath(path_replace_what)
    replace_what.clear()
    replace_what.send_keys(date44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with = driver.find_element_by_xpath(path_replace_with)
    replace_with.clear()
    replace_with.send_keys(orig_date)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all = driver.find_element_by_xpath(path_replace_all)
    replace_all.click()
    # legalname44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(legalname44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_legalname)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    # birthday44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(birthday44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_dob)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    # lnf44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(lnf44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_lnf)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    # salutations44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(salutations44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_salutations)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    # booking44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(booking44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_booking)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    driver.find_element_by_xpath(path_closer1).click()



elaw_1_url = "https://www5.elawsoftware.com/"
global_one_exists = 0
global_2_exists = 0
pe = " (A)"
global_3_exists = 0
global_4_exists = 0
global_5_exists = 0
global no_hyphens_dob_global4, no_hyphens_dob_global4, no_hyphens_dob_global3, no_hyphens_dob_global2
no_hyphens_dob_global4 = re.sub('-', '', DOB_global4)



third_case_court_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[3]/tbody/tr/td[4]/p/span"


def appointment_iteration():

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def get_case_details():


        first_case_number_path: str = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[2]/tbody/tr/td[2]/p/span"
        second_case_number_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[3]/tbody/tr/td[2]/p/span"
        third_case_number_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[4]/tbody/tr/td[2]/p/span"
        fourth_case_number_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[5]/tbody/tr/td[2]/p/span"
        fifth_case_number_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[6]/tbody/tr/td[2]/p/span"
        first_case_court_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[2]/tbody/tr/td[4]/p/span"
        second_case_court_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[3]/tbody/tr/td[4]/p/span"
        fourth_case_court_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[4]/tbody/tr/td[4]/p/span"
        fourth_case_court_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[5]/tbody/tr/td[4]/p/span"
        fifth_case_court_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[6]/tbody/tr/td[4]/p/span"
        first_case_date_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[2]/tbody/tr/td[5]/p/span"
        second_case_date_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[3]/tbody/tr/td[5]/p/span"
        third_case_date_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[4]/tbody/tr/td[5]/p/span"
        fourth_case_date_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[5]/tbody/tr/td[5]/p/span"
        fifth_case_date_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[6]/tbody/tr/td[5]/p/span"
        first_case_time_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[2]/tbody/tr/td[6]/p/span"
        second_case_time_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[3]/tbody/tr/td[6]/p/span"
        third_case_time_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[4]/tbody/tr/td[6]/p/span"
        fourth_case_time_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[5]/tbody/tr/td[6]/p/span"
        fifth_case_time_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[6]/tbody/tr/td[6]/p/span"
        first_case_offense_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[2]/tbody/tr/td[7]/p/span"
        second_case_offense_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[3]/tbody/tr/td[7]/p/span"
        third_case_offense_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[4]/tbody/tr/td[7]/p/span"
        fourth_case_offense_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[5]/tbody/tr/td[7]/p/span"
        fifth_case_offense_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/table[6]/tbody/tr/td[7]/p/span"

        def only_one_case_exists():

            wait.until(EC.presence_of_element_located(By.XPATH, first_case_number_path))
            global first_case_number
            first_case_number = driver.find_element_by_xpath(first_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_date_path))
            global first_case_date
            first_case_date = driver.find_element_by_xpath(first_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_offense_path))
            global first_case_offense
            first_case_offense = driver.find_element_by_xpath(first_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_court_path))
            global first_case_court
            first_case_court = driver.find_element_by_xpath(first_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_time_path))
            global first_case_time
            first_case_time = driver.find_element_by_xpath(first_case_time_path).text


        def only_two_cases_exist():
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_number_path))
            global first_case_number
            first_case_number = driver.find_element_by_xpath(first_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_date_path))
            global first_case_date
            first_case_date = driver.find_element_by_xpath(first_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_offense_path))
            global first_case_offense
            first_case_offense = driver.find_element_by_xpath(first_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_court_path))
            global first_case_court
            first_case_court = driver.find_element_by_xpath(first_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_time_path))
            global first_case_time
            first_case_time = driver.find_element_by_xpath(first_case_time_path).text
            #### 2 OF 2
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_number_path))
            global second_case_number
            second_case_number = driver.find_element_by_xpath(second_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_date_path))
            global second_case_date
            second_case_date = driver.find_element_by_xpath(second_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_offense_path))
            global second_case_offense
            second_case_offense = driver.find_element_by_xpath(second_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_court_path))
            global second_case_court
            second_case_court = driver.find_element_by_xpath(second_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_time_path))
            global second_case_time
            second_case_time = driver.find_element_by_xpath(second_case_time_path).text

        def only_three_cases_exist():
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_number_path))
            global first_case_number
            first_case_number = driver.find_element_by_xpath(first_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_date_path))
            global first_case_date
            first_case_date = driver.find_element_by_xpath(first_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_offense_path))
            global first_case_offense
            first_case_offense = driver.find_element_by_xpath(first_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_court_path))
            global first_case_court
            first_case_court = driver.find_element_by_xpath(first_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_time_path))
            global first_case_time
            first_case_time = driver.find_element_by_xpath(first_case_time_path).text
            #### 2 OF 2
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_number_path))
            global second_case_number
            second_case_number = driver.find_element_by_xpath(second_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_date_path))
            global second_case_date
            second_case_date = driver.find_element_by_xpath(second_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_offense_path))
            global second_case_offense
            second_case_offense = driver.find_element_by_xpath(second_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_court_path))
            global second_case_time
            global second_case_court
            second_case_court = driver.find_element_by_xpath(second_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_time_path))
            global second_case_time
            second_case_time = driver.find_element_by_xpath(second_case_time_path).text
            #### 3 OF 3
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_number_path))
            global third_case_number
            third_case_number = driver.find_element_by_xpath(third_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_date_path))
            global third_case_date
            third_case_date = driver.find_element_by_xpath(third_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_offense_path))
            global third_case_offense
            third_case_offense = driver.find_element_by_xpath(third_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_court_path))
            global third_case_court
            third_case_court = driver.find_element_by_xpath(third_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_time_path))
            global third_case_time
            third_case_time = driver.find_element_by_xpath(third_case_time_path).text
        def four_cases_exist():
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_number_path))
            global first_case_number
            first_case_number = driver.find_element_by_xpath(first_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_date_path))
            global first_case_date
            first_case_date = driver.find_element_by_xpath(first_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_offense_path))
            global first_case_offense
            first_case_offense = driver.find_element_by_xpath(first_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_court_path))
            global first_case_court
            first_case_court = driver.find_element_by_xpath(first_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_time_path))
            global first_case_time
            first_case_time = driver.find_element_by_xpath(first_case_time_path).text
            #### 2 OF 2
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_number_path))
            global second_case_number
            second_case_number = driver.find_element_by_xpath(second_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_date_path))
            global second_case_date
            second_case_date = driver.find_element_by_xpath(second_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_offense_path))
            global second_case_offense
            second_case_offense = driver.find_element_by_xpath(second_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_court_path))
            global second_case_court
            second_case_court = driver.find_element_by_xpath(second_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_time_path))
            global second_case_time
            second_case_time = driver.find_element_by_xpath(second_case_time_path).text
            #### 3 OF 3
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_number_path))
            global third_case_number
            third_case_number = driver.find_element_by_xpath(third_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_date_path))
            global third_case_date
            third_case_date = driver.find_element_by_xpath(third_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_offense_path))
            global third_case_offense
            third_case_offense = driver.find_element_by_xpath(third_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_court_path))
            global third_case_court
            third_case_court = driver.find_element_by_xpath(third_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_time_path))
            global third_case_time
            third_case_time = driver.find_element_by_xpath(third_case_time_path).text
            #### 4 OF 4
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_number_path))
            global fourth_case_number
            fourth_case_number = driver.find_element_by_xpath(fourth_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_date_path))
            global fourth_case_date
            fourth_case_date = driver.find_element_by_xpath(fourth_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_offense_path))
            global fourth_case_offense
            fourth_case_offense = driver.find_element_by_xpath(fourth_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_court_path))
            global fourth_case_court
            fourth_case_court = driver.find_element_by_xpath(fourth_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_time_path))
            global fourth_case_time
            fourth_case_time = driver.find_element_by_xpath(fourth_case_time_path).text

        def five_cases_exist():
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_number_path))
            global first_case_number
            first_case_number = driver.find_element_by_xpath(first_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_date_path))
            global first_case_date
            first_case_date = driver.find_element_by_xpath(first_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_offense_path))
            global first_case_offense
            first_case_offense = driver.find_element_by_xpath(first_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_court_path))
            global first_case_court
            first_case_court = driver.find_element_by_xpath(first_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, first_case_time_path))
            global first_case_time
            first_case_time = driver.find_element_by_xpath(first_case_time_path).text
            #### 2 OF 2
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_number_path))
            global second_case_number
            second_case_number = driver.find_element_by_xpath(second_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_date_path))
            global second_case_date
            second_case_date = driver.find_element_by_xpath(second_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_offense_path))
            global second_case_offense
            second_case_offense = driver.find_element_by_xpath(second_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_court_path))
            global second_case_court
            second_case_court = driver.find_element_by_xpath(second_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, second_case_time_path))
            global second_case_time
            second_case_time = driver.find_element_by_xpath(second_case_time_path).text
            #### 3 OF 3
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_number_path))
            global third_case_number
            third_case_number = driver.find_element_by_xpath(third_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_date_path))
            global third_case_date
            third_case_date = driver.find_element_by_xpath(third_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_offense_path))
            global third_case_offense
            third_case_offense = driver.find_element_by_xpath(third_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_court_path))
            global third_case_court
            third_case_court = driver.find_element_by_xpath(third_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, third_case_time_path))
            global third_case_time
            third_case_time = driver.find_element_by_xpath(third_case_time_path).text
            #### 4 OF 4
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_number_path))
            global fourth_case_number
            fourth_case_number = driver.find_element_by_xpath(fourth_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_date_path))
            global fourth_case_date
            fourth_case_date = driver.find_element_by_xpath(fourth_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_offense_path))
            global fourth_case_offense
            fourth_case_offense = driver.find_element_by_xpath(fourth_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_court_path))
            global fourth_case_court
            fourth_case_court = driver.find_element_by_xpath(fourth_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_case_time_path))
            global fourth_case_time
            fourth_case_time = driver.find_element_by_xpath(fourth_case_time_path).text
            #### 5 OF 5
            wait.until(EC.presence_of_element_located(By.XPATH, fifth_case_number_path))
            global fifth_case_number
            fifth_case_number = driver.find_element_by_xpath(fifth_case_number_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fifth_case_date_path))
            global fifth_case_date
            fifth_case_date = driver.find_element_by_xpath(fifth_case_date_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fifth_case_offense_path))
            global fifth_case_offense
            fifth_case_offense = driver.find_element_by_xpath(fifth_case_offense_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fifth_case_court_path))
            global fifth_case_court
            fifth_case_court = driver.find_element_by_xpath(fifth_case_court_path).text
            wait.until(EC.presence_of_element_located(By.XPATH, fifth_case_time_path))
            fifth_case_time_box = driver.find_element_by_xpath(fifth_case_time_path)
            global fifth_case_time
            fifth_case_time = fifth_case_time_box.text

        def inner_case_details():
            if (global_one_exists == 1) and global_2_exists == 0:
                only_one_case_exists()
            elif (global_one_exists == 1) and global_2_exists == 2:
                only_two_cases_exist()
            elif (global_one_exists == 1) and global_3_exists == 3:
                only_three_cases_exist()
            elif (global_one_exists == 1) and global_4_exists == 4:
                four_cases_exist()
            elif (global_one_exists == 1) and global_5_exists == 5:
                five_cases_exist()

        inner_case_details()

    def find_defendent_info():
        lnf_name_global_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[5]/span[2]"
        if check_exists_by_xpath(first_appointment_xpath == True):
            wait.until(EC.presence_of_element_located(By.XPATH, first_appointment_xpath))
            appointment = driver.find_element_by_xpath(first_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            global booker
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            global booking_global1
            booking_global1 = booker
            global global_one_exists
            global_one_exists = 1
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
            global lnf_name_global1
            lnf_name_global1 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            global DOB_global1
            DOB_global1: object = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            global last_name_global1
            last_name_global1 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            global legalname_global1
            legalname_global1 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            global gender_global1, global_firstname1, globalzip_1, globalstate_1, globalcity_1, firstline_address1, d2, global_datenamez1, global_homephone_1
            global global_alternate_1, global_email1
            gender_global1 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname1 = str(last_name1.split(sep, 1)[1])
            ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global global_booking_address1
            global_booking_address1 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_1 = global_booking_address1.split(",")[3].strip()
            globalstate_1 = global_booking_address1.split(",")[2].strip()
            globalcity_1 = global_booking_address1.split(",")[1].strip()
            firstline_address1 = global_booking_address1.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            global no_hyphens_dob_global1
            no_hyphens_dob_global1 = re.sub('-', '', DOB_global1)
            d2 = "-"
            global_datenamez1 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global1 + pe
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_1 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_1 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email1 = driver.find_element_by_xpath(gmail_apt_email_path).text
            get_case_details()
        elif check_exists_by_xpath(second_appointment_xpath) == True:
            wait.until(EC.presence_of_element_located(By.XPATH, second_appointment_xpath))
            appointment = driver.find_element_by_xpath(second_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            global booker
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            global booking_global2, global_2_exists
            booking_global2 = booker
            global_2_exists = 2
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
            global lnf_name_global2, last_name_global2, legalname_global2, gender_global2, global_firstname2, globalzip_2, globalstate_2
            global  globalcity_2, firstline_address2, global_datenamez2, global_homephone_2, global_alternate_2, global_email2, DOB_global2
            lnf_name_global2 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            DOB_global2 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global2 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global2 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            gender_global2 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname2 = str(last_name1.split(sep, 1)[1])
            global global_booking_address2, no_hyphens_dob_global2
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address2 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_2 = global_booking_address2.split(",")[3].strip()
            globalstate_2 = global_booking_address2.split(",")[2].strip()
            globalcity_2 = global_booking_address2.split(",")[1].strip()
            firstline_address2 = global_booking_address2.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            no_hyphens_dob_global2 = re.sub('-', '', DOB_global2)
            d2 = "-"
            global_datenamez2 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global2 + pe
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_2 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_2 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email2 = driver.find_element_by_xpath(gmail_apt_email_path).text
            get_case_details()  ########################################################################
        elif check_exists_by_xpath(third_appointment_xpath) == True:
            wait.until(EC.presence_of_element_located(By.XPATH, third_appointment_xpath))
            appointment = driver.find_element_by_xpath(third_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            global booking_global3, global_3_exists, lnf_name_global3, globalcity_3, global_datenamez3
            global last_name_global3, gender_global3, global_firstname3, globalzip_3, globalstate_3,firstline_address3
            global booker
            booking_global3 = booker
            global_3_exists = 3
            open_gmail()

            def booker_tool():  # must follow open gmail function call
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchpath))
                gmailht_search = driver.find_element_by_xpath(gmailht_searchpath)
                gmailht_search.click().clear().send_keys(booker)
                wait.until(EC.presence_of_element_located(By.XPATH, gmailht_searchbtnpath))
                gmail_srch_button = driver.find_element_by_xpath(gmailht_searchbtnpath)
                gmail_srch_button.click()
            global DOB_global3, global_booking_address3, no_hyphens_dob_global3
            booker_tool()
            wait.until(EC.presence_of_element_located(By.XPATH, lnf_name_global_path))
            lnf_name_global3 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            DOB_global3 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global3 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            global legalname_global3
            legalname_global3 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            gender_global3 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname3 = str(last_name1.split(sep, 1)[1])
            ################################################
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address3 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_3 = global_booking_address3.split(",")[3].strip()
            globalstate_3 = global_booking_address3.split(",")[2].strip()
            globalcity_3 = global_booking_address3.split(",")[1].strip()
            firstline_address3 = global_booking_address3.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            no_hyphens_dob_global3 = re.sub('-', '', DOB_global3)
            d2 = "-"
            global_datenamez3 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global3 + pe
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global global_homephone_3, global_alternate_3, global_email3, global4, booker
            global_homephone_3 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_3 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email3 = driver.find_element_by_xpath(gmail_apt_email_path).text
            get_case_details()  ########################################################################
        elif check_exists_by_xpath(fourth_appointment_xpath) == True:
            wait.until(EC.presence_of_element_located(By.XPATH, fourth_appointment_xpath))
            appointment = driver.find_element_by_xpath(fourth_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            global booking_global4, global_4_exists, booker
            booking_global4 = booker
            global_4_exists = 4
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
            global lnf_name_global4
            lnf_name_global4 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            global globalcity_4, globalstate_4, globalzip_4, gender_global4, global_firstname4, legalname_global4
            global firstline_address4, global_datenamez4, global_homephone_4, global_email4, DOB_global4, last_name_global4
            global global_booking_address4, global_alternate_4
            DOB_global4 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global4 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global4 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            gender_global4 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname4 = str(last_name1.split(sep, 1)[1])
            ################################################
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address4 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_4 = global_booking_address4.split(",")[3].strip()
            globalstate_4 = global_booking_address4.split(",")[2].strip()
            globalcity_4 = global_booking_address4.split(",")[1].strip()
            firstline_address4 = global_booking_address4.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            d2 = "-"
            global_datenamez4 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global4 + pe
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_4 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_4 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email4 = driver.find_element_by_xpath(gmail_apt_email_path).text
            get_case_details()
        elif check_exists_by_xpath(fifth_appointment_xpath == True):
            wait.until(EC.presence_of_element_located(By.XPATH, fifth_appointment_xpath))
            appointment = driver.find_element_by_xpath(fifth_appointment_xpath)
            appointment.click()
            wait.until(EC.presence_of_element_located(By.XPATH, booking_global_xpath))
            booker = driver.find_element_by_xpath(booking_global_xpath).text
            global booking_global5, global_5_exists, booker
            booking_global5 = booker
            global_5_exists = 5
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
            global lnf_name_global5, globalcity_5, globalstate_5, globalzip_5, global_homephone_5, global_email5, last_name_global5, legalname_global5
            global gender_global5, global_firstname5, firstline_address5, global_datenamez5, global_alternate_5
            lnf_name_global5 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            global DOB_global5, no_hyphens_dob_global5, global_booking_address5
            DOB_global5 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global5 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global5 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            gender_global5 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname5 = str(last_name1.split(sep, 1)[1])
            ################################################
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address5 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_5 = global_booking_address5.split(",")[3].strip()
            globalstate_5 = global_booking_address5.split(",")[2].strip()
            globalcity_5 = global_booking_address5.split(",")[1].strip()
            firstline_address5 = global_booking_address5.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            no_hyphens_dob_global5 = re.sub('-', '', DOB_global5)
            d2 = "-"
            global_datenamez5 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global5 + pe
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_5 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_5 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email5 = driver.find_element_by_xpath(gmail_apt_email_path).text
            get_case_details()
        else:
            pass
    create_elaw_appointments()
    find_defendent_info()
    replace_doc_values_and_print()


# Open_amp -> appointment_iteration ->find defendent info -> open gmail -> booker -> open drive -> replace_dochub_values() -> print dochub letters()

def open_amp():
    driver: WebDriver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
    driver.get(
        "window.open('https://idc.traviscountytx.gov/nidp/idff/sso?id=35&sid=2&option=credential&sid=2&target=https%3A%2F%2Fcourts.traviscountytx.gov%2Famp%2F');")
    global user1_XPATH, pass1_XPATH, access_server_XPATH
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
    pass1.send_keys(pass00)
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


###create appointments - > create cases
global no_hyphens_dob_global3
no_hyphens_dob_global3 = re.sub('-', '', DOB_global3)

def create_elaw_appointments():
    # find the elements to click and interact with

    # ELAW XPATHS!!!!!
    elaw_city_path = "//*[@id=\"clientinformation\"]/fieldset/table[5]/tbody/tr[2]/td[1]/font/input"
    elaw_state_path = "//*[@id=\"clientinformation\"]/fieldset/table[5]/tbody/tr[2]/td[2]/font/input"
    elaw_zip_path = "//*[@id=\"clientinformation\"]/fieldset/table[5]/tbody/tr[2]/td[3]/font/input"
    elaw_home_phone_path = "//*[@id=\"clientinformation\"]/fieldset/table[6]/tbody/tr[5]/td[2]/font/input"
    elaw_alternate_phone_path: str = "//*[@id=\"clientinformation\"]/fieldset/table[6]/tbody/tr[9]/td[2]/font/input"
    elaw_email_path: str = "//*[@id=\"clientinformation\"]/fieldset/table[6]/tbody/tr[10]/td[2]/font/input"
    elaw_salutations_mr_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[5]/font/select/option[2]"
    elaw_salutations_ms_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[5]/font/select/option[3]"
    elaw_first_address_path = "//*[@id=\"clientinformation\"]/fieldset/table[4]/tbody/tr[2]/td[1]/font/input"
    global elaw_second_address_path
    elaw_second_address_path = "//*[@id=\"clientinformation\"]/fieldset/table[4]/tbody/tr[3]/td/font/input"
    elaw_court_no_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[1]/font[1]/select"
    elaw_court_appt_yes_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[1]/font[1]/select/option[2]"
    elaw_bookingno_path: str = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[1]/font[3]/input"
    elaw_inJail_no_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[2]/font[1]/select"
    elawe_inJail_yes_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[2]/font[1]/select/option[2]"
    elaw_dob_path = "//*[@id=\"clientinformation\"]/fieldset/table[6]/tbody/tr[13]/td[2]/font/input"
    elaw_saveclose_path = "/html/body/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/a[1]"
    elaw_sex_male_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[4]/font/select"
    elaw_sex_female_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[4]/font/select/option[2]"
    elaw_first_name_path = "//*[@id=\"clientinformation\"]/fieldset/table[3]/tbody/tr[2]/td[1]/font/input"
    elaw_last_name_path = "//*[@id=\"clientinformation\"]/fieldset/table[3]/tbody/tr[2]/td[3]/font/input"
    elaw_salutations_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[5]/font/select"

    def insert_jail_status():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_inJail_no_path))
        jail_no_elaw = driver.find_element_by_xpath(elaw_inJail_no_path)
        jail_no_elaw.click()
        wait.until(EC.presence_of_element_located(By.XPATH, elawe_inJail_yes_path))
        jail_yes_elaw = driver.find_element_by_xpath(elawe_inJail_yes_path)
        jail_yes_elaw.click()

    def insert_appt_status():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_court_no_path))
        court_no_elaw = driver.find_element_by_xpath(elaw_court_no_path)
        court_no_elaw.click()
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_court_appt_yes_path))
        elaw_appt_yes = driver.find_element_by_xpath(elaw_court_appt_yes_path)
        elaw_appt_yes.click()  # one of 12 sub functions

    def insert_booking_number1():  # one of five
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_bookingno_path))
        elaw_bookingno = driver.find_element_by_xpath(elaw_bookingno_path)
        elaw_bookingno.send_keys(booking_global1)

    def insert_booking_number2():  # one of five
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_bookingno_path))
        elaw_bookingno = driver.find_element_by_xpath(elaw_bookingno_path)
        elaw_bookingno.send_keys(booking_global2)

    def insert_booking_number3():  # one of five
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_bookingno_path))
        elaw_bookingno = driver.find_element_by_xpath(elaw_bookingno_path)
        elaw_bookingno.send_keys(booking_global3)

    def insert_booking_number4():  # one of five
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_bookingno_path))
        elaw_bookingno = driver.find_element_by_xpath(elaw_bookingno_path)
        elaw_bookingno.send_keys(booking_global4)

    def insert_booking_number5():  # one of five
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_bookingno_path))
        elaw_bookingno = driver.find_element_by_xpath(elaw_bookingno_path)
        elaw_bookingno.send_keys(booking_global5)

    ########## two out of twelve
    def insert_dob1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_dob_path))
        elaw_dob = driver.find_element_by_xpath(elaw_dob_path)
        elaw_dob.send_keys(DOB_global1)

    def insert_dob2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_dob_path))
        elaw_dob = driver.find_element_by_xpath(elaw_dob_path)
        elaw_dob.send_keys(DOB_global2)

    def insert_dob3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_dob_path))
        elaw_dob = driver.find_element_by_xpath(elaw_dob_path)
        elaw_dob.send_keys(DOB_global3)

    def insert_dob4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_dob_path))
        elaw_dob = driver.find_element_by_xpath(elaw_dob_path)
        elaw_dob.send_keys(DOB_global4)

    def insert_dob5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_dob_path))
        elaw_dob = driver.find_element_by_xpath(elaw_dob_path)
        elaw_dob.send_keys(DOB_global5)

    ######### THREE OF TWELVE
    def insert_email1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_email_path))
        elaw_email = driver.find_element_by_xpath(elaw_email_path)
        elaw_email.send_keys(global_email1)

    def insert_email2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_email_path))
        elaw_email = driver.find_element_by_xpath(elaw_email_path)
        elaw_email.send_keys(global_email2)

    def insert_email3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_email_path))
        elaw_email = driver.find_element_by_xpath(elaw_email_path)
        elaw_email.send_keys(global_email3)

    def insert_email4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_email_path))
        elaw_email = driver.find_element_by_xpath(elaw_email_path)
        elaw_email.send_keys(global_email4)

    def insert_email5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_email_path))
        elaw_email = driver.find_element_by_xpath(elaw_email_path)
        elaw_email.send_keys(global_email5)

    ####FOUR OF TWELVE
    def insert_alternate_phone1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_alternate_phone_path))
        elaw_alternate_phone = driver.find_element_by_xpath(elaw_alternate_phone_path)
        elaw_alternate_phone.send_keys(global_alternate_1)

    def insert_alternate_phone2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_alternate_phone_path))
        elaw_alternate_phone = driver.find_element_by_xpath(elaw_alternate_phone_path)
        elaw_alternate_phone.send_keys(global_alternate_2)

    def insert_alternate_phone3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_alternate_phone_path))
        elaw_alternate_phone = driver.find_element_by_xpath(elaw_alternate_phone_path)
        elaw_alternate_phone.send_keys(global_alternate_3)

    def insert_alternate_phone4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_alternate_phone_path))
        elaw_alternate_phone = driver.find_element_by_xpath(elaw_alternate_phone_path)
        elaw_alternate_phone.send_keys(global_alternate_4)

    def insert_alternate_phone5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_alternate_phone_path))
        elaw_alternate_phone = driver.find_element_by_xpath(elaw_alternate_phone_path)
        elaw_alternate_phone.send_keys(global_alternate_5)  ########### FIVE OF TWELVE

    def insert_home_phone1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_home_phone_path))
        elaw_home_phone = driver.find_element_by_xpath(elaw_home_phone_path)
        elaw_home_phone.send_keys(global_homephone_1)

    def insert_home_phone2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_home_phone_path))
        elaw_home_phone = driver.find_element_by_xpath(elaw_home_phone_path)
        elaw_home_phone.send_keys(global_homephone_2)

    def insert_home_phone3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_home_phone_path))
        elaw_home_phone = driver.find_element_by_xpath(elaw_home_phone_path)
        elaw_home_phone.send_keys(global_homephone_3)

    def insert_home_phone4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_home_phone_path))
        elaw_home_phone = driver.find_element_by_xpath(elaw_home_phone_path)
        elaw_home_phone.send_keys(global_homephone_4)

    def insert_home_phone5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_home_phone_path))
        elaw_home_phone = driver.find_element_by_xpath(elaw_home_phone_path)
        elaw_home_phone.send_keys(global_homephone_5)

    ########## SIX OF TWELVE
    def insert_datenamez1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_name_path))
        elaw_first_name_box = driver.find_element_by_xpath(elaw_first_name_path)
        elaw_first_name_box.send_keys(global_datenamez1)
    def insert_datenamez2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_name_path))
        elaw_first_name_box = driver.find_element_by_xpath(elaw_first_name_path)
        elaw_first_name_box.send_keys(global_datenamez2)
    def insert_datenamez3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_name_path))
        elaw_first_name_box = driver.find_element_by_xpath(elaw_first_name_path)
        elaw_first_name_box.send_keys(global_datenamez3)
    def insert_datenamez4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_name_path))
        elaw_first_name_box = driver.find_element_by_xpath(elaw_first_name_path)
        elaw_first_name_box.send_keys(global_datenamez4)
    def insert_datenamez5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_name_path))
        elaw_first_name_box = driver.find_element_by_xpath(elaw_first_name_path)
        elaw_first_name_box.send_keys(global_datenamez5)
        ############### SEVEN OF TWELVE

    def insert_salutationssex():
        if global_pronoun == pn2:
            wait.until(EC.presence_of_element_located(By.XPATH, elaw_sex_male_path))
            sex_male = driver.find_element_by_xpath(elaw_sex_male_path)
            sex_male.click()
            wait.until(EC.presence_of_element_located(By.XPATH, elaw_sex_female_path))
            sex_female = driver.find_element_by_xpath(elaw_sex_female_path)
            sex_female.click()
            wait.until(EC.presence_of_element_located(By.XPATH, elaw_salutations_path))
            salutations_law = driver.find_element_by_xpath(elaw_salutations_path)
            salutations_law.click()
            wait.until(EC.presence_of_element_located(By.XPATH, elaw_salutations_ms_path))
            salutations_ms = driver.find_element_by_xpath(elaw_salutations_ms_path)
            salutations_ms.click()
        else:
            wait.until(EC.presence_of_element_located(By.XPATH, elaw_salutations_path))
            salutations_law = driver.find_element_by_xpath(elaw_salutations_path)
            salutations_law.click()
            wait.until(EC.presence_of_element_located(By.XPATH, elaw_salutations_mr_path))
            salutations_mr = driver.find_element_by_xpath(elaw_salutations_mr_path)
            salutations_mr.click()

    ############ EIGHT OF TWELVE
    def insert_zip1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_zip_path))
        elaw_zip = driver.find_element_by_xpath(elaw_zip_path)
        elaw_zip.send_keys(globalzip_1)

    def insert_zip2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_zip_path))
        elaw_zip = driver.find_element_by_xpath(elaw_zip_path)
        elaw_zip.send_keys(globalzip_2)

    def insert_zip3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_zip_path))
        elaw_zip = driver.find_element_by_xpath(elaw_zip_path)
        elaw_zip.send_keys(globalzip_3)

    def insert_zip4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_zip_path))
        elaw_zip = driver.find_element_by_xpath(elaw_zip_path)
        elaw_zip.send_keys(globalzip_4)

    def insert_zip5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_zip_path))
        elaw_zip = driver.find_element_by_xpath(elaw_zip_path)
        elaw_zip.send_keys(globalzip_5)  ############# NINE OF TWELVE

    def insert_state1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_state_path))
        elaw_state1 = driver.find_element_by_xpath(elaw_state_path)
        elaw_state1.send_keys(globalstate_1)

    def insert_state2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_state_path))
        elaw_state1 = driver.find_element_by_xpath(elaw_state_path)
        elaw_state1.send_keys(globalstate_2)

    def insert_state3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_state_path))
        elaw_state1 = driver.find_element_by_xpath(elaw_state_path)
        elaw_state1.send_keys(globalstate_3)

    def insert_state4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_state_path))
        elaw_state1 = driver.find_element_by_xpath(elaw_state_path)
        elaw_state1.send_keys(globalstate_4)

    def insert_state5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_state_path))
        elaw_state1 = driver.find_element_by_xpath(elaw_state_path)
        elaw_state1.send_keys(globalstate_5)  ############# TEN OF TWELVE

    def insert_city1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_city_path))
        city1 = driver.find_element_by_xpath(elaw_city_path)
        city1.send_keys(globalcity_1)

    def insert_city2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_city_path))
        city1 = driver.find_element_by_xpath(elaw_city_path)
        city1.send_keys(globalcity_2)

    def insert_city3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_city_path))
        city1 = driver.find_element_by_xpath(elaw_city_path)
        city1.send_keys(globalcity_3)

    def insert_city4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_city_path))
        city1 = driver.find_element_by_xpath(elaw_city_path)
        city1.send_keys(globalcity_4)

    def insert_city5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_city_path))
        city1 = driver.find_element_by_xpath(elaw_city_path)
        city1.send_keys(globalcity_5)  ############# ELEVEN OF TWELVE

    def insert_first_address1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_address_path))
        elaw_first_address = driver.find_element_by_xpath(elaw_first_address_path)
        elaw_first_address.send_keys(firstline_address1)

    def insert_first_address2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_address_path))
        elaw_first_address = driver.find_element_by_xpath(elaw_first_address_path)
        elaw_first_address.send_keys(firstline_address2)

    def insert_first_address3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_address_path))
        elaw_first_address = driver.find_element_by_xpath(elaw_first_address_path)
        elaw_first_address.send_keys(firstline_address3)

    def insert_first_address4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_address_path))
        elaw_first_address = driver.find_element_by_xpath(elaw_first_address_path)
        elaw_first_address.send_keys(firstline_address4)

    def insert_first_address5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_first_address_path))
        elaw_first_address = driver.find_element_by_xpath(elaw_first_address_path)
        elaw_first_address.send_keys(firstline_address5)  ############### TWELVE OF TWELVE

    def insert_last_name1():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_last_name_path))
        elaw_last_name = driver.find_element_by_xpath(elaw_last_name_path)
        elaw_last_name.send_keys(last_name_global1)

    def insert_last_name2():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_last_name_path))
        elaw_last_name = driver.find_element_by_xpath(elaw_last_name_path)
        elaw_last_name.send_keys(last_name_global2)

    def insert_last_name3():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_last_name_path))
        elaw_last_name = driver.find_element_by_xpath(elaw_last_name_path)
        elaw_last_name.send_keys(last_name_global3)

    def insert_last_name4():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_last_name_path))
        elaw_last_name = driver.find_element_by_xpath(elaw_last_name_path)
        elaw_last_name.send_keys(last_name_global4)

    def insert_last_name5():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_last_name_path))
        elaw_last_name = driver.find_element_by_xpath(elaw_last_name_path)
        elaw_last_name.send_keys(last_name_global5)

    def save_elaw():
        wait.until(EC.presence_of_element_located(By.XPATH, elaw_saveclose_path))
        elaw_saveclose = driver.find_element_by_xpath(elaw_saveclose_path)
        elaw_saveclose.click()
        time.sleep(6)
        driver.close()  #########3FIVE CASES FOR ONE DEFENDENET CASE

    def create_elaw_case_by_case1():
        time.sleep(5)
        replacement_casenumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_courtnumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_date_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[9]/td[3]/b/font/input"
        replacement_offense_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[13]/td[3]/b[2]/font/input"
        sign_elaw_open_old_client()
        replacement_time_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[10]/td[3]/b[2]/font/input"
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_courtnumber_path))
        replacement_courtnumber = driver.find_element_by_xpath(replacement_courtnumber_path)
        replacement_courtnumber.clear()
        replacement_courtnumber.send_keys(first_case_court)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_date_path))
        replacement_date = driver.find_element_by_xpath(replacement_date_path)
        replacement_date.clear()
        replacement_date.send_keys(first_case_date)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_offense_path))
        replacement_offense = driver.find_element_by_xpath(replacement_offense_path)
        replacement_offense.clear()
        replacement_offense.send_keys(first_case_offense)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_casenumber_path))
        replacement_casenumber = driver.find_element_by_xpath(replacement_casenumber_path)
        replacement_casenumber.clear()
        replacement_casenumber.send_keys(first_case_number)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_time_path))
        replacement_time = driver.find_element_by_xpath(replacement_time_path)
        replacement_time.send_keys(first_case_time)
        wait.until(EC.presence_of_element_located(By.XPATH, case_elaw_save_close_path))
        case_elaw_save_close = driver.find_element_by_xpath(case_elaw_save_close_path)
        case_elaw_save_close.click()
        time.sleep(5)

    def create_elaw_case_by_case2():
        time.sleep(5)
        replacement_casenumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_courtnumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_date_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[9]/td[3]/b/font/input"
        replacement_offense_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[13]/td[3]/b[2]/font/input"
        sign_elaw_open_old_client()
        replacement_time_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[10]/td[3]/b[2]/font/input"
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_courtnumber_path))
        replacement_courtnumber = driver.find_element_by_xpath(replacement_courtnumber_path)
        replacement_courtnumber.clear()
        replacement_courtnumber.send_keys(second_case_court)
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_date_path))
        replacement_date = driver.find_element_by_xpath(replacement_date_path)
        replacement_date.clear()
        replacement_date.send_keys(second_case_date)
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_offense_path))
        replacement_offense = driver.find_element_by_xpath(replacement_offense_path)
        replacement_offense.clear()
        replacement_offense.send_keys(second_case_offense)
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_casenumber_path))
        replacement_casenumber = driver.find_element_by_xpath(replacement_casenumber_path)
        replacement_casenumber.clear()
        replacement_casenumber.send_keys(second_case_number)
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_time_path))
        replacement_time = driver.find_element_by_xpath(replacement_time_path)
        replacement_time.send_keys(second_case_time)
        wait.until(ec.presence_of_element_located(By.XPATH, case_elaw_save_close_path))
        case_elaw_save_close = driver.find_element_by_xpath(case_elaw_save_close_path)
        case_elaw_save_close.click()
        time.sleep(5)

    def create_elaw_case_by_case3():
        time.sleep(5)
        replacement_casenumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_courtnumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_date_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[9]/td[3]/b/font/input"
        replacement_offense_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[13]/td[3]/b[2]/font/input"
        sign_elaw_open_old_client()
        replacement_time_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[10]/td[3]/b[2]/font/input"
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_courtnumber_path))
        replacement_courtnumber = driver.find_element_by_xpath(replacement_courtnumber_path)
        replacement_courtnumber.clear()
        replacement_courtnumber.send_keys(third_case_court)
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_date_path))
        replacement_date = driver.find_element_by_xpath(replacement_date_path)
        replacement_date.clear()
        replacement_date.send_keys(third_case_date)
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_offense_path))
        replacement_offense = driver.find_element_by_xpath(replacement_offense_path)
        replacement_offense.clear()
        replacement_offense.send_keys(third_case_offense)
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_casenumber_path))
        replacement_casenumber = driver.find_element_by_xpath(replacement_casenumber_path)
        replacement_casenumber.clear()
        replacement_casenumber.send_keys(third_case_number)
        wait.until(ec.presence_of_element_located(By.XPATH, replacement_time_path))
        replacement_time = driver.find_element_by_xpath(replacement_time_path)
        replacement_time.send_keys(third_case_time)
        wait.until(ec.presence_of_element_located(By.XPATH, case_elaw_save_close_path))
        case_elaw_save_close = driver.find_element_by_xpath(case_elaw_save_close_path)
        case_elaw_save_close.click()
        time.sleep(5)

    def create_elaw_case_by_case4():
        time.sleep(5)
        replacement_casenumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_courtnumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_date_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[9]/td[3]/b/font/input"
        replacement_offense_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[13]/td[3]/b[2]/font/input"
        sign_elaw_open_old_client()
        replacement_time_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[10]/td[3]/b[2]/font/input"
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_courtnumber_path))
        replacement_courtnumber = driver.find_element_by_xpath(replacement_courtnumber_path)
        replacement_courtnumber.clear()
        replacement_courtnumber.send_keys(fourth_case_court)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_date_path))
        replacement_date = driver.find_element_by_xpath(replacement_date_path)
        replacement_date.clear()
        replacement_date.send_keys(fourth_case_date)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_offense_path))
        replacement_offense = driver.find_element_by_xpath(replacement_offense_path)
        replacement_offense.clear()
        replacement_offense.send_keys(fourth_case_offense)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_casenumber_path))
        replacement_casenumber = driver.find_element_by_xpath(replacement_casenumber_path)
        replacement_casenumber.clear()
        replacement_casenumber.send_keys(fourth_case_number)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_time_path))
        replacement_time = driver.find_element_by_xpath(replacement_time_path)
        replacement_time.send_keys(fourth_case_time)
        wait.until(EC.presence_of_element_located(By.XPATH, case_elaw_save_close_path))
        case_elaw_save_close = driver.find_element_by_xpath(case_elaw_save_close_path)
        case_elaw_save_close.click()
        time.sleep(5)

    def create_elaw_case_by_case5():
        time.sleep(5)
        replacement_casenumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_courtnumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_date_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[9]/td[3]/b/font/input"
        replacement_offense_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[13]/td[3]/b[2]/font/input"
        sign_elaw_open_old_client()
        replacement_time_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[10]/td[3]/b[2]/font/input"
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_courtnumber_path))
        replacement_courtnumber = driver.find_element_by_xpath(replacement_courtnumber_path)
        replacement_courtnumber.clear()
        replacement_courtnumber.send_keys(fifth_case_court)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_date_path))
        replacement_date = driver.find_element_by_xpath(replacement_date_path)
        replacement_date.clear()
        replacement_date.send_keys(fifth_case_date)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_offense_path))
        replacement_offense = driver.find_element_by_xpath(replacement_offense_path)
        replacement_offense.clear()
        replacement_offense.send_keys(fifth_case_offense)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_casenumber_path))
        replacement_casenumber = driver.find_element_by_xpath(replacement_casenumber_path)
        replacement_casenumber.clear()
        replacement_casenumber.send_keys(fifth_case_number)
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_time_path))
        replacement_time = driver.find_element_by_xpath(replacement_time_path)
        replacement_time.send_keys(fifth_case_time)
        wait.until(EC.presence_of_element_located(By.XPATH, case_elaw_save_close_path))
        case_elaw_save_close = driver.find_element_by_xpath(case_elaw_save_close_path)
        case_elaw_save_close.click()
        time.sleep(5)

        # for the first defendent in list of up to 5

    def wait_and_replace_elements1():
        insert_jail_status()
        insert_appt_status()
        insert_salutationssex()
        # about 15 individual boxes (instance objects)
        insert_booking_number1()
        insert_datenamez1()
        insert_dob1()  ##//
        insert_email1()  ##//
        insert_alternate_phone1()  ##//
        insert_home_phone1()  ##//
        insert_last_name1()  ##//
        insert_zip1()
        insert_state1()
        insert_city1()
        insert_first_address1()
        save_elaw()
        create_elaw_case_by_case1()

    # for the second in list of up to 5
    def wait_and_replace_elements2():  # function for second defendant only
        insert_jail_status()  # //
        insert_appt_status()  # //
        insert_salutationssex()
        # about 15 individual boxes (instance objects)
        insert_booking_number2()  ##//
        insert_datenamez2()  ##//
        insert_dob2()  ##//
        insert_email2()  ##//
        insert_alternate_phone2()  ##//
        insert_home_phone2()  ##//
        insert_last_name2()  ##//
        insert_zip2()  ##//
        insert_state2()  ##//
        insert_city2()  ##//
        insert_first_address2()  # //
        save_elaw()
        create_elaw_case_by_case2()
        
    def wait_and_replace_elements3():  # function for second defendant only
        insert_jail_status()  # //
        insert_appt_status()  # //
        insert_salutationssex()
        # about 15 individual boxes (instance objects)
        insert_booking_number3()  ##//
        insert_datenamez3()  ##//
        insert_dob3()  ##//
        insert_email3()  ##//
        insert_alternate_phone3()  ##//
        insert_home_phone3()  ##//
        insert_last_name3()  ##//
        insert_zip3()  ##//
        insert_state3()  ##//
        insert_city3()  ##//
        insert_first_address3()  # //
        save_elaw()
        create_elaw_case_by_case3()
        
    def wait_and_replace_elements4():  # function for second defendent only
        insert_jail_status()  # //
        insert_appt_status()  # //
        insert_salutationssex()
        # about 15 individual boxes (instance objects)
        insert_booking_number4()  ##//
        insert_datenamez4()  ##//
        insert_dob4()  ##//
        insert_email4()  ##//
        insert_alternate_phone4()  ##//
        insert_home_phone4()  ##//
        insert_last_name4()  ##//
        insert_zip4()  ##//
        insert_state4()  ##//
        insert_city4()  ##//
        insert_first_address4()  # //
        save_elaw()
        create_elaw_case_by_case4()
    def wait_and_replace_elements5():
        insert_jail_status()  # //
        insert_appt_status()  # //
        insert_salutationssex()
        # about 15 individual boxes (instance objects)
        insert_booking_number5()  ##//
        insert_datenamez5()  ##//
        insert_dob5()  ##//
        insert_email5()  ##//
        insert_alternate_phone5()  ##//
        insert_home_phone5()  ##//
        insert_last_name5()  ##//
        insert_zip5()  ##//
        insert_state5()  ##//
        insert_city5()  ##//
        insert_first_address5()  # //
        save_elaw()
        create_elaw_case_by_case5()
        
    def only_one_defendent_exists():
        sign_elaw_open_new_client()
        wait_and_replace_elements1()

    def only_two_defendents_exist():
        sign_elaw_open_new_client()
        wait_and_replace_elements1()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements2()

    def only_three_defendents_exist():
        sign_elaw_open_new_client()
        wait_and_replace_elements1()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements2()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements3()

    def four_defendents_exist():
        sign_elaw_open_new_client()
        wait_and_replace_elements1()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements2()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements3()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements4()

    def five_defendents_exist():
        sign_elaw_open_new_client()
        wait_and_replace_elements1()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements2()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements3()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements4()
        time.sleep(5)
        sign_elaw_open_new_client()
        wait_and_replace_elements5()

    # TODO: REPLACE ALL VALUES WITH GLOBAL VARIABLES FROM PREVIOUS GETTER FUNCTIONS
    def inner_doc_replacements():
        if (global_one_exists == 1) and global_2_exists == 0:
            only_one_defendent_exists()
        elif (global_one_exists == 1) and global_2_exists == 2:
            only_two_defendents_exist()
        elif (global_one_exists == 1) and global_3_exists == 3:
            only_three_defendents_exist()
        elif (global_one_exists == 1) and global_4_exists == 4:
            four_defendents_exist()
        elif (global_one_exists == 1) and global_5_exists == 5:
            five_defendents_exist()

    inner_doc_replacements()


open_amp()  # this is the fuse, will automatically start appointment iteration
# which will also start find_appointment_info and replacedocvalues/print
time.sleep(15 * 60)
driver.close()
