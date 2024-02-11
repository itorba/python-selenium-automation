from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then


@when('Click on the sign in')
def sign_in_click(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Account, sign in"]').click()


@when('Click on the sign in from nav menu')
def sign_in_from_nav_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]').click()


@then('Verify sign in form shown')
def verify_sign_in_shown(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, '//span[text()="Sign into your Target account"]').text
    assert actual_result == expected_result, f'Expected {expected_result} bot got {actual_result}'
