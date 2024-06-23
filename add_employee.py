'''
Project 1 : Selenium with python
___Add new employee in PIM module___
Test Case ID: TC_PIM_01
A User should be able to add a new employee in the PIM and should see a message for successful employee addition
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class Orange:

   def __init__(self, url):
      #initializing the url
       self.url = url
      #initializing the chrome webdriver
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(self.url)
       sleep(3)
       #Maximizing the window
       self.driver.maximize_window()

   def quit(self):
       # Quitting function
       self.driver.quit()

   def login(self):
       self.boot()
       sleep(3)
       username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
       #Passing username value
       username.send_keys("Admin")
       password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
       #Passing password value
       password.send_keys("admin123")
       login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       #Clicking on login button
       login_button.click()

   def add_employee(self):
       sleep(3)
       #Clicking on PIM module
       pim=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
       pim.click()
       sleep(3)
       #Adding employee details inside PIM module
       add_employee_btn=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
       add_employee_btn.click()
       sleep(3)
       #Passing firstname, lname, empid values into their respective textboxes
       fname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
       fname.send_keys("lilly")
       Lname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
       Lname.send_keys("Rosy")
       empid=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
       empid.send_keys("3456")
       save = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
       save.click()
       sleep(5)

       # #Enter some more personal details inside the same module
       personal_detail = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
       personal_detail.click()
       sleep(5)
       nationality = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')
       nationality.click()
       sleep(5)
       n1=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')
       n1.send_keys("Namibian")
       sleep(5)
       n2=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')
       n2.click()
       sleep(2)

       marital_status = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i')
       marital_status.click()
       sleep(5)
       m1 = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]')
       m1.send_keys("married")
       sleep(5)

       otherid = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]")
       otherid.send_keys("7864")
       sleep(2)
       licence = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]")
       licence.send_keys("7941")
       sleep(3)
       expiry_date = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
       expiry_date.send_keys("2024-04-05")
       sleep(5)
       birth_date =self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
       birth_date.send_keys("1992-10-12")
       sleep(2)
       gender = self.driver.find_element(By.XPATH,"//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']")
       gender.click()

       sleep(2)
       # saving the details
       self.driver.find_element(By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
       sleep(3)
       # closing the webpage
       self.quit()
       print("New employee is added successfully !!!")



#Passing URL into the class to perform all the above activities
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#login
obj.login()
#Add employee
obj.add_employee()