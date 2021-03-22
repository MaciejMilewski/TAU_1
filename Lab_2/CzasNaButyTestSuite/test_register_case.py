from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_register(name, surname, address, postal_code, city, email,
                  telephone_number, password, password_confirmation, shop_regulations,
                  expected_text, driver):
    try:
        url = "https://www.czasnabuty.pl/"

        driver.maximize_window()
        driver.get(url)

        # Sometimes popup can disturb test, so I wait for 4,5 sec to be sure popup is loaded and proceed to close it
        time.sleep(4.5)
        popup_close = driver.find_element_by_class_name("tln3_button")
        popup_close.click()

        button_register = driver.find_element_by_class_name("to_acc-3")
        button_register.click()

        input_name = driver.find_element_by_id("client_firstname_copy")
        input_name.send_keys(name)

        surname_input = driver.find_element_by_id("client_lastname_copy")
        surname_input.send_keys(surname)

        address_input = driver.find_element_by_id("client_street")
        address_input.send_keys(address)

        postal_code_input = driver.find_element_by_id("client_zipcode")
        postal_code_input.send_keys(postal_code)

        city_input = driver.find_element_by_id("client_city")
        city_input.send_keys(city)

        email_input = driver.find_element_by_id("client_email")
        email_input.send_keys(email)

        telephone_number_input = driver.find_element_by_id("client_phone")
        telephone_number_input.send_keys(telephone_number)

        password_input = driver.find_element_by_id("client_password")
        password_input.send_keys(password)

        password_confirmation_input = driver.find_element_by_id("repeat_password")
        password_confirmation_input.send_keys(password_confirmation)

        shop_regulations_checkbox = driver.find_element_by_id("terms_agree")
        if shop_regulations is True:
            shop_regulations_checkbox.click()

        privacy_regulations_input = driver.find_element_by_id("terms_agree_2")
        privacy_regulations_input.click()

        button_register_confirm = driver.find_element_by_id("submit_register")
        button_register_confirm.click()
    except Exception as e:
        print("Fields required for register not found: ", e)
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


def test_register_no_shop_regulations_checkbox(driver):
    name = "Matt"
    surname = "TestAndGo"
    address = "Betonowa 13"
    postal_code = "10-100"
    city = "Szczecin"
    email = "fadiotrea@blyat.com"
    telephone_number = "111222333"
    password = "abcdefg1A"
    password_confirmation = "abcdefg1A"
    shop_regulations = False
    expected_text = "Wypełnij wskazane pola."

    return test_register(name, surname, address, postal_code, city, email,
                         telephone_number, password, password_confirmation, shop_regulations,
                         expected_text, driver)


def test_register_no_name(driver):
    name = ""
    surname = "TestAndGo"
    address = "Betonowa 13"
    postal_code = "10-100"
    city = "Szczecin"
    email = "apmlbbbbpp@blyat.com"
    telephone_number = "111222333"
    password = "abcdefg1A"
    password_confirmation = "abcdefg1A"
    shop_regulations = True
    expected_text = "Wypełnij wskazane pola."

    return test_register(name, surname, address, postal_code, city, email,
                         telephone_number, password, password_confirmation, shop_regulations,
                         expected_text, driver)


def test_register_no_surname(driver):
    name = "Matt"
    surname = ""
    address = "Betonowa 13"
    postal_code = "10-100"
    city = "Szczecin"
    email = "aakratPLa@bvvlyat.com"
    telephone_number = "111222333"
    password = "abcdefg1A"
    password_confirmation = "abcdefg1A"
    shop_regulations = True
    expected_text = "Wypełnij wskazane pola."

    return test_register(name, surname, address, postal_code, city, email,
                         telephone_number, password, password_confirmation, shop_regulations,
                         expected_text, driver)


def test_register_blank_form(driver):
    name = ""
    surname = ""
    address = ""
    postal_code = ""
    city = ""
    email = ""
    telephone_number = ""
    password = ""
    password_confirmation = ""
    shop_regulations = False
    expected_text = "Wypełnij wskazane pola."

    return test_register(name, surname, address, postal_code, city, email,
                         telephone_number, password, password_confirmation, shop_regulations,
                         expected_text, driver)


def test_register_wrong_email(driver):
    name = "Maaaaatt"
    surname = "TestAndGo"
    address = "Betonowa 13"
    postal_code = "10-100"
    city = "Szczecin"
    email = "bardzo_niepoprawny_email"
    telephone_number = "111222333"
    password = "abcdefg1A"
    password_confirmation = "abcdefg1A"
    shop_regulations = True
    expected_text = "Wypełnij wskazane pola."

    return test_register(name, surname, address, postal_code, city, email,
                         telephone_number, password, password_confirmation, shop_regulations,
                         expected_text, driver)


def test_register_wrong_postal_code(driver):
    name = "Matxt"
    surname = "TestAndGo"
    address = "Betonowa 13"
    postal_code = "1111111111"
    city = "Szczecin"
    email = "uwmekuw1k@blbvyat.com"
    telephone_number = "111222333"
    password = "abcdefg1A"
    password_confirmation = "abcdefg1A"
    shop_regulations = True
    expected_text = "Wypełnij wskazane pola."

    return test_register(name, surname, address, postal_code, city, email,
                         telephone_number, password, password_confirmation, shop_regulations,
                         expected_text, driver)


def test_register_wrong_address(driver):
    name = "Matt"
    surname = "TestAndGo"
    address = "xxx"
    postal_code = "80-100"
    city = "Szczecin"
    email = "iaqpasou@blyat.com"
    telephone_number = "111222333"
    password = "abcdefg1A"
    password_confirmation = "abcdefg1A"
    shop_regulations = True
    expected_text = "Wypełnij wskazane pola."

    return test_register(name, surname, address, postal_code, city, email,
                         telephone_number, password, password_confirmation, shop_regulations,
                         expected_text, driver)


def test_register_no_password_confirmation(driver):
    name = "Matt"
    surname = "TestAndGo"
    address = "Betonowa 13"
    postal_code = "80-100"
    city = "Szczecin"
    email = "alantIMPTvbssAaa@blyeat.com"
    telephone_number = "111222333"
    password = "abcdefg1A"
    password_confirmation = ""
    shop_regulations = True
    expected_text = "Wypełnij wskazane pola."

    return test_register(name, surname, address, postal_code, city, email,
                         telephone_number, password, password_confirmation, shop_regulations,
                         expected_text, driver)
