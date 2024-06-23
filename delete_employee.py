'''
Project 1 : Selenium with python
___Delete PIM module___
Test Case ID: TC_PIM_03

'''
#Importing all the necessary in built / added functions
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
        username = self.driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        # Passing username value
        username.send_keys("Admin")
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        # Passing password value
        password.send_keys("admin123")
        login_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        # Clicking on login button
        login_button.click()

    def delete_employee(self):
        sleep(3)
        #Clicking on PIM module
        pim = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pim.click()
        sleep(3)
        #Passing emp name value to search it (previsously added using add_employee.py)
        emp_name=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        emp_name.send_keys("lilly Rosy")
        sleep(5)
        search=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        search.click()
        sleep(5)
        #After i search and found the required value, deleting it
        delete = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[9]/div[1]/button[1]/i[1]")
        delete.click()
        sleep(5)
        delete_alert = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
        delete_alert.click()
        sleep(3)
        print("Deleted successfully !!!")
        self.quit()

#Passing URL into the class Orange
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#login
obj.login()
#Deleting an employee
obj.delete_employee()