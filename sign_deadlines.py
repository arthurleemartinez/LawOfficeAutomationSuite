from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
global savepath_amp
savepath_amp = "//*[@id=\"required-act-save-view\"]/div[2]/div[3]/ul/li[2]/input"
global xpath_deadline_1, xpath_deadline_2, xpath_deadline_3, xpath_deadline_1_number
global xpath_deadline_2_number, xpath_deadline_3_number, xpath_initial_contact_date, wait
global xpath_deadline_4, xpath_deadline_5, xpath_deadline_4_number, xpath_deadline_5_number
xpath_initial_contact_date = "//*[@id=\"required-act-grid\"]/table/tbody/tr[2]/td[2]/span[2]"
xpath_real_deadline = "//*[@id=\"required-act-grid\"]/table/tbody/tr[2]/td[2]/span[2]"
xpath_real_edit = "//*[@id=\"required-act-grid\"]/table/tbody/tr[2]/td[6]/a/i"
xpath_deadline_1 = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[1]/td[5]/menu[2]"
xpath_deadline_2 = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[2]/td[5]/menu[2]"
xpath_deadline_3 = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[3]/td[5]/menu[2]"
xpath_deadline_4 = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[4]/td[5]/menu[2]"
xpath_deadline_5 = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[5]/td[5]/menu[2]"
xpath_deadline_1_number = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[1]/td[5]/menu[2]/a/i[2]"
xpath_deadline_2_number = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[2]/td[5]/menu[2]/a/i[2]"
xpath_deadline_3_number = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[3]/td[5]/menu[2]/a/i[2]"
xpath_deadline_4_number = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[4]/td[5]/menu[2]/a/i[2]"
xpath_deadline_5_number = "//*[@id=\"case-grid\"]/div[2]/table/tbody/tr[5]/td[5]/menu[2]/a/i[2]"
global contact_method_button_path, letter_btn_path
letter_btn_path = "//*[@id=\"contact-method_listbox\"]/li[1]"
contact_method_button_path = "//*[@id=\"required-act-save-view\"]/div[2]/form/div[1]/div[2]/span/span/span[1]"
global user00, pass00
user00 = "Sbn13142750"
pass00 = ""

driver: WebDriver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
wait = WebDriverWait(driver, 10)
def open_amp_only():
    driver: WebDriver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
    driver.get("https://idc.traviscountytx.gov/nidp/idff/sso?id=35&sid=2&option=credential&sid=2&target=https%3A%2F%2Fcourts.traviscountytx.gov%2Famp%2F")
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
    user1.send_keys()
    pass1.send_keys(pass00)
    access1.click()
    driver.get("https://courts.traviscountytx.gov/AMP/Cases/Search")

def check_number_of_alerts_deadline_boxes():
    global deadlines_count, deadline_1_btn, deadline_number_1, deadline_2_btn, deadline_3_btn, deadline_4_btn, deadline_5_btn
    global deadline_number_2, deadline_number_3, deadline_number_4, deadline_number_5
    global date_of_contact_path
    date_of_contact_path = "//*[@id=\"date\"]"
    deadlines_count = 0
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_deadline_1)))
    deadline_1_btn = driver.find_element_by_xpath(xpath_deadline_1)
    deadline_2_btn = driver.find_element_by_xpath(xpath_deadline_2)
    deadline_3_btn = driver.find_element_by_xpath(xpath_deadline_3)
    deadline_4_btn = driver.find_element_by_xpath(xpath_deadline_4)
    deadline_5_btn = driver.find_element_by_xpath(xpath_deadline_5)
    deadline_number_1 = driver.find_element_by_xpath(xpath_deadline_1_number).text
    deadline_number_2 = driver.find_element_by_xpath(xpath_deadline_1_number).text
    deadline_number_3 = driver.find_element_by_xpath(xpath_deadline_1_number).text
    deadline_number_4 = driver.find_element_by_xpath(xpath_deadline_1_number).text
    deadline_number_5 = driver.find_element_by_xpath(xpath_deadline_1_number).text

    if xpath_deadline_1_number == "1":
        deadlines_count = 0
    elif xpath_deadline_1_number == "2" and deadline_number_2 == "1":
        deadlines_count = 1
    elif xpath_deadline_1_number == "2" and deadline_number_2 == "2":
        deadlines_count = 2
    elif xpath_deadline_1_number == "2" and deadline_number_3 == "2":
        deadlines_count = 3
    elif xpath_deadline_1_number == "2" and deadline_number_4 == "2":
        deadlines_count = 4
    elif xpath_deadline_1_number == "2" and deadline_number_5 == "2":
        deadlines_count = 5
def return_searches():
    driver.get("https://courts.traviscountytx.gov/AMP/Cases/Search")
    wait.until(EC.presence_of_element_located((By.XPATH, user1_XPATH)))


