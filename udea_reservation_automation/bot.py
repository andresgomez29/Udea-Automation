from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


class Bot:
    def __init__(self):

        self.driver = webdriver.Chrome("storage/chromedriver")
        self.wait_driver=WebDriverWait(self.driver,timeout=20)

    def search_on_youtube(self):

        self.driver.get("https://www.youtube.com")
        self.wait_driver.until(EC.presence_of_all_elements_located(By.ID,"search"))
        self.wait_driver.find_element_by_id("search").click()

    def close(self):
        self.driver.close()
