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

#by IDs
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

#by XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

#by XPATH, multiple attributes
driver.find_element(By.XPATH, "//input[@name='field-keywords' and @placeholder='Search Amazon']")

#by XPATH, using text
driver.find_element(By.XPATH, "//a[text()='New Releases']")
driver.find_element(By.XPATH, "//a[text()='New Releases' and @class='nav-a']")

#by XPATH, partial link (contains)
driver.find_element(By.XPATH, "//a[contains(@href,'nav_cs_bestsellers')]")

