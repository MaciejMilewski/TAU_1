from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color
import time


def test_newsletter(email, newsletter_terms, expected_text, driver):
    try:
        url = "https://www.czasnabuty.pl/"

        driver.maximize_window()
        driver.get(url)

        # wait for popup to appear
        time.sleep(3.5)
        input_email = driver.find_element_by_id("tln3_input")
        input_email.send_keys(email)

        newsletter_terms_checkbox = driver.find_element_by_id("agree")
        if newsletter_terms is True:
            newsletter_terms_checkbox.click()

        button_newsletter_save = driver.find_element_by_id("tln3_submit")
        button_newsletter_save.click()

    except Exception as e:
        print("Fields required for newsletter not found: ", e)
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


def test_newsletter_wrong_email(driver):
    email = "aaa"
    newsletter_terms = True
    expected_text = "Wystąpił błąd. Spróbuj ponownie później"

    return test_newsletter(email, newsletter_terms, expected_text, driver)


def test_newsletter_no_terms_checkbox(driver):
    email = "aaa@wp.pl"
    newsletter_terms = False
    url = "https://www.czasnabuty.pl/"

    driver.maximize_window()
    driver.get(url)

    # wait for popup to appear
    time.sleep(3.5)
    input_email = driver.find_element_by_id("tln3_input")
    input_email.send_keys(email)

    newsletter_terms_checkbox = driver.find_element_by_id("agree")
    if newsletter_terms is True:
        newsletter_terms_checkbox.click()

    button_newsletter_save = driver.find_element_by_id("tln3_submit")
    button_newsletter_save.click()

    time.sleep(3.5)
    warning_span_color = driver.find_element_by_class_name("zaznaczenie").value_of_css_property('color')
    warning_span_color_in_hex = Color.from_string(warning_span_color).hex

    result = False
    if warning_span_color_in_hex == "#ff0000":
        result = True

    driver.quit()

    return result


def test_newsletter_no_email(driver):
    email = ""
    newsletter_terms = True
    expected_text = "Wystąpił błąd. Spróbuj ponownie później"

    return test_newsletter(email, newsletter_terms, expected_text, driver)

