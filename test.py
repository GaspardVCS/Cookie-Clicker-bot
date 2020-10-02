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
    
    def buy_store(self):
        for i in range(5, -1, -1): # On s'arrete aux banques, en tout 17 buildings différents
            try:
                item = self.driver.find_element_by_id("product" + str(i))
                
                cookie_count = self.driver.find_element_by_id('cookies').text.split(' ')[0]
                cookie_count = int(''.join(cookie_count.split(',')))
                
                
                product_price = self.driver.find_element_by_id('productPrice' + str(i)).text
                product_price = int(''.join(product_price.split(',')))
                
                can_buy = cookie_count >= product_price
                while can_buy:
                    item.click()
                    cookie_count = self.driver.find_element_by_id('cookies').text.split(' ')[0]
                    cookie_count = int(''.join(cookie_count.split(',')))

                    product_price = self.driver.find_element_by_id('productPrice' + str(i)).text
                    product_price = int(''.join(product_price.split(',')))

                    can_buy = cookie_count >= product_price

            except:
                pass
            
    def buy_upgrade(self):
            try:
                item = self.driver.find_element_by_id("upgrade0")
                item.click()