import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from _datetime import datetime
import holidays
from selenium.common.exceptions import *
import longo
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
wait = WebDriverWait(driver, 10)


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
        return def_dictionary


def in_def_amp():
    amp_def_array_xpaths = longo.amp_def_array_xpaths
    amp_def_array = longo.amp_def_array
    a = amp_def_array
    for i in range((len(amp_def_array_xpaths))-1):
        try:
            waitp(amp_def_array_xpaths[i])
            b = fbxp(amp_def_array_xpaths[i]).text
            if a[i] == "":
                a[i] = b
        except:
            print("Case not found!")
    return a


def amp_to_elaw():  # Get a list of defendents, containing a list of cases, which is a list of case info
    new_amp_appointments()
    defs = longo.defs
    listed_defs = []
    for i in range(5):
        try:
            waitp(defs[i])
            fbxp(defs[i]).click()
            listed_defs.append(in_def_amp())
        except:
            pass
    return listed_defs
