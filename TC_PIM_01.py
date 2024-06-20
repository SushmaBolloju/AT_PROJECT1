import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
login = driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
#Adding personal details of an employee.
# click on PIM
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(5)
#Click on +Add
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
time.sleep(5)
first_name=driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
first_name.send_keys("lilly")
last_name = driver.find_element(By.XPATH,"//input[@placeholder='Last Name']")
last_name.send_keys("rosy")
empid = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
empid.send_keys("3456")
save = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
time.sleep(5)
# //////Adding personal details of an employee/////
wait = WebDriverWait(driver, 30)
dropdown_menu =wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div')))
dropdown_menu.click()
time.sleep(5)
option_to_select = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]' )))
option_to_select.send_keys("Namibian")
id1 = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("7864")
licence = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]").send_keys("7941")
expiry_date = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("2024-04-05")
birth_date = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("1992-10-12")
gender = driver.find_element(By.XPATH,"//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']").click()
time.sleep(2)
dropdown_menu_m =wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div')))
dropdown_menu_m.click()
option_to_select_m = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]' ))).send_keys("Single")
driver.find_element(By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
time.sleep(3)
# closing the webpage
driver.quit()
