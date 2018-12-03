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
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
from _datetime import datetime
import datetime
import holidays
import re
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


booking_global = ""




def open_gmail():

    driver.get(html_1url)
    signin_gmail = driver.find_element_by_xpath(signin_gmail_path)
    wait.until(EC.presence_of_element_located(By.XPATH, signin_gmail_path))
    signin_gmail.click()  
    wait.until(EC.presence_of_element_located(By.XPATH, login5path))
    login5 = driver.find_element_by_xpath(login5path)
    login5.send_keys(user00)
    wait.until(EC.presence_of_element_located(By.XPATH, pass5path))
    pass5 = driver.find_element_by_xpath(pass5path)
    pass5.send_keys(pass00)
    wait.until(EC.presence_of_element_located(By.XPATH, gmail_next_path))
    driver.find_element_by_xpath(gmail_next_path).click()
    driver.get(html_1url)
    
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
no_hyphens_dob_global1 = ""
no_hyphens_dob_global2 = ""
no_hyphens_dob_global3 = ""
no_hyphens_dob_global4 = ""
no_hyphens_dob_global5 = ""
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
booking_global_xpath = "//*[@id=\"appt-detail\"]/div[2]/div[1]/p[3]/span"
gender_global_path = "//*[@id=\":eq\"]/div[1]/div[2]/div[2]/div/div[2]/div/p[24]/span[2]"

sheriff_booking_path = "//*[@id=\"InmateCharges\"]/text()[1]"



entered_date = business_day()



documents_xpath = "//*[@id=\"appt_actions\"]/ul/li[1]/a"

open_docs_url = "https://docs.google.com/document/d/15Qk0UM2f9G7glB0BOL-hPeN86o_YN9YjfRvj53riBMQ/edit?usp=sharing"
sign_in_docs_path = "//*[@id=\"gb\"]/div/div/a"
docs_email_path = "//*[@id=\"identifierId\"]"
docs_pass_path = "//*[@id=\"password\"]/div[1]/div/div[1]/input"
docs_next_path = "//*[@id=\"passwordNext\"]"
more_options_path = "//*[@id=\"docs-findbar-button-more-options\"]"
firstname = ""
def open_docs():
    driver.get(open_docs_url)
    wait.until(EC.presence_of_element_located(By.XPATH, sign_in_docs_path))
    sign_in_docs = driver.find_element_by_xpath(sign_in_docs_path)
    sign_in_docs.click()
    wait.until(EC.presence_of_element_located(By.XPATH, docs_email_path))
    docs_email1 = driver.find_element_by_xpath(docs_email_path)
    docs_email1.send_keys(user00)
    wait.until(EC.presence_of_element_located(By.XPATH, docs_pass_path))
    docs_pass = driver.find_element_by_xpath(docs_pass_path)
    docs_pass.send_keys(pass00)
    wait.until(EC.presence_of_element_located(By.XPATH, docs_next_path))
    driver.find_element_by_xpath(docs_next_path).click()
pn1 = "Mr. "
jail_status = ""
global_pronoun = pn1
pn2 = "Ms. "

global_pronoun_1 = ""
global_pronoun_2 = ""
path_print_def = "//*[@id=\"print-header\"]/div/button[2]"
global_pronoun_3 = ""
global_pronoun_4 = ""
normal_pages_path = "//*[@id=\"page-settings\"]/div[2]/div/div[1]/label/input"
global_pronoun_5 = ""
orig_date = "Date:"
orig_legalname = "v."
global_lastName = ""
orig_lnf = "Defendant:"
custom_pages_path = "//*[@id=\"page-settings-custom-input\"]"
orig_dob = "DOB:"
orig_booking = "Booking No."
orig_salutations = "Dear"
def getpronoun():
    if gender_global1 = "Female":
        global_pronoun = pn2
    elif gender_global2 = "Female":
        global_pronoun = pn2        
    elif gender_global3 = "Female":
        global_pronoun = pn2        
    elif gender_global4 = "Female":
        global_pronoun = pn2        
    elif gender_global5 = "Female":
        global_pronoun = pn2        
    else:
        global_pronoun = pn1        

  

