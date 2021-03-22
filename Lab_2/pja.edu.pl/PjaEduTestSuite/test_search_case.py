from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_search(search_keyword, expected_text, driver):
    try:
        url = "https://www.pja.edu.pl/"

        driver.maximize_window()
        driver.get(url)

        input_search = driver.find_element_by_id("mod-search-searchword")
        input_search.send_keys(search_keyword)

        button_search = driver.find_element_by_tag_name("input.button")
        button_search.click()

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


def test_find_hackathon_using_search(driver):
    expected_text = "hackathon"
    search_keyword = "hackathon"
    return test_search(search_keyword, expected_text, driver)


def test_find_library_info_using_search(driver):
    expected_text = "Procedura wypożyczenia książek:"
    search_keyword = "biblioteka"
    return test_search(search_keyword, expected_text, driver)


def test_find_japan_exchange_info_using_search(driver):
    expected_text = "Rekrutacja na wyjazdy do Japonii przebiega zgodnie z" \
                    " terminami wyznaczonymi corocznie przez uczelnie partnerskie" \
                    " i jest inna dla każdej z tych uczelni"
    search_keyword = "japonia"
    return test_search(search_keyword, expected_text, driver)
