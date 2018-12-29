import time

import keyboard
from selenium.webdriver.common.by import By
from selenium import webdriver
from _datetime import datetime
import holidays
from selenium.common.exceptions import *
import longo
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
user00 = "lawofficeofleonardmartinezdocu@gmail.com"
pass00 = ""

driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
wait = WebDriverWait(driver, 10)
def inserto9(i,j):
    listed_defs = longo.amp_def_array
    lambs = listed_defs[i][j]
    for lamb in lambs:
        replacement_casenumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_courtnumber_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[7]/td[3]/b/font/input"
        replacement_date_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[9]/td[3]/b/font/input"
        replacement_offense_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[13]/td[3]/b[2]/font/input"
        replacement_time_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[10]/td[3]/b[2]/font/input"
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_casenumber_path))
        replacement_casenumber = driver.find_element_by_xpath(replacement_casenumber_path)
        replacement_casenumber.clear()
        replacement_casenumber.send_keys(str(lamb[0]))
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_courtnumber_path))
        replacement_courtnumber = driver.find_element_by_xpath(replacement_courtnumber_path)
        replacement_courtnumber.clear()
        replacement_courtnumber.send_keys(str(lamb[5]))
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_date_path))
        replacement_date = driver.find_element_by_xpath(replacement_date_path)
        replacement_date.clear()
        replacement_date.send_keys((str(lamb[1])).split(' ', 1)[0])
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_offense_path))
        replacement_offense = driver.find_element_by_xpath(replacement_offense_path)
        replacement_offense.clear()
        replacement_offense.send_keys(str(lamb[6]))
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_time_path))
        replacement_time = driver.find_element_by_xpath(replacement_time_path)
        replacement_time.send_keys((str(lamb[1])).split(' ', 1)[1])
        replacement_setting_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[11]/td[3]/b[2]/font/input"
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_setting_path))
        replacement_setting = driver.find_element_by_xpath(replacement_setting_path)
        replacement_setting.click()
        replacement_setting.clear()
        replacement_setting.send_keys(str(lamb[2]))
        replacement_bond_path = "/html/body/form/div[2]/table/tbody/tr[1]/td/div[1]/table/tbody/tr[18]/td[3]/b/font/input"
        wait.until(EC.presence_of_element_located(By.XPATH, replacement_bond_path))
        replacement_bond = driver.find_element_by_xpath(replacement_bond_path)
        replacement_bond.click()
        replacement_bond.clear()
        replacement_bond.send_keys(str(lamb[3]))
        case_elaw_save_close_path = "/html/body/form/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/a[1]"
        wait.until(EC.presence_of_element_located(By.XPATH, case_elaw_save_close_path))
        case_elaw_save_close = driver.find_element_by_xpath(case_elaw_save_close_path)
        case_elaw_save_close.click()
        waito(3)


def insert_case_values(i,j):
    listed_defs = longo.amp_def_array
    cases:list = listed_defs[i]
    for p in range(cases):
        try:
            add_case_elaw()
            inserto9(i,j)
        except:
            pass


def open_docs():
    open_docs_url = "https://docs.google.com/document/d/15Qk0UM2f9G7glB0BOL-hPeN86o_YN9YjfRvj53riBMQ/edit?usp=sharing"
    sign_in_docs_path = "//*[@id=\"gb\"]/div/div/a"
    docs_email_path = "//*[@id=\"identifierId\"]"
    docs_pass_path = "//*[@id=\"password\"]/div[1]/div/div[1]/input"
    docs_next_path = "//*[@id=\"passwordNext\"]"
    more_options_path = "//*[@id=\"docs-findbar-button-more-options\"]"
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


def hover(x):
    hover1 = ActionChains(driver).move_to_element(x)
    a = hover1.perform()
    return a