def replace_doc_values_and_print():
    getpronoun()

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
    get_legal()
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
    get_birthday()
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
    get_lnf()
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
    getlasto()
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
    get_firstname()
    def getJailStatus():
        sheriff_url = "https://public.co.travis.tx.us/sips/default.aspx"
        sheriff_lastname_path = "//*[@id=\"LastName\"]"
        sheriff_firstname_path = "//*[@id=\"FirstInitial\"]"
        sheriff_search_path = "//*[@id=\"SubmitNameSearch\"]"
        wait.until(EC.presence_of_element_located(By.XPATH, sheriff_lastname_path))
        sheriff_lastname = driver.find_element_by_xpath(sheriff_lastname_path)
        sheriff_lastname.send_keys(lasto)
        sheriff_firstname.send_keys(firstname)
        wait.until(EC.presence_of_element_located(By.XPATH, sheriff_search_path))
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
                if sheriff_booking == booker
                    keyboard.press_and_release("ctrl+p")
                    keyboard.press_and_release("enter")
                    jail_status = "Yes"
                    time.sleep(5)
            else:
                jail_status = "No"
                pass
        level2()      
    getJailStatus()


    #44 suffix means final replacement values per defendant
    date44 = orig_date + " " + entered_date
    legalname44 = orig_legalname + " " + legal
    birthday44 = orig_dob + " " + birthday
    lnf44 =  orig_lnf + " " + lnf
    salutations44 = orig_salutations + " " + global_pronoun + lasto + ","
    booking44 = orig_booking + " " + booker  
    open_docs()
    keyboard.press_and_release('ctrl+f')
    path_closer1 = "/html/body/div[61]/div[1]/span[2]"
    path_replace_what = "//*[@id=\"docs-findandreplacedialog-input\"]"
    path_replace_with = "//*[@id=\"docs-findandreplacedialog-replace-input\"]"
    path_replace_all = "//*[@id=\"docs-findandreplacedialog-button-replace-all\"]"
    #date44
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
    #legalname44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_legalname)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(legalname44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()    
    #birthday44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_dob)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(birthday44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()    
    #lnf44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_lnf)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(lnf44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()    
    #salutations44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_salutations)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(salutations44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    #booking44
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(orig_booking)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(booking44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    driver.find_element_by_xpath(path_closer1).click()
    
    #start printing
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
    #RESET VALUES TO DEFAULT
        #date44 REPLACE REPLACE REPLACE
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
    #legalname44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(legalname44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_legalname)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()    
    #birthday44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(birthday44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_dob)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()    
    #lnf44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(lnf44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_lnf)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()    
    #salutations44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(salutations44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_salutations)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    #booking44 REPLACE REPLACE REPLACE
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
    replace_what.clear()
    replace_what.send_keys(booking44)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
    replace_with.clear()
    replace_with.send_keys(orig_booking)
    wait.until(EC.presence_of_element_located(By.XPATH, path_replace_all))
    replace_all.click()
    driver.find_element_by_xpath(path_closer1).click()
global_firstname1 = ""
global_firstname2 = ""
global_firstname3 = ""
global_firstname4 = ""
global_firstname5 = ""

elaw_1_url = "https://www5.elawsoftware.com/"
def create_elaw_appointments():
    driver.get(elaw_1_url)
    user1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[3]/input"
    pass1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[2]/td[3]/input"
    access_server_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[3]/td[1]/div/input"
    #ELAW XPATHS!!!!!
    elaw_court_no_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[1]/font[1]/select"
    elaw_court_appt_yes_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[1]/font[1]/select/option[2]"
    elaw_bookingno_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[1]/font[3]/input"
    elaw_inJail_no_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[2]/font[1]/select"     
    elawe_inJail_yes_path = "//*[@id=\"clientinformation\"]/fieldset/table[1]/tbody/tr[2]/td[2]/font[1]/select/option[2]"
    elaw_sex_male_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[4]/font/select"
    elaw_sex_female_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[4]/font/select/option[2]"
    elaw_first_name_path = "//*[@id=\"clientinformation\"]/fieldset/table[3]/tbody/tr[2]/td[1]/font/input"
    elaw_last_name_path = "//*[@id=\"clientinformation\"]/fieldset/table[3]/tbody/tr[2]/td[3]/font/input"
    elaw_salutations_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[5]/font/select"
    elaw_salutations_mr_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[5]/font/select/option[2]"
    elaw_salutations_ms_path = "//*[@id=\"clientinformation\"]/fieldset/table[2]/tbody/tr[2]/td[5]/font/select/option[3]"
    elaw_first_address_path = "//*[@id=\"clientinformation\"]/fieldset/table[4]/tbody/tr[2]/td[1]/font/input"
    elaw_second_address_path = "//*[@id=\"clientinformation\"]/fieldset/table[4]/tbody/tr[3]/td/font/input"
    elaw_city_path = "//*[@id=\"clientinformation\"]/fieldset/table[5]/tbody/tr[2]/td[1]/font/input"
    elaw_state_path = "//*[@id=\"clientinformation\"]/fieldset/table[5]/tbody/tr[2]/td[2]/font/input"
    elaw_zip_path = "//*[@id=\"clientinformation\"]/fieldset/table[5]/tbody/tr[2]/td[3]/font/input"
    elaw_home_phone_path = "//*[@id=\"clientinformation\"]/fieldset/table[6]/tbody/tr[5]/td[2]/font/input"
    elaw_alternate_phone_path = "//*[@id=\"clientinformation\"]/fieldset/table[6]/tbody/tr[9]/td[2]/font/input"
    elaw_email_path = "//*[@id=\"clientinformation\"]/fieldset/table[6]/tbody/tr[10]/td[2]/font/input"
    elaw_dob_path = "//*[@id=\"clientinformation\"]/fieldset/table[6]/tbody/tr[13]/td[2]/font/input"
    elaw_saveclose_path = "/html/body/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/a[1]"
    #find the elements to click and interact with
    user1 = driver.find_element_by_xpath(user1_XPATH)
    pass1 = driver.find_element_by_xpath(pass1_XPATH)
    access1 = driver.find_element_by_xpath(access_server_XPATH)
    user1.send_keys(user01)
    pass1.send_keys(pass01)
    access1.click()    
    create_hover_path = "//*[@id=\"qmim2\"]"
    hover = ActionChains(driver).move_to_element(create_hover_path)
    hover.perform()
    new_apt_path = "//*[@id=\"qmitemhl2_0\"]"
    wait.until(EC.presence_of_element_located(By.XPATH, new_apt_path))
    new_apt = driver.find_element_by_xpath(new_apt_path)
    new_apt.click()
    #TODO: REPLACE ALL VALUES WITH GLOBAL VARIABLES FROM PREVIOUS GETTER FUNCTIONS
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
                email = driver.find_element_by_xpath(emailpath)
                email.click()
            booker_tool()
            wait.until(EC.presence_of_element_located(By.XPATH, lnf_name_global_path))
            lnf_name_global1 = driver.find_element_by_xpath(lnf_name_global_path).text  # final lnf name for defendent 1
            last_name1 = driver.find_element_by_xpath(lnf_name_global_path).text
            DOB_global1 = driver.find_element_by_xpath(def_DOB).text  # final dob for defendent 1
            last_name_global1 = last_name1.split(sep, 1)[0]  # USE FOR FINAL LAST NAME VALUE
            legalname_global1 = str(last_name1.split(sep, 1)[1]) + str(last_name1.split(sep, 1)[0])  # FINAL LEGAL NAME
            gender_global1 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname1 = str(last_name1.split(sep, 1)[1])
            ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!
                        ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!
            ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!
                        ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!                        
            ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!
            ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!
            ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!
            ##ADD THESE GLOBAL VARIABLES AND INSTANCE VARIABLES TO REST OF THE ITERATION!!!!
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address1 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_1 = global_booking_address1.split(",")[3].strip()
            globalstate_1 = global_booking_address1.split(",")[2].strip()
            globalcity_1 = global_booking_address1.split(",")[1].strip()
            firstline_address1 = global_booking_address1.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            no_hyphens_dob_global1 = re.sub('-','',DOB_global1)
            d2 = "-"
            global_datenamez1 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global1
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_1 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_1 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email1 = driver.find_element_by_xpath(gmail_apt_email_path).text

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
            gender_global2 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname2 = str(last_name1.split(sep, 1)[1])
##########################################################################
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address2 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_2 = global_booking_address1.split(",")[3].strip()
            globalstate_2 = global_booking_address1.split(",")[2].strip()
            globalcity_2 = global_booking_address1.split(",")[1].strip()
            firstline_address2 = global_booking_address1.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            no_hyphens_dob_global2 = re.sub('-','',DOB_global2)
            d2 = "-"
            global_datenamez2 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global2
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_2 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_2 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email2 = driver.find_element_by_xpath(gmail_apt_email_path).text
            ########################################################################            
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
            gender_global3 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname3 = str(last_name1.split(sep, 1)[1])
################################################
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address3 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_3 = global_booking_address1.split(",")[3].strip()
            globalstate_3 = global_booking_address1.split(",")[2].strip()
            globalcity_3 = global_booking_address1.split(",")[1].strip()
            firstline_address3 = global_booking_address1.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            no_hyphens_dob_global3 = re.sub('-','',DOB_global3)
            d2 = "-"
            global_datenamez3 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global3
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_3 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_3 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email3 = driver.find_element_by_xpath(gmail_apt_email_path).text
            ########################################################################            
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
            gender_global4 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname4 = str(last_name1.split(sep, 1)[1])
################################################
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address4 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_4 = global_booking_address1.split(",")[3].strip()
            globalstate_4 = global_booking_address1.split(",")[2].strip()
            globalcity_4 = global_booking_address1.split(",")[1].strip()
            firstline_address4 = global_booking_address1.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            no_hyphens_dob_global4 = re.sub('-','',DOB_global4)
            d2 = "-"
            global_datenamez3 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global3
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_3 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_3 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email3 = driver.find_element_by_xpath(gmail_apt_email_path).text
            ########################################################################   
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
            gender_global5 = driver.find_element_by_xpath(gender_global_path).text
            global_firstname5 = str(last_name1.split(sep, 1)[1])
################################################
            wait.until(EC.presence_of_element_located(By.XPATH, booking_address_xpath))
            global_booking_address5 = driver.find_element_by_xpath(booking_address_xpath).text
            globalzip_5 = global_booking_address1.split(",")[3].strip()
            globalstate_5 = global_booking_address1.split(",")[2].strip()
            globalcity_5 = global_booking_address1.split(",")[1].strip()
            firstline_address5 = global_booking_address1.split(",")[0].strip()
            date2222 = datetime.datetime.today().strftime('%m-%d-%Y')
            no_hyphens_dob_global5 = re.sub('-','',DOB_global5)
            d2 = "-"
            global_datenamez5 = str(last_name1.split(sep, 1)[1]) + " " + date2222 + no_hyphens_dob_global5
            wait.until(EC.presence_of_element_located(By.XPATH, booking_phone_path))
            global_homephone_5 = driver.find_element_by_xpath(booking_phone_path).text
            global_alternate_5 = driver.find_element_by_xpath(alternate_phone_xpath).text
            global_email5 = driver.find_element_by_xpath(gmail_apt_email_path).text
            ########################################################################  

        else:
            pass
    find_defendent_info()
    replace_doc_values_and_print()


# Open_amp -> apppointment_iteration ->find defendent info -> open gmail -> booker -> open drive -> replace_dochub_values() -> print dochub letters()

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

        

open_amp() #this is the fuse
time.sleep(15 * 60)
driver.close()
