from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CookieBot():
    
    def __init__(self):
        
        #Aller sur la page de Cookie Clicker
        self.driver = webdriver.Chrome(self.path)
        time.sleep(5)
        
        #Choisir l'option de voir tous les chiffres
        options_btn = self.driver.find_element_by_id("prefsButton")
    
    