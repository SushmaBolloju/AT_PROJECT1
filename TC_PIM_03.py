import time
from selenium.webdriver.common.by import By
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
# click on PIM
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(5)
driver.execute_script("window.scrollTo(500, 500);")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[4]//div[1]//div[9]//div[1]//button[1]//i[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
time.sleep(3)
driver.quit()