import os
import time
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

load_dotenv()

SELENIUM_PROFILE_DIRECTORY = os.getenv("SELENIUM_PROFILE_DIRECTORY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY")

options = Options()
options.add_argument(
    f"--user-data-dir={SELENIUM_PROFILE_DIRECTORY}"
)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get(
    f"https://ra9plus.jp/cn/inbox?organizationId={ORGANIZATION_ID}"
)
for element in driver.find_elements(
    By.CSS_SELECTOR, "span.css-1jxf684.r-1wdu9aa.r-vw2c0b"
):
    element.click()
    time.sleep(1)
    for element2 in driver.find_elements(
        By.CSS_SELECTOR, "div.css-146c3p1.r-1wdu9aa.r-a023e6.r-1ow6zhx"
    ):
        filename = element2.text
        print(filename)
        if not os.path.exists(DOWNLOAD_DIRECTORY + filename):
            print("ダウンロードします。")
            element2.click()
            time.sleep(1)
    driver.back()
    time.sleep(1)
