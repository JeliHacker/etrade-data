from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller as chromedriver
chromedriver.install()


class EtradeBot:

    def __init__(self):
        options = Options()
        options.add_argument("start-maximized")

        # Chrome is controlled by automated test software
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        s = Service('/Users/jeligooch/Desktop/chromedriver')

        driver = webdriver.Chrome(service=s, options=options)

        # Selenium Stealth settings
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        self.driver = webdriver.Chrome()
        self.driver.get("https://etrade.com")
        sleep(1)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Log on')]")\
            .click()
        sleep(20)

        # click Transactions
        # self.driver.find_element(By.XPATH, "//a[@href=\"https://us.etrade.com/e/t/user/logout\"]")\
        self.driver.find_element(By.XPATH, "//*[@id='menu']/li[1]/ul/li[6]/a")\
            .click()
        sleep(10)


EtradeBot()