def new_amp_appointments():
    driver.get('https://idc.traviscountytx.gov/nidp/idff/sso?id=35&sid=2&option=credential&sid=2&target=https%3A%2F%2Fcourts.traviscountytx.gov%2Famp%2F')
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
    pass1.send_keys("")
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
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_search4)))
    search4 = driver.find_element_by_xpath(xpath_search4)
    search4.click()


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_plt(x):
    try:
        driver.find_element_by_partial_link_text(x)
    except NoSuchElementException:
        return False
    return True


def cebplt(x):
    return check_exists_by_plt(x)

def add_case_elaw():
    waito(1)
    x = driver.find_element_by_link_text("Create")
    hover(x)
    waito(1)
    driver.find_element_by_link_text("Add Case").click()



def cebx(x):
    return check_exists_by_xpath(x)


def open_elaw():
    driver.get('https://www5.elawsoftware.com/eLawSecure.nsf/SecureLogin?ReadForm')
    user1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[1]/td[3]/input"
    pass1_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[2]/td[3]/input"
    access_server_XPATH = "/html/body/form/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[3]/td[1]/div/input"
    # find the elements to click and interact with
    user1 = driver.find_element_by_xpath(user1_XPATH)
    pass1 = driver.find_element_by_xpath(pass1_XPATH)
    access1 = driver.find_element_by_xpath(access_server_XPATH)
    user1.send_keys("Leonard.martinez")
    pass1.send_keys("")
    access1.click()

def open_new_client_form():
    open_elaw()
    x = driver.find_element_by_link_text("Create")
    waito(2)
    hover(x)
    waito(1)
    driver.find_element_by_link_text("New Client File").click()
    waito(1)


def waito(x):
    waite = WebDriverWait(driver, x)
    return waite


def waitp(x):
    y = wait.until(EC.presence_of_element_located((By.XPATH, x)))
    return y


def open_sheriff(y):
    if (y == '') or (y == 0):
        driver.get('https://public.co.travis.tx.us/sips/default.aspx')
        return False
    else:
        driver.get('https://public.co.travis.tx.us/sips/default.aspx')
        first_initial_XPATH = "//*[@id=\"FirstInitial\"]"
        lastname_XPATH = "//*[@id=\"LastName\"]"
        waitp(lastname_XPATH)
        submitter = "//*[@id=\"SubmitNameSearch\"]"
        ln = y.split(',', 1)[0]
        fn = y.split(', ', 1)[1][0]
        fbxp(lastname_XPATH).send_keys(ln)
        fbxp(first_initial_XPATH).send_keys(fn)
        waito(.1)
        submit = driver.find_element_by_xpath(submitter)
        submit.click()
        waito(.3)
        submit1path = "//*[@id=\"SubmitInmate\"]"
        waito(2)
        if cebx(submit1path) == True:
            submit1 = fbxp(submit1path)
            submit1.click()
            return True
        else:
            return False


def next_business_day(x):
    if x == '':
        ONE_DAY = datetime.timedelta(days=1)
        HOLIDAYS_US = holidays.US()
        next_day = datetime.date.today() + ONE_DAY
        while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_US:
            next_day += ONE_DAY
        return next_day
    else:
        ONE_DAY = datetime.timedelta(days=x)
        HOLIDAYS_US = holidays.US()
        next_day = datetime.today() + ONE_DAY
        while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_US:
            next_day += ONE_DAY
        return next_day


def converted_next_business_day(x):
    if (x == 0) or (x == ""):
        next_day = next_business_day(1)
        day = str(next_day.day)
        d1 = "/"
        month = str(next_day.month)
        yr = str(next_day.year)
        formatted = month + d1 + day + d1 + yr
        return formatted
    else:
        next_day = next_business_day(x)
        day = str(next_day.day)
        d1 = "/"
        month = str(next_day.month)
        yr = str(next_day.year)
        formatted = month + d1 + day + d1 + yr
        return formatted

