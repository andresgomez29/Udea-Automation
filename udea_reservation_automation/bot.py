from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC


class Bot:
    def __init__(self):

        self.driver = webdriver.Chrome("storage/chromedriver") #start with chromedriver
        self.wait_driver=WebDriverWait(self.driver,timeout=20) #wait for open the browser

    def search_on_youtube(self,input):

        self.driver.get("https://www.youtube.com") #open youtube
        #self.wait_driver.until(EC.presence_of_all_elements_located(By.ID())) #
        self.searchBox=self.driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input") #searchbox input
        self.searchBox.send_keys(input)

        self.searchButton=self.driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button") #search button
        self.searchButton.click()

    def go_to_video(self):
        self.box1=self.driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a")
        self.box1.click()

    def close(self):
        self.driver.close()
