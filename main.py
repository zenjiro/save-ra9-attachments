import os
import time
from dotenv import load_dotenv

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
GROUP_NAME = os.getenv("GROUP_NAME")
DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY")

if __name__ == "__main__":
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.get("https://ra9.jp/user")
        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.NAME, "login").click()
        driver.find_element(By.LINK_TEXT, GROUP_NAME).click()
        driver.find_element(By.LINK_TEXT, "メール").click()
        for i in range(len(driver.find_elements(By.CLASS_NAME, "fa-paperclip"))):
            driver.find_element(By.TAG_NAME, "body").send_keys(" ")
            element = driver.find_elements(By.CLASS_NAME, "fa-paperclip")[i]
            if element.is_displayed():
                element.click()
                filename = driver.find_element(By.CLASS_NAME, "val-name").text
                print(filename)
                if not os.path.exists(DOWNLOAD_DIRECTORY + filename):
                    if driver.find_elements(By.LINK_TEXT, "開く"):
                        driver.find_element(By.TAG_NAME, "body").send_keys("  ")
                        time.sleep(1)
                        WebDriverWait(driver, 20).until(
                            expected_conditions.element_to_be_clickable(
                                (By.LINK_TEXT, "開く")
                            )
                        ).click()
                        time.sleep(1)
                driver.back()
    finally:
        driver.quit()