from selenium import webdriver
import unittest
from RMSTestSuite import test_order_details_case
from EmpikTestSuite import test_shopping_cart_case


def driver_chrome():
    return webdriver.Chrome(executable_path="drivers/chromedriver.exe")


class TestRmsOrderDetails(unittest.TestCase):
    def test_order_details(self):
        result = test_order_details_case.test_adding_product_to_cart_with_quantity_change(driver_chrome())
        self.assertTrue(result)


class TestEmpikShoppingCart(unittest.TestCase):
    def test_shopping_cart(self):
        result = test_shopping_cart_case.test_order_details(driver_chrome())
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()


