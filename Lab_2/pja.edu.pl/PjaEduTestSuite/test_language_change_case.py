from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_language_change(language, expected_text, driver):
    try:
        url = "https://www.pja.edu.pl/"

        driver.maximize_window()
        driver.get(url)

        if language is "PL":
            language_change_link = driver.find_element_by_link_text("EN")
            language_change_link.click()

        language_change_link = driver.find_element_by_link_text(language)
        language_change_link.click()
    except Exception as e:
        print("Fields required for language change not found: ", e)
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


def test_en_language_change(driver):
    expected_text = "Warsaw"
    language = "EN"
    return test_language_change(language, expected_text, driver)


def test_ru_language_change(driver):
    expected_text = "Бытом"
    language = "RU"
    return test_language_change(language, expected_text, driver)


def test_pl_language_change(driver):
    expected_text = "Warszawa"
    language = "PL"
    return test_language_change(language, expected_text, driver)