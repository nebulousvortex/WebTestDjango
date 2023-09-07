from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@given('I open the browser')
def open_browser(context):
    context.driver = webdriver.Chrome()

@when('I navigate to the home page')
def navigate_to_home_page(context):
    context.driver.get("http://127.0.0.1:8000/")

@then('I should see a non-empty title')
def check_title(context):
    wait = WebDriverWait(context.driver, 10)
    title_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    title = title_element.text
    assert title != ""

@then('I close the browser')
def close_browser(context):
    context.driver.quit()
