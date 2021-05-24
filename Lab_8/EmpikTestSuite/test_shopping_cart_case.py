from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_product_order_details(expected_text, driver):
    try:
        url = "https://www.empik.com/"

        driver.maximize_window()
        driver.get(url)

        search_bar_input = driver.find_element_by_xpath('//*[@id="bq"]')
        search_bar_input.send_keys("ekstremista")

        time.sleep(1.5)

        search_btn = driver.find_element_by_xpath('//*[@id="searchSet"]/button')
        search_btn.click()

        time.sleep(1.5)

        book_card = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/a')
        book_card.click()

        time.sleep(1.5)

        add_to_cart_btn = driver.find_element_by_xpath('/html/body/main/div[1]/div[3]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[5]/div/button')
        add_to_cart_btn.click()

        time.sleep(1.5)

        go_to_cart_btn = driver.find_element_by_xpath('//html/body/div[5]/div/div[2]/div[2]/div[1]/button')
        go_to_cart_btn.click()

        time.sleep(1.5)

    except Exception as e:
        print("Fields required for shopping cart case not found: ", e)
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


def test_order_details(driver):
    expected_text = "Ekstremista"

    return test_product_order_details(expected_text, driver)