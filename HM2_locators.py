from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# selectors for login page
#driver.get("https://www.amazon.com/")
#sleep(10)
#driver.find_element(By.ID, "nav-link-accountList").click()
# driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")
# driver.find_element(By.XPATH,"//input[@type='email']")
# driver.find_element(By.ID, "continue")
# driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
# driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
# driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']").click()
# driver.find_element(By.ID, "auth-fpp-link-bottom")
# driver.find_element(By.ID, "ap-other-signin-issues-link")

#login page test case
driver.get("https://www.target.com/")
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(1)
driver.find_element(By.XPATH, "//span[text()='Sign in' and @class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
sleep(1)
driver.find_element(By.ID, "login")
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
sleep(1)
driver.quit()