from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()


def logout(chrome: webdriver):
    print("-   Logging Out...")
    chrome.find_element(
        By.CSS_SELECTOR, "span[style='display: table-cell; vertical-align: middle; white-space: nowrap;']"
    ).click()
    chrome.find_element(
        By.CSS_SELECTOR, "a[href='/auth/logout?redirect=%2F']"
    ).click()
    print("-   Logged Out!")

def login(chrome: webdriver):
    print("-   Logging In...")
    email = chrome.find_element(
        By.ID, "emailInput"
    )
    password = chrome.find_element(
        By.ID, "passwordInput"
    )
    email.send_keys(os.environ.get("EMAIL"))
    password.send_keys(os.environ.get("PASSWORD"))
    sleep(10)
    chrome.find_element(
        By.CSS_SELECTOR, "span[class='_1lMForvxbNw3au4JG5jdB9']"
    ).click()
    print("-   Logged In!")

def renewServer(chrome: webdriver):
    print("-   Renewing Server...")    
    chrome.find_element(
        By.CSS_SELECTOR, "a[data-mkt-id='console_main_button_runContainer']"
    ).click()
    chrome.switch_to.window(chrome.window_handles[1])
    sleep(7 * 60)
    chrome.close()
    chrome.switch_to.window(chrome.window_handles[0])
    sleep(10)
    chrome.refresh()
    sleep(10)

    chrome.find_element(
        By.CSS_SELECTOR, "button[data-mkt-id='console_main_button_viewContainerMore']"
    ).click()
    chrome.find_element(
        By.CSS_SELECTOR, f"a[href='{os.environ.get('SETTING_HREF')}']"
    ).click()
    sleep(10)

    portForwardingCells = WebDriverWait(chrome, 20).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, "table[class='PortForwardingCard_PortForwardingCard__CardBody__Table__TzFcw table']"
        ))
    ).find_elements(
        By.TAG_NAME, "td"
    )
    for cell in portForwardingCells:
        if(cell.text):
            print(f"    - {cell.text}")
    print("-   Server Renewed!")



chrome = webdriver.Chrome("./chromedriver.exe")
chrome.maximize_window()
chrome.implicitly_wait(5)
chrome.get(os.environ.get("STARTING_URL"))
print("Start Renewing!")
login(chrome)
sleep(10)
renewServer(chrome)
sleep(10)
logout(chrome)
sleep(10)
chrome.close()