def dash_converted_next_business_day(x):
    if (x == 0) or (x == ""):
        next_day = next_business_day(0)
        day = str(next_day.day)
        d1 = "-"
        month = str(next_day.month)
        yr = str(next_day.year)
        formatted = month + d1 + day + d1 + yr
        return formatted
    else:
        next_day = next_business_day(x)
        day = str(next_day.day)
        d1 = "/"
        month = str(next_day.month)
        yr = str(next_day.year)
        formatted = month + d1 + day + d1 + yr
        return formatted

def fbxp(x):
    go = driver.find_element_by_xpath(x)
    return go


def open_gmail(y):  # MUST USE FULL DEFENDENT NAME OR BOOKING NUMBER!
    if (y == '') or (y == 0):
        html_1url = "https://mail.google.com/mail/?ui=html"
        signin_gmail_path = "/html/body/nav/div/a[2]"
        login5path = "//*[@id=\"identifierId\"]"
        pass5path = "//*[@id=\"password\"]/div[1]/div/div[1]/input"
        pass00 = ""
        user00 = "lawofficeofleonardmartinezdocu@gmail.com"
        gmail_next_path = "//*[@id=\"passwordNext\"]"
        driver.get(html_1url)
        signin_gmail = driver.find_element_by_xpath(signin_gmail_path)
        wait0 = WebDriverWait(driver, 10)
        wait0.until(EC.presence_of_element_located(By.XPATH, signin_gmail_path))
        signin_gmail.click()
        wait0.until(EC.presence_of_element_located(By.XPATH, login5path))
        login5 = driver.find_element_by_xpath(login5path)
        login5.send_keys(user00)
        wait0.until(EC.presence_of_element_located(By.XPATH, pass5path))
        pass5 = driver.find_element_by_xpath(pass5path)
        pass5.send_keys(pass00)
        wait0.until(EC.presence_of_element_located(By.XPATH, gmail_next_path))
        driver.find_element_by_xpath(gmail_next_path).click()
        driver.get(html_1url)
        return "Opened Gmail Non-Specific Defendent"
    else:
        html_1url = "https://mail.google.com/mail/?ui=html"
        signin_gmail_path = "/html/body/nav/div/a[2]"
        login5path = "//*[@id=\"identifierId\"]"
        pass5path = "//*[@id=\"password\"]/div[1]/div/div[1]/input"
        pass00 = ""
        user00 = "lawofficeofleonardmartinezdocu@gmail.com"
        gmail_next_path = "//*[@id=\"passwordNext\"]"
        driver.get(html_1url)
        wait0 = WebDriverWait(driver, 10)
        signin_gmail = driver.find_element_by_xpath(signin_gmail_path)
        wait0.until(EC.presence_of_element_located(By.XPATH, signin_gmail_path))
        signin_gmail.click()
        wait0.until(EC.presence_of_element_located(By.XPATH, login5path))
        login5 = driver.find_element_by_xpath(login5path)
        login5.send_keys(user00)
        wait0.until(EC.presence_of_element_located(By.XPATH, pass5path))
        pass5 = driver.find_element_by_xpath(pass5path)
        pass5.send_keys(pass00)
        wait0.until(EC.presence_of_element_located(By.XPATH, gmail_next_path))
        driver.find_element_by_xpath(gmail_next_path).click()
        driver.get(html_1url)
        gmailht_searchbtnpath = "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/input[2]"
        gmailht_searchpath = "//*[@id=\"sbq\"]"
        wait0.until(EC.presence_of_element_located(By.XPATH, gmailht_searchpath))
        gmailht_search = driver.find_element_by_xpath(gmailht_searchpath)
        gmailht_search.click().clear().send_keys(y)
        wait0.until(EC.presence_of_element_located(By.XPATH, gmailht_searchbtnpath))
        gmail_srch_button = driver.find_element_by_xpath(gmailht_searchbtnpath)
        gmail_srch_button.click()
        waito(1)
        xpath_go = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]/a"
        waitp(xpath_go)
        fbxp(xpath_go).click()
        waito(1)
        lnf_name_gmail_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[5]/span[2]"
        gender_gmaiL_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/p[24]/span[2]"
        arrest_date_gmail_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/p[18]/span[2]"
        booking_phone_gmail_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/p[19]/span[2]"
        alternate_phone_gmail_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/p[20]/span[3]"
        email_gmail_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/p[21]/span[3]/a"
        dob_gmail_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/p[23]/span[2]"
        address_gmail_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/p[17]/span[2]"
        notes_gmaiL_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/p[28]/span"
        waitp(lnf_name_gmail_path)
        last_name_first = fbxp(lnf_name_gmail_path).text
        booking_number_gmail_path = "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div[1]/div/div[2]/div/div[2]/div/p[6]/span[2]"
        gender = fbxp(gender_gmaiL_path).text
        arrest_date = fbxp(arrest_date_gmail_path).text
        booking_phone = fbxp(booking_phone_gmail_path).text
        alternate_phone = fbxp(alternate_phone_gmail_path).text
        email = fbxp(email_gmail_path).text
        dob = fbxp(dob_gmail_path).text
        address = fbxp(address_gmail_path).text
        notes = fbxp(notes_gmaiL_path).text
        booking_number = fbxp(booking_number_gmail_path).text
        sep = ","
        sep1 = ", "
        last_name = last_name_first.split(sep, 1)[0]
        first_names = last_name_first.split(sep1, 1)[1]
        middle_name = ""
        first_name = first_names
        try:
            middle_name = last_name_first.split(" ", 1)[2]
            first_name = first_names.replace(middle_name, '')
        except:
            pass

        def_dictionary = {"legal name": last_name_first, "phone": booking_phone, "alt phone": alternate_phone, "address": address, "notes": notes, "gender": gender, "arrest date": arrest_date, "dob": dob, "email": email, "last name": last_name, "middle name": middle_name, "first name": first_name, "booking number": booking_number}
        jail_status = open_sheriff(last_name_first)
        def_array = last_name_first, booking_number, dob, address, email, booking_phone, alternate_phone, gender, notes, arrest_date, jail_status
        return def_dictionary, def_array  # 13 and 10 long


