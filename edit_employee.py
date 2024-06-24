'''
Project 1 : Selenium with python
___Edit PIM module___
Test Case ID: TC_PIM_02

'''
#importing all necessary in built /added functions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Orange:
    def __init__(self, url):
        #Initializing the url
        self.url = url
        #Initializing the chrome webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)

        sleep(3)
        #Maximizing the window
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def login(self):
        self.boot()
        sleep(3)
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
                                            
        # Passing username value
        username.send_keys("Admin")
        
        password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
                                            
        # Passing password value
        password.send_keys("admin123")
        login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
                                                
        # Clicking on login button
        login_button.click()

    def edit_employee(self):
        sleep(3)
        #Clicking on PIM module
        pim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pim.click()
        sleep(3)
        #Searching previously added employee (using add_employee.py)
        emp_name=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        emp_name.send_keys("lilly Rosy")
        sleep(2)
        search=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        search.click()
        sleep(3)
       #Editing the searched and found employee details
        edit=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]')
        sleep(3)
        edit.click()
        sleep(5)
        other_id=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
        other_id.send_keys("123")
        sleep(2)
        #After editing it, saving the page
        save_button = self.driver.find_element(By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']")
        save_button.click()
        sleep(2)
        self.quit()

#Passing URL link into the class to perform all the above activities
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#Login
obj.login()
#Editing employee
obj.edit_employee()
