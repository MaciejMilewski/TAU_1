from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s', filename='rms.log', encoding='utf-8', level=logging.DEBUG)


def test_order_details(expected_text, driver):
    try:
        url = "https://sklep.rms.pl/"
        logging.debug("Maximizing chrome driver window")
        driver.maximize_window()

        logging.info("Waiting for https://sklep.rms.pl/ - start")
        try:
            logging.debug("Waiting for https://sklep.rms.pl/ - try")
            driver.get(url)
        except:
            logging.error("Waiting for https://sklep.rms.pl/ - failed")
            return
        logging.info("Waiting for https://sklep.rms.pl/ - end")
        time.sleep(3)

        logging.info("Close popup window - start")
        try:
            logging.debug("Getting popup window close button")
            popup_window_close_btn = driver.find_element_by_xpath('//*[@id="popupfoot"]/a')
            logging.debug("Click popup window close button")
            popup_window_close_btn.click()
        except:
            logging.error("Close popup window - failed")
            return
        logging.info("Close popup window - end")

        logging.info("Headphone product category selection - start")
        try:
            logging.debug("Getting headphone category button")
            headphones_product_category = driver.find_element_by_xpath("/html/body/div[2]/div/div/aside/nav/ul/li[4]/a/h2")
            logging.debug("Click headphone category button")
            headphones_product_category.click()
        except:
            logging.error("Headphone product category selection - failed")
            return
        logging.info("Headphone product category selection - start")

        logging.info("HI-END headphone product subcategory selection - start")
        try:
            logging.debug("Getting HI-END headphone product subcategory button")
            hiend_headphones_product_subcategory = driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/article/div[2]/ul/li[1]/a[2]/h2")
            logging.debug("Click HI-END headphone product subcategory button")
            hiend_headphones_product_subcategory.click()
        except:
            logging.error("HI-END headphone product subcategory selection - failed")
            return
        logging.info("HI-END headphone product subcategory selection - end")

        logging.info("Add are100 headphones to cart - start")
        try:
            logging.debug("Getting add are100 headphones to cart button")
            are100_headphones_add_to_cart_btn = driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/article/div[4]/ul/li[2]/div/div/div[3]/a[1]")
            logging.debug("Click add are100 headphones to cart button")
            are100_headphones_add_to_cart_btn.click()
        except:
            logging.error("Add are100 headphones to cart - failed")
            return
        logging.info("Add are100 headphones to cart - end")

        logging.info("Increase product quantity - start")
        try:
            logging.debug("Getting increase quantity button")
            product_quantity_up_btn = driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/article/div/form/div[2]/table/tbody/tr/td[5]/div/div[2]/div[1]/a[1]")
            logging.debug("Click increase quantity button")
            product_quantity_up_btn.click()
        except:
            logging.error("Increase product quantity - failed")
            return
        logging.info("Increase product quantity - end")

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
