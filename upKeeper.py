from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep, time
from datetime import datetime
import os
from dotenv import load_dotenv

from emailHandler import sendInfo

load_dotenv()


def logout(chrome: webdriver):
    print(f"{datetime.now()} -   Logging Out...")
    chrome.find_element(
        By.CSS_SELECTOR, "span[style='display: table-cell; vertical-align: middle; white-space: nowrap;']"
    ).click()
    chrome.find_element(
        By.CSS_SELECTOR, "a[href='/auth/logout?redirect=%2F']"
    ).click()
    print(f"{datetime.now()} -   Logged Out!")

def login(chrome: webdriver):
    print(f"{datetime.now()} -   Logging In...")
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
    print(f"{datetime.now()} -   Logged In!")

def renewServer(chrome: webdriver):
    print(f"{datetime.now()} -   Renewing Server...")
    WebDriverWait(chrome, 20).until(
        EC.visibility_of_element_located((
            By.ID, os.environ.get("BUTTON_ID")
        ))
    ).click()
    chrome.switch_to.window(chrome.window_handles[1])
    sleep(7 * 60)
    chrome.close()
    chrome.switch_to.window(chrome.window_handles[0])
    sleep(10)
    chrome.refresh()
    sleep(10)

    WebDriverWait(chrome, 20).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, "button[data-mkt-id='console_main_button_viewContainerMore']"
        ))
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
    details = []
    for cell in portForwardingCells:
        if(cell.text):
            details.append(cell.text)

    print(f"{datetime.now()} -   Server Renewed!")
    return details



startTime = time()
waitPeriodInMinutes = 4 * 60

while(True):
    chrome = webdriver.Chrome("./chromedriver.exe")
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    
    chrome.get(os.environ.get("STARTING_URL"))

    login(chrome)
    sleep(10)

    info = renewServer(chrome)
    sleep(10)
    sendInfo(info[2], info[3], info[4])

    logout(chrome)
    sleep(10)
    
    chrome.close()
    print("==================================================")
    sleep( (waitPeriodInMinutes * 60.0) - ((time() - startTime) % (waitPeriodInMinutes * 60.0)) )