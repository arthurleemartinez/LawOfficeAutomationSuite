from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import keyboard
import os
import shutil
import glob
import os
import zipfile
singular_globa_name = ""

def prompt():
  answer = input("Copy and paste the url here and hit enter. If you have a case number please type/paste it here as well and hit enter.")
  print("Response accepted. Accessing TechShare...")
  return answer


def open_techshare():
  answer = prompt()
  print("Opening chrome robot...")
  driver = webdriver.Chrome(executable_path='C:/Users/Arthur Martinez/chromedriver.exe')
   # 12 SECONDS TO LET LOAD
   # access url
  print("Loading TechShare...")
  wait = WebDriverWait(driver, 15)
   """ user1_css = "td[class=\"ember-view ember-text-field required\"][data-key=\"username\"]"
   pass1_css = "td[class=\"ember-view ember-text-field required\"][data-key=\"password\"]"
   access_server_XPATH = "//*[@id=\"loginButton\"]"
   # find the elements to click and interact with
   wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, user1_css)))
   user1 = driver.find_element_by_css_selector(user1_css)
   wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, pass1_css)))
   pass1 = driver.find_element_by_css_selector(pass1_css)
   print("Logging in...")
   wait.until(EC.presence_of_element_located((By.XPATH, access_server_XPATH)))
   access1 = driver.find_element_by_xpath(access_server_XPATH)
   user1.send_keys("Lmartinez1314")
   pass1.send_keys("Lm13142750*")
   access1.click()"""
  casewords = ["c-1", "C1", "C-1", "c1", "D-1", "d-1", "d1", "D1"]
  print("Figuring out what information you gave me...")
  if ".org" not in answer:
    for caseword in casewords:
      if caseword in answer:
        answer.strip("-")
        answer.upper()
    print("Searching for case...")
    xpath_search4 = "//*[@id=\"search\"]"
    wait.until(EC.presence_of_element_located((By.XPATH, xpath_search4)))
    search4 = driver.find_element_by_xpath(xpath_search4)
    search4.click()
    search4.send_keys(answer)
    print("Waiting 3 seconds for web-loading...")
    driver.implicitly_wait(3)
    try:
      wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, answer)))
      caselink = driver.find_element_by_partial_link_text(answer)
      caselink.click()
      print("Loading client/case page...")
    except:
      print("Failed to click case.")
  else:
    print("Loading client's TechShare page...")
    driver.get(answer)
    time.sleep(3)
    name_client_web_xpath = "//*[@id=\"ember440\"]/fieldset[1]/legend/text()"
    name_client_web = driver.find_element_by_xpath(name_client_web_xpath).text
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.write("Lmartinez1314")
    keyboard.press_and_release('tab')
    keyboard.write("Lm13142750*1")
    keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')
    time.sleep(2)
    driver.get(answer)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View DME")))
    vDME = driver.find_element_by_link_text("View DME")
    vDME.click()
    driver.implicitly_wait(5)
    try:
          """wait.until(EC.presence_of_element_located((By.XPATH, "// *[ @ id = \"content\"] / fieldset[3] / div")))
          words = driver.find_element_by_xpath("// *[ @ id = \"content\"] / fieldset[3] / div").text
          if words == "There is no DME for this case that meets the filter criteria.":
            print("THERE IS NO DIGITAL MEDIA EVIDENCE FOR THIS CLIENT AS OF NOW! Come back later...")"""
      sadme_xp = "//*[@id=\"selectAllDme\"]"
      wait.until(EC.presence_of_element_located((By.XPATH, sadme_xp)))
      sadme = driver.find_element_by_xpath(sadme_xp)
      sadme.click()
       # "//*[@id=\"content\"]/fieldset[3]/p/a"
      print("Attempting to download all of the client's files...")
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Download Selected")))
        DS = driver.find_element_by_link_text("Download Selected")
        DS.click()
      singular_global_name = name_client_web
    except:
      print("Failed to download! Program Exiting. Alert Arthur of his wretched failures.")
      quit()



def dropboxDump():
  directory_template = "C:/Users/Angelica Law Office/Dropbox/My Documents/Open Criminal State Cases/"
  downloads_directory = "C:/Users/Angelica Law Office/Downloads"
  try:
    if singular_global_name != ""
    mypath = directory_template + singular_global_name
    if not os.path.isdir(mypath):
    os.makedirs(mypath)
    access_toke = "U23lcsPMRG4AAAAAAAArIeNOXeSRkNQGdAWPiFw1EjCeJIHL_WeflohDf6_8Jt5g"
    list_of_files = glob.glob(downloads_directory+'*') # * means all if need specific format then *.csv
    latest_download = max(list_of_files, key=os.path.getctime)
    path_to_zip_file = downloads_directory + latest_download
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(mypath)
    zip_ref.close()
  except:
    print("Folder could not be created")
  

open_techshare()
dropboxDump()
print("Files are downloading...")
print("Do not close. This program will self-destruct when your files are done being distributed.")
time.sleep(60*60)
quit()


