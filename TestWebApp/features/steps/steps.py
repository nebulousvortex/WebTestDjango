from behave import given, when, then
from behave import *
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

@when('I navigate to login page')
def navigate_to_home_page(context):
    context.driver.get("http://127.0.0.1:8000/login/")

@then('I should see a non-empty title')
def check_title(context):
    wait = WebDriverWait(context.driver, 10)
    title_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    title = title_element.text
    assert title != ""

@then('I close the browser')
def close_browser(context):
    context.driver.quit()

@when(u'I navigate to the message page')
def navigate_to_admin_page(context):
    context.driver.get("http://127.0.0.1:8000/chat/")

@then(u'I should see a auth page')
def get_menu(context):
    wait = WebDriverWait(context.driver, 10)
    assert context.driver.current_url == 'http://127.0.0.1:8000/database/not_login_user/?next=/chat/'
    assert context.driver.find_elements(By.XPATH, '/html/body/div/main/div/h1')

@when(u'I navigate to the admin panel')
def navigate_to_admin_page(context):
    context.driver.get("http://127.0.0.1:8000/admin/")

@when(u'I enter my login {login} and password {passw}')
def login(context, login, passw):
    wait = WebDriverWait(context.driver, 10)
    login_field = wait.until(EC.visibility_of_element_located((By.ID, "id_username")))
    login_field.send_keys(login)

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "id_password")))
    password_field.send_keys(passw)

    submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-form"]/div[3]/input')))
    submit_button.click()

@when('I enter wrong login {wrong_login} or password {wrong_pass}')
def login(context, wrong_login, wrong_pass):
    wait = WebDriverWait(context.driver, 10)
    login_field = wait.until(EC.visibility_of_element_located((By.ID, "id_username")))
    login_field.send_keys(wrong_login)

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "id_password")))
    password_field.send_keys(wrong_pass)

    submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-form"]/div[3]/input')))
    submit_button.click()

@then(u'I should see the menu')
def get_menu(context):
    wait = WebDriverWait(context.driver, 10)
    main_content = wait.until(EC.visibility_of_element_located((By.ID, "content-main")))

    # Get all elements within the main content
    elements = main_content.find_elements(By.XPATH, '//*[@id="content-main"]//*')
    # Print the elements
    for element in elements:
        print(element.text)

    assert len(elements) != 0

@then(u'I cant see the menu')
def get_menu(context):
    wait = WebDriverWait(context.driver, 10)
    assert context.driver.current_url == 'http://127.0.0.1:8000/admin/login/?next=/admin/'
    assert context.driver.find_elements(By.CLASS_NAME, 'errornote')

@when(u'I navigate to news panel')
def navigate_to_admin_page(context):
    context.driver.get("http://127.0.0.1:8000/database/")

@then(u'I navigate to add news panel')
def navigate_to_admin_page(context):
    context.driver.get("http://127.0.0.1:8000/database/create_note")

@then(u'I should see the news')
def get_menu(context):
    expected_links = {
        'button1': 'http://127.0.0.1:8000/database/note/25/',
        'button2': 'http://127.0.0.1:8000/database/note/24/',
        'button3': 'http://127.0.0.1:8000/database/note/23/'
    }
    wait = WebDriverWait(context.driver, 10)
    buttons = context.driver.find_elements(By.CLASS_NAME, 'alert alert-warning')
    print(buttons)
    for button in buttons:
        button.click()
        WebDriverWait(context.driver, 10).until(EC.url_changes(context.driver.current_url))
        new_link = context.driver.current_url
        if new_link in expected_links:
            assert new_link == expected_links[new_link]
        else:
            print(f"Ожидаемая ссылка {new_link} не найдена в словаре")

@when(u'I enter admin login {login} and password {passw}')
def login(context, login, passw):
    wait = WebDriverWait(context.driver, 10)
    login_field = wait.until(EC.visibility_of_element_located((By.ID, "id_username")))
    login_field.send_keys(login)

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "id_password")))
    password_field.send_keys(passw)

    submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/form/button')))
    submit_button.click()

@then(u'I try to add new news {title} {anons} {full_text}')
def login(context, title, anons, full_text):
    wait = WebDriverWait(context.driver, 10)

    login_field = wait.until(EC.visibility_of_element_located((By.ID, "id_title")))
    login_field.send_keys(title)

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "id_anons")))
    password_field.send_keys(anons)

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "id_full_text")))
    password_field.send_keys(full_text)

    assert title != "" and anons !="" and full_text != ""

    # submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div/form/button')))
    # submit_button.click()