def in_def_amp():
    amp_def_array_xpaths = longo.amp_def_array_xpaths
    amp_def_array = longo.amp_def_array
    a = amp_def_array
    for i in range(len(amp_def_array_xpaths)):
        try:
            waitp(amp_def_array_xpaths[i])
            b = fbxp(amp_def_array_xpaths[i]).text
            if a[i] == "":
                a[i] = b
        except:
            print("Case not found!")
    return a


def amp_to_list_letter():  # Get a list of defendents, containing a list of cases, which is a list of case info
    defs = longo.defs
    defs_not = longo.defs_nots
    listed_defs = []
    listed_gmail = []
    for i in range(5):
        new_amp_appointments()
        try:
            waito(3)
            if fbxp(defs_not[i]).text == 2:
                name = fbxp(longo.names_xp[i]).text
                waitp(defs[i])
                fbxp(defs[i]).click()
                listed_defs.append(in_def_amp())
                gmail_defendent_values = open_gmail(name)[1]
                listed_gmail.append(gmail_defendent_values)
                try:
                    open_docs()
                    keyboard.press_and_release('ctrl+f')
                    path_closer1 = "/html/body/div[61]/div[1]/span[2]"
                    path_replace_what: str = "//*[@id=\"docs-findandreplacedialog-input\"]"
                    path_replace_with: str = "//*[@id=\"docs-findandreplacedialog-replace-input\"]"
                    path_replace_all: str = "//*[@id=\"docs-findandreplacedialog-button-replace-all\"]"
                    orig_date = "Date:"
                    orig_legalname = "v."
                    orig_lnf = "Defendant:"
                    custom_pages_path = "//*[@id=\"page-settings-custom-input\"]"
                    orig_dob = "DOB:"
                    orig_booking = "Booking No."
                    orig_salutations = "Dear"
                    pn1 = "Mr. "
                    global_pronoun = pn1
                    # 44 suffix means final replacement values per defendant
                    date44 = orig_date + " " + str(converted_next_business_day())
                    legalname44 = orig_legalname + " " + (gmail_defendent_values[0].split(", ", 1)[1]) + ", " + (gmail_defendent_values[0].split(", ", 1)[0])
                    birthday44 = orig_dob + " " + gmail_defendent_values[2]
                    lnf44 = orig_lnf + " " + gmail_defendent_values[0]
                    salutations44 = orig_salutations + " " + global_pronoun + (
                    gmail_defendent_values[0].split(", ", 1)[0]) + ","
                    if gmail_defendent_values[7] != "Male":
                        pn2 = "Ms. "
                        salutations44 = pn2
                    booking44 = orig_booking + " " + gmail_defendent_values[1]
                    replacements = [date44, lnf44, birthday44, booking44, legalname44, salutations44]
                    origs = [orig_date, orig_lnf, orig_dob, orig_booking, orig_legalname, orig_salutations]
                    for j in range(len(replacements)):
                        wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
                        replace_what = fbxp(path_replace_what)
                        replace_what.clear()
                        replace_what.send_keys(origs[j])
                        wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
                        replace_with = fbxp(path_replace_with)
                        replace_with.clear()
                        replace_with.send_keys(gmail_defendent_values[j])
                    # start printing
                    path_print_def = "//*[@id=\"print-header\"]/div/button[2]"
                    normal_pages_path = "//*[@id=\"page-settings\"]/div[2]/div/div[1]/label/input"
                    keyboard.press_and_release("ctrl+p")
                    wait.until(EC.presence_of_element_located(By.XPATH, normal_pages_path))
                    normal_pages = driver.find_element_by_xpath(normal_pages_path)
                    normal_pages.click()
                    wait.until(EC.presence_of_element_located(By.XPATH, path_print_def))
                    print_def = driver.find_element_by_xpath(path_print_def)
                    print_def.click()
                    keyboard.press_and_release('enter')
                    time.sleep(5)
                    keyboard.press_and_release("ctrl+p")
                    wait.until(EC.presence_of_element_located(By.XPATH, custom_pages_path))
                    custom_pages = driver.find_element_by_xpath(custom_pages_path)
                    custom_pages.click()
                    custom_pages.send_keys("1")
                    wait.until(EC.presence_of_element_located(By.XPATH, path_print_def))
                    print_def.click()
                    time.sleep(5)
                    for p in range(len(replacements)):
                        wait.until(EC.presence_of_element_located(By.XPATH, path_replace_what))
                        replace_what = fbxp(path_replace_what)
                        replace_what.clear()
                        replace_what.send_keys(origs[p])
                        wait.until(EC.presence_of_element_located(By.XPATH, path_replace_with))
                        replace_with = fbxp(path_replace_with)
                        replace_with.clear()
                        replace_with.send_keys(origs[p])
                        time.sleep(3)
                except:
                    pass
            else:
                waitp(defs[i])
                fbxp(defs[i]).click()
                listed_defs.append(in_def_amp())
                listed_gmail.append(gmail_defendent_values)
        except:
            pass
    return listed_defs, listed_gmail


