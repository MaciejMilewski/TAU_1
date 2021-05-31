from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s', filename='empik.log', encoding='utf-8', level=logging.DEBUG)


def test_product_order_details(expected_text, driver):
    try:
        url = "https://www.empik.com/"

        logging.debug("Maximizing chrome driver window")
        driver.maximize_window()

        logging.info("Waiting for https://www.empik.com/ - start")
        try:
            logging.debug("Waiting for https://www.empik.com/ - try")
            driver.get(url)
        except:
            logging.error("Waiting for https://www.empik.com/ - failed")
            return
        logging.info("Waiting for https://www.empik.com/ - end")
        time.sleep(1.5)

        logging.info("Using searchbar - start")
        try:
            logging.debug("Getting searchbar input field")
            search_bar_input = driver.find_element_by_xpath('/html/body/header/div/div/div[3]/div/div/form/div[1]/input')
            logging.debug("Inserting string to searchbar input field")
            search_bar_input.send_keys("ekstremista")
        except:
            logging.error("Using searchbar - failed")
            return
        logging.info("Using searchbar - end")
        time.sleep(1.5)

        logging.info("Using search button- start")
        try:
            logging.debug("Getting search button")
            search_btn = driver.find_element_by_xpath('/html/body/header/div/div/div[3]/div/div/form/button')
            logging.debug("Click button")
            search_btn.click()
        except:
            logging.error("Using search button - failed")
            return
        logging.info("Using search button - end")
        time.sleep(1.5)

        logging.info("Selecting product card- start")
        try:
            logging.debug("Getting product card element")
            book_card = driver.find_element_by_xpath(
                '/html/body/main/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/a')
            logging.debug("Click product card")
            book_card.click()
        except:
            logging.error("Selecting product card - failed")
            return
        logging.info("Selecting product card - end")
        time.sleep(1.5)

        logging.info("Add product to card - start")
        try:
            logging.debug("Getting add product to cart button")
            add_to_cart_btn = driver.find_element_by_xpath('/html/body/main/div[1]/div[3]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[5]/div/button')
            logging.debug("Click add product to cart button")
            add_to_cart_btn.click()
        except:
            logging.error("Add product to card - failed")
            return
        logging.info("Add product to card - end")
        time.sleep(1.5)

        logging.info("Go to cart - start")
        try:
            logging.debug("Getting go to cart button")
            go_to_cart_btn = driver.find_element_by_xpath('//*[@id="portal-root"]/div/div[2]/div[2]/div[1]/button')
            logging.debug("Click go to cart button")
            go_to_cart_btn.click()
        except:
            logging.error("Go to cart - failed")
            return
        logging.info("Go to cart - end")

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