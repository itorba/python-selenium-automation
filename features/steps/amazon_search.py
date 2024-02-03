from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search_word)
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert actual_result == expected_result, f'Expected {expected_result} bot got {actual_result}'
