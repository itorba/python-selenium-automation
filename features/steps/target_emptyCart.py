from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on the cart icon')
def cart_click(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()


@then('Verify empty cart message shown')
def verify_empty_cart(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert actual_result == expected_result, f'Expected {expected_result} bot got {actual_result}'