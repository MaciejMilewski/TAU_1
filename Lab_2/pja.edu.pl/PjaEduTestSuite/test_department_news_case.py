from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_department(department_name, expected_text, driver):
    try:
        url = "https://www.pja.edu.pl/"

        driver.maximize_window()
        driver.get(url)

        if department_name == "informatyka":
            department_link = driver.find_element_by_class_name("infcolor")
            department_link.click()
        elif department_name == "architektura wnętrz":
            department_link = driver.find_element_by_class_name("awcolor")
            department_link.click()
        elif department_name == "sztuka nowych mediów":
            department_link = driver.find_element_by_class_name("snmcolor")
            department_link.click()

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


def test_check_computer_science_article(driver):
    expected_text = "W trakcie zajęć w laboratoriach komputerowych każdy student ma do dyspozycji oddzielny komputer."
    department_name = "informatyka"
    return test_department(department_name, expected_text, driver)


def test_check_interior_design_article(driver):
    expected_text = "Studia z Architektury Wnętrz na PJATK to połączenie sztuki plastycznej i architektonicznej"
    department_name = "architektura wnętrz"
    return test_department(department_name, expected_text, driver)


def test_check_new_media_arts_article(driver):
    expected_text = "Wydział Sztuki Nowych Mediów PJATK"
    department_name = "sztuka nowych mediów"
    return test_department(department_name, expected_text, driver)
