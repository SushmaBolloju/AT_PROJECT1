'''
Project 1 : Selenium with python
___Testing login credentials___
Test Case ID: TC_Login_02
A Valid error message for invalid credentials is displayed
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class Orange:

   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(self.url)
       sleep(3)
       #Maximizing the window
       self.driver.maximize_window()

   def quit(self):
       #Quiting function
       self.driver.quit()

   def invalid_login(self):
       self.boot()
       sleep(3)
       username=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
       #Passing username value
       username.send_keys("Admin")
       password=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
       #Passing password value
       password.send_keys("India")
       login_button=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       #Clicking on the login button
       login_button.click()
       sleep(3)
       #assert alert
       alert_text_element = self.driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')
       error_message = alert_text_element.text
       assert error_message == 'Invalid credentials'
       self.quit()

#Passing url into the class Orange
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#Calling the function
obj.invalid_login()

