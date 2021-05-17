from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_order_details(expected_text, driver):
    try:
        url = "https://sklep.rms.pl/"

        driver.maximize_window()
        driver.get(url)

        time.sleep(3)

        popup_window_close_btn = driver.find_element_by_xpath('//*[@id="popupfoot"]/a')
        popup_window_close_btn.click()

        headphones_product_category = driver.find_element_by_xpath("/html/body/div[2]/div/div/aside/nav/ul/li[4]/a/h2")
        headphones_product_category.click()

        hiend_headphones_product_subcategory = driver.find_element_by_xpath("/html/body/div[2]/div/div/article/div[2]/ul/li[1]/a[2]/h2")
        hiend_headphones_product_subcategory.click()

        are100_headphones_add_to_cart_btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/article/div[4]/ul/li[2]/div/div/div[3]/a[1]")
        are100_headphones_add_to_cart_btn.click()

        product_quantity_up_btn = driver.find_element_by_xpath("/html/body/div[2]/div/div/article/div/form/div[2]/table/tbody/tr/td[5]/div/div[2]/div[1]/a[1]")
        product_quantity_up_btn.click()

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


def test_adding_product_to_cart_with_quantity_change(driver):
    expected_text = "1198"

    return test_order_details(expected_text, driver)
