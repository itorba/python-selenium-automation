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

# open the url
driver.get('https://www.amazon.com/')

#by IDs (CSS_Selector)
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

#by CLASS
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-us')

#by CSS Attributes
driver.find_element(By.CSS_SELECTOR, 'a[href*="ref=ap_signin_notification_condition_of_use?')
driver.find_element(By.CSS_SELECTOR, 'a[data-csa-c-func-deps="aui-da-a-expander-toggle"][role="button"]')

sleep(10)