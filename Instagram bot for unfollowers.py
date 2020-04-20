#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from time import sleep

class Instabot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path= r'C:\Users\mistr\Downloads\chromedriver_win32 (1)/chromedriver.exe')
        self.username = username
        self.driver.get("https://instagram.com")
        
        sleep(0.5) #waits for 2 sec before executing it, basically you need to wait before the page is loaded
        
        self.driver.find_element_by_xpath("//input[@name = \"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name = \"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type= \"submit\"]").click()
        
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(1)
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        
        following = self.get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        
        followers = self.get_names()
        
        not_following = [user for user in following if user not in followers]
        print(not_following)

    def get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0,1
        
        while last_ht != ht:
            last_ht = ht
            sleep(1)
        
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        
        return names

username = str(input("Enter your user name: "))
password = str(input ("Enter your password: "))
myfirstbot = Instabot(username, password)
myfirstbot.get_unfollowers()


# In[ ]:





# In[ ]:





# In[ ]:




