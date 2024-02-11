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

#locators for sign up page
driver.get("https://www.amazon.com/")
sleep(10)
driver.find_element(By.ID, "nav-link-accountList").click()
sleep(2)
driver.find_element(By.ID, "createAccountSubmit").click()
sleep(5)
driver.find_element(By.CSS_SELECTOR, 'i[class="a-icon a-icon-logo"]')
driver.find_element(By.CSS_SELECTOR, 'h1[class="a-spacing-small"]')
driver.find_element(By.ID, "ap_customer_name")
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "ap_password")
driver.find_element(By.ID, "ap_password_check")
driver.find_element(By.ID, "continue")
driver.find_element(By.CSS_SELECTOR, 'a[class="a-link-emphasis"]')



