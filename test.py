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
        options_btn.click()
        menu = self.driver.find_element_by_id("menu")
        a = menu.find_elements_by_tag_name('a')
        a[16].click() #On clique sur Short Numbers ON
        menu.find_elements_by_tag_name('div')[0].click() #On ferme la fenetre d'option
        
        
        # Contiendra le lien de la partie une fois enregistrée
        self.link = ''
        
        
    def click(self):
        Cookie = self.driver.find_element_by_id("bigCookie")
        Cookie.click()
    
    