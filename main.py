import os
import time

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == "__main__":
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.get("https://ra9.jp/user")
        driver.find_element(By.NAME, "email").send_keys("要修正：メールアドレス")
        driver.find_element(By.NAME, "password").send_keys("要修正：パスワード")
        driver.find_element(By.NAME, "login").click()
        driver.find_element(By.LINK_TEXT, "要修正：団体名").click()
        driver.find_element(By.LINK_TEXT, "メール").click()
        for i in range(len(driver.find_elements(By.CLASS_NAME, "fa-paperclip"))):
            driver.find_element(By.TAG_NAME, "body").send_keys(" ")
            element = driver.find_elements(By.CLASS_NAME, "fa-paperclip")[i]
            if element.is_displayed():
                element.click()
                print(driver.find_element(By.CLASS_NAME, "val-name").text)
                if not os.path.exists(
                    "C:/Users/要修正：Windowsのユーザー名/Downloads/"
                    + driver.find_element(By.CLASS_NAME, "val-name").text
                ):
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
