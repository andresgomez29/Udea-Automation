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

class Bot_Meet_Room():
    def __init__(self):
        self.driver = webdriver.Chrome("storage/chromedriver")
        self.wait_driver=WebDriverWait(self.driver,timeout=20)  
          
    def enter_page(self):
        self.driver.get("https://biblioteca.udea.edu.co/turnosudea/#/")



    def Log_in(self,username,password):

        self.UsenameBox=self.driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div/div/div[1]/div/div/div/form/div[3]/input")
        self.UsenameBox.send_keys(username)

        self.passwordBox=self.driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div/div/div[1]/div/div/div/form/div[4]/input")
        self.passwordBox.send_keys(password)

        self.log_in_Button=self.driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div/div/div[1]/div/div/div/form/div[5]/div/button")
        self.log_in_Button.click()

    def library_interfaz(self):
        self.libraryBox=self.driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div[2]/div[1]/div/div/a")
        self.libraryBox.click()
    
    def meet_rooms_interfaz(self):
        self.meet_roomsBox=self.driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div[4]/div[3]/div/div/a")
        self.meet_roomsBox.click()
        

    def room1(self):
        self.room1Box=self.driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div[5]/div[1]/div/a")
        self.room1Box.click()



    def ReserveRoom(self):
        self.horariosBox=self.driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div[4]/div[2]/div[2]/div/div/div[4]")
        self.horariosBox.click()

        self.reserveButton=self.driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div[4]/div[2]/div[3]/div/button")
        self.reserveButton.click()
        





    def close(self):
        self.driver.close()


        

