        menu = self.driver.find_element_by_id("menu")
        a = menu.find_elements_by_tag_name('a')
        a[16].click() #On clique sur Short Numbers ON
        menu.find_elements_by_tag_name('div')[0].click() #On ferme la fenetre d'option
        
        
        # Contiendra le lien de la partie une fois enregistree
        self.link = ''
        
        
    def click(self):
        Cookie = self.driver.find_element_by_id("bigCookie")
        Cookie.click()
    
    