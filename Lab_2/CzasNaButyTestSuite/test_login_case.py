from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_login(email, password, expected_text, driver):
    try:
        url = "https://www.czasnabuty.pl/"

        driver.maximize_window()
        driver.get(url)

        # Sometimes popup can disturb test, so I wait for 4,5 sec to be sure popup is loaded and proceed to close it
        time.sleep(4.5)
        popup_close = driver.find_element_by_class_name("tln3_button")
        popup_close.click()

        button_login = driver.find_element_by_class_name("to_acc-4")
        button_login.click()

        input_email = driver.find_element_by_id("signin_login_input")
        input_email.send_keys(email)

        input_password = driver.find_element_by_id("signin_pass_input")
        input_password.send_keys(password)

        button_login_confirm = driver.find_element_by_class_name("signin_button")
        button_login_confirm.click()
    except Exception as e:
        print("Fields required for login not found: ", e)
        driver.quit()
        return False

    try:
        expected_text_found = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]"))
        )
        driver.quit()
    except Exception as e:
        print("Not found: ", expected_text, e)
        driver.quit()
        return False
    driver.quit()
    return True


def test_login_wrong_email(driver):
    email = "rtrtrtrtr"
    password = "abcdefghijk11"
    expected_text = "Podany login lub hasło nie jest poprawne."
    return test_login(email, password, expected_text, driver)


def test_login_wrong_password(driver):
    email = "abc@gmail.com"
    password = "abcdefghijk11"
    expected_text = "Podany login lub hasło nie jest poprawne."
    return test_login(email, password, expected_text, driver)


def test_login_no_email(driver):
    email = ""
    password = "abrakadabra"
    expected_text = "Podany login lub hasło nie jest poprawne."
    return test_login(email, password, expected_text, driver)


def test_login_no_password(driver):
    email = "pajtonCzad@onet.pl"
    password = ""
    expected_text = "Podany login lub hasło nie jest poprawne."
    return test_login(email, password, expected_text, driver)


def test_login_no_email_and_password(driver):
    email = ""
    password = ""
    expected_text = "Podany login lub hasło nie jest poprawne."
    return test_login(email, password, expected_text, driver)