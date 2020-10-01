""" 
Cookie Clicker bot
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CookieBot():
    
    def __init__(self):
        
        #Aller sur la page de Cookie Clicker
        self.path = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.path)
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
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
            except:
                pass
            
    def save_game_link(self):
        #Cliquer sur le bouton option
        options_btn = self.driver.find_element_by_id("prefsButton")
        options_btn.click()
        
        #Cliquer sur le bouton Export save
        menu = self.driver.find_element_by_id('menu')
        a = menu.find_elements_by_tag_name('a')
        a[1].click()
        
        #Copier coller le lien dans la variable link du bot
        link = self.driver.find_element_by_id("textareaPrompt").text
        self.link = link
        
        #Quitter le menu option
        self.driver.find_element_by_id("textareaPrompt").send_keys(Keys.RETURN)
        menu.find_elements_by_tag_name('div')[0].click()
        
    
    def load_game_link(self):
         #Cliquer sur le bouton option
        options_btn = self.driver.find_element_by_id("prefsButton")
        options_btn.click()
        
        #Cliquer sur le bouton Export save
        menu = self.driver.find_element_by_id('menu')
        a = menu.find_elements_by_tag_name('a')
        a[2].click()
        
        #On écrit le link du bot
        white_window = self.driver.find_element_by_id('textareaPrompt')
        white_window.send_keys(self.link)
        white_window.send_keys(Keys.RETURN)
        
        #On ferme la fenetre d'options
        menu.find_elements_by_tag_name('div')[0].click()
            
    def quit(self):
        self.driver.quit()
        
    def lets_get_cookies(self, number_loops = 100, number_clicks = 200):
        
        for i in range(number_loops):
            self.buy_store()
            for j in range(number_clicks):
                self.click()
            self.buy_upgrade()
            

cookie = CookieBot()

for i in range(9): #1h30
    print(i)
    cookie.lets_get_cookies(5, int(200*(1.5**i)))

cookie.save_game_link()
link = cookie.link