def create_new_clients():
    # 22 Long
    elaw_client_paths = longo.elaw_client_paths
    listed_defs = amp_to_list_letter()[0]
    listed_gmail = amp_to_list_letter()[1]
    #            def_array = last_name_first, booking_number, dob, address, email, booking_phone, alternate_phone, gender, notes, arrest_date, jail_status

    for i in range(5):
        try:
            delvalle = "3614 Bill Price Rd, Del Valle, TX, 78617"
            open_new_client_form()
            city = listed_gmail[i][3].split(',', 1)[1]
            state = listed_gmail[i][3].split(',', 1)[2]
            zip_code = listed_gmail[i][3].split(',', 1)[3]
            phone = listed_gmail[i][5]
            alt_phone = listed_gmail[i][6]
            email = listed_gmail[i][4]
            gender = listed_gmail[i][7]
            dob = listed_gmail[2]
            waitp(elaw_client_paths[15])
            fbxp(elaw_client_paths[15]).send_keys(dob)
            first_address = listed_gmail[i][3].split(',', 1)[0]
            first_name = listed_gmail[i][0].split(", ", 1)[1]
            last_name = listed_gmail[i][0].split(", ", 1)[0]
            booking_number = listed_gmail[i][1]
            waitp(elaw_client_paths[12])
            fbxp(elaw_client_paths[12]).send_keys(booking_number)
            wait.until(EC.presence_of_element_located(By.XPATH, longo.elaw_client_paths[10]))
            court_no_elaw = driver.find_element_by_xpath(longo.elaw_client_paths[10])
            court_no_elaw.click()
            wait.until(EC.presence_of_element_located(By.XPATH, longo.elaw_client_paths[11]))
            elaw_appt_yes = driver.find_element_by_xpath(longo.elaw_client_paths[11])
            elaw_appt_yes.click()  # one of 12 sub functions
            second_address = ""
            waitp(elaw_client_paths[19])
            fbxp(elaw_client_paths[19]).send_keys(first_name + str(dash_converted_next_business_day()) + "-" + listed_gmail[2].replace("/", ""))
            fbxp(elaw_client_paths[20]).send_keys(last_name.upper())
            if listed_gmail[i][10] == True:
                first_address = "Travis County Correctional Complex"
                second_address = "3614 Bll Price Rd"
                city = "Del Valle"
                state = "TX"
                zip_code = "78617"
                wait.until(EC.presence_of_element_located(By.XPATH, longo.elaw_client_paths[11]))
                jail_no_elaw = driver.find_element_by_xpath(longo.elaw_client_paths[10])
                jail_no_elaw.click()
                wait.until(EC.presence_of_element_located(By.XPATH, longo.elaw_client_paths[11]))
                jail_yes_elaw = driver.find_element_by_xpath(longo.elaw_client_paths[11])
                jail_yes_elaw.click()
            waitp(elaw_client_paths[8])
            fbxp(elaw_client_paths[8]).send_keys(first_address)
            waitp(elaw_client_paths[9])
            fbxp(elaw_client_paths[9]).send_keys(second_address)
            for j in range(6):
                seven = [city, state, zip_code, phone, alt_phone, email]
                waitp(elaw_client_paths[j])
                fbxp(elaw_client_paths[j]).send_keys(seven[j])
            if gender != "Male":
                waitp(elaw_client_paths[7])
                sal = fbxp(elaw_client_paths[6])
                sal.click()
                sal.send_keys("down")
                sal2 = fbxp(elaw_client_paths[7])
                sal2.click()
            save = elaw_client_paths[16]
            waitp(save)
            fbxp(save).click()
            try:
                insert_case_values(i, len(case))


                insert_case_logic() # use index i, and a for loop with the cases from 1-5 or whatever length is)
#amp_def_array = [cause1_cn, cause1_dt, cause1_set, cause1_bond, cause1_level, cause1_crt, cause1_charge, cause1_indict, cause2_cn, cause2_dt, cause2_set, cause2_bond, cause2_level, cause2_crt, cause2_charge, cause2_indict, cause3_cn, cause3_dt, cause3_set, cause3_bond, cause3_level, cause4_crt, cause3_charge, cause3_indict, cause4_cn, cause4_dt, cause4_set, cause4_bond, cause4_level, cause4_crt, cause4_charge, cause4_indict, cause5_cn, cause5_dt, cause5_set, cause5_bond, cause5_level, cause5_crt, cause5_charge, cause5_indict]

        except:
            pass