def iterate_boxes_once():
    return_searches()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_deadline_1)))
    deadline_1_btn = driver.find_element_by_xpath(xpath_deadline_1)
    deadline_1_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_deadline)))
    replace_deadline = driver.find_element_by_xpath(xpath_real_deadline)
    d12 = replace_deadline.text
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_edit)))
    edit = driver.find_element_by_xpath(xpath_real_edit)
    edit.click()
    wait.until(EC.presence_of_element_located((By.XPATH, contact_method_button_path)))
    contact_btn = driver.find_element_by_xpath(contact_method_button_path)
    contact_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, letter_btn_path)))
    letter_btn = driver.find_element_by_xpath(letter_btn_path)
    letter_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, date_of_contact_path)))
    date_of_contact = driver.find_element_by_xpath(date_of_contact_path)
    date_of_contact.send_keys(d12)
    wait.until(EC.presence_of_element_located((By.XPATH, savepath_amp)))
    save_amp1 = driver.find_element_by_xpath(savepath_amp)
    save_amp1.click()
def iterate_boxes_two():
    iterate_boxes_once()
    return_searches()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_deadline_2)))
    deadline_1_btn = driver.find_element_by_xpath(xpath_deadline_2)
    deadline_1_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_deadline)))
    replace_deadline = driver.find_element_by_xpath(xpath_real_deadline)
    d12 = replace_deadline.text
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_edit)))
    edit = driver.find_element_by_xpath(xpath_real_edit)
    edit.click()
    wait.until(EC.presence_of_element_located((By.XPATH, contact_method_button_path)))
    contact_btn = driver.find_element_by_xpath(contact_method_button_path)
    contact_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, letter_btn_path)))
    letter_btn = driver.find_element_by_xpath(letter_btn_path)
    letter_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, date_of_contact_path)))
    date_of_contact = driver.find_element_by_xpath(date_of_contact_path)
    date_of_contact.send_keys(d12)
    wait.until(EC.presence_of_element_located((By.XPATH, savepath_amp)))
    save_amp1 = driver.find_element_by_xpath(savepath_amp)
    save_amp1.click()
def iterate_boxes_three():
    iterate_boxes_two()
    return_searches()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_deadline_3)))
    deadline_1_btn = driver.find_element_by_xpath(xpath_deadline_3)
    deadline_1_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_deadline)))
    replace_deadline = driver.find_element_by_xpath(xpath_real_deadline)
    d12 = replace_deadline.text
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_edit)))
    edit = driver.find_element_by_xpath(xpath_real_edit)
    edit.click()
    wait.until(EC.presence_of_element_located((By.XPATH, contact_method_button_path)))
    contact_btn = driver.find_element_by_xpath(contact_method_button_path)
    contact_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, letter_btn_path)))
    letter_btn = driver.find_element_by_xpath(letter_btn_path)
    letter_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, date_of_contact_path)))
    date_of_contact = driver.find_element_by_xpath(date_of_contact_path)
    date_of_contact.send_keys(d12)
    wait.until(EC.presence_of_element_located((By.XPATH, savepath_amp)))
    save_amp1 = driver.find_element_by_xpath(savepath_amp)
    save_amp1.click()
def iterate_boxes_four():
    iterate_boxes_three()
    return_searches()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_deadline_4)))
    deadline_1_btn = driver.find_element_by_xpath(xpath_deadline_4)
    deadline_1_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_deadline)))
    replace_deadline = driver.find_element_by_xpath(xpath_real_deadline)
    d12 = replace_deadline.text
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_edit)))
    edit = driver.find_element_by_xpath(xpath_real_edit)
    edit.click()
    wait.until(EC.presence_of_element_located((By.XPATH, contact_method_button_path)))
    contact_btn = driver.find_element_by_xpath(contact_method_button_path)
    contact_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, letter_btn_path)))
    letter_btn = driver.find_element_by_xpath(letter_btn_path)
    letter_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, date_of_contact_path)))
    date_of_contact = driver.find_element_by_xpath(date_of_contact_path)
    date_of_contact.send_keys(d12)
    wait.until(EC.presence_of_element_located((By.XPATH, savepath_amp)))
    save_amp1 = driver.find_element_by_xpath(savepath_amp)
    save_amp1.click()
def iterate_boxes_five():
    iterate_boxes_four()
    return_searches()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_deadline_5)))
    deadline_1_btn = driver.find_element_by_xpath(xpath_deadline_5)
    deadline_1_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_deadline)))
    replace_deadline = driver.find_element_by_xpath(xpath_real_deadline)
    d12 = replace_deadline.text
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_real_edit)))
    edit = driver.find_element_by_xpath(xpath_real_edit)
    edit.click()
    wait.until(EC.presence_of_element_located((By.XPATH, contact_method_button_path)))
    contact_btn = driver.find_element_by_xpath(contact_method_button_path)
    contact_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, letter_btn_path)))
    letter_btn = driver.find_element_by_xpath(letter_btn_path)
    letter_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, date_of_contact_path)))
    date_of_contact = driver.find_element_by_xpath(date_of_contact_path)
    date_of_contact.send_keys(d12)
    wait.until(EC.presence_of_element_located((By.XPATH, savepath_amp)))
    save_amp1 = driver.find_element_by_xpath(savepath_amp)
    save_amp1.click()

def conditional2():
    if deadlines_count == 1:
        iterate_boxes_once()
    elif deadlines_count == 2:
        iterate_boxes_two()
    elif deadlines_count == 3:
        iterate_boxes_three()
    elif deadlines_count == 4:
        iterate_boxes_four()
    elif deadlines_count == 5:
        iterate_boxes_five()
    else:
        pass

open_amp_only()
check_number_of_alerts_deadline_boxes()
conditional2()
driver.close()
