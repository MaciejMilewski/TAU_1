from selenium import webdriver
import unittest
import test_newsletter_case
import test_login_case
import test_register_case
import tracemalloc


def driver_chrome():
    return webdriver.Chrome(executable_path="drivers/chromedriver.exe")


def driver_firefox():
    return webdriver.Firefox(executable_path="drivers/geckodriver.exe")


def driver_edge():
    return webdriver.Edge(executable_path="drivers/msedgedriver.exe")


class TestCzasNaButyLogin(unittest.TestCase):

    def test_no_email_chrome(self):
        result = test_login_case.test_login_no_email(driver_chrome())
        self.assertTrue(result)

    def test_no_password_chrome(self):
        result = test_login_case.test_login_no_password(driver_chrome())
        self.assertTrue(result)

    def test_no_email_and_password_chrome(self):
        result = test_login_case.test_login_no_email_and_password(driver_chrome())
        self.assertTrue(result)

    def test_wrong_email_chrome(self):
        result = test_login_case.test_login_wrong_email(driver_chrome())
        self.assertTrue(result)

    def test_wrong_password_chrome(self):
        result = test_login_case.test_login_wrong_password(driver_chrome())
        self.assertTrue(result)

    def test_no_email_firefox(self):
        result = test_login_case.test_login_no_email(driver_firefox())
        self.assertTrue(result)

    def test_no_password_firefox(self):
        result = test_login_case.test_login_no_password(driver_firefox())
        self.assertTrue(result)

    def test_no_email_and_password_firefox(self):
        result = test_login_case.test_login_no_email_and_password(driver_firefox())
        self.assertTrue(result)

    def test_wrong_email_firefox(self):
        result = test_login_case.test_login_wrong_email(driver_firefox())
        self.assertTrue(result)

    def test_wrong_password_firefox(self):
        result = test_login_case.test_login_wrong_password(driver_firefox())
        self.assertTrue(result)

    def test_no_email_edge(self):
        result = test_login_case.test_login_no_email(driver_edge())
        self.assertTrue(result)

    def test_no_password_edge(self):
        result = test_login_case.test_login_no_password(driver_edge())
        self.assertTrue(result)

    def test_no_email_and_password_edge(self):
        result = test_login_case.test_login_no_email_and_password(driver_edge())
        self.assertTrue(result)

    def test_wrong_email_edge(self):
        result = test_login_case.test_login_wrong_email(driver_edge())
        self.assertTrue(result)

    def test_wrong_password_edge(self):
        result = test_login_case.test_login_wrong_password(driver_edge())
        self.assertTrue(result)


class TestCzasNaButyRegister(unittest.TestCase):

    def test_test_no_shop_regulations_checkbox_chrome(self):
        result = test_register_case.test_register_no_shop_regulations_checkbox(driver_chrome())
        self.assertTrue(result)

    def test_register_no_name_chrome(self):
        result = test_register_case.test_register_no_name(driver_chrome())
        self.assertTrue(result)

    def test_register_no_surname_chrome(self):
        result = test_register_case.test_register_no_surname(driver_chrome())
        self.assertTrue(result)

    def test_register_blank_form_chrome(self):
        result = test_register_case.test_register_blank_form(driver_chrome())
        self.assertTrue(result)

    def test_register_wrong_email_chrome(self):
        result = test_register_case.test_register_wrong_email(driver_chrome())
        self.assertTrue(result)

    def test_register_wrong_postal_code_chrome(self):
        result = test_register_case.test_register_wrong_postal_code(driver_chrome())
        self.assertTrue(result)

    def test_register_wrong_address_chrome(self):
        result = test_register_case.test_register_wrong_address(driver_chrome())
        self.assertTrue(result)

    def test_register_no_password_confirmation_chrome(self):
        result = test_register_case.test_register_no_password_confirmation(driver_chrome())
        self.assertTrue(result)

    def test_test_no_shop_regulations_checkbox_firefox(self):
        result = test_register_case.test_register_no_shop_regulations_checkbox(driver_firefox())
        self.assertTrue(result)

    def test_register_no_name_firefox(self):
        result = test_register_case.test_register_no_name(driver_firefox())
        self.assertTrue(result)

    def test_register_no_surname_firefox(self):
        result = test_register_case.test_register_no_surname(driver_firefox())
        self.assertTrue(result)

    def test_register_blank_form_firefox(self):
        result = test_register_case.test_register_blank_form(driver_firefox())
        self.assertTrue(result)

    def test_register_wrong_email_firefox(self):
        result = test_register_case.test_register_wrong_email(driver_firefox())
        self.assertTrue(result)

    def test_register_wrong_postal_code_firefox(self):
        result = test_register_case.test_register_wrong_postal_code(driver_firefox())
        self.assertTrue(result)

    def test_register_wrong_address_firefox(self):
        result = test_register_case.test_register_wrong_address(driver_firefox())
        self.assertTrue(result)

    def test_register_no_password_confirmation_firefox(self):
        result = test_register_case.test_register_no_password_confirmation(driver_firefox())
        self.assertTrue(result)

    def test_test_no_shop_regulations_checkbox_edge(self):
        result = test_register_case.test_register_no_shop_regulations_checkbox(driver_edge())
        self.assertTrue(result)

    def test_register_no_name_edge(self):
        result = test_register_case.test_register_no_name(driver_edge())
        self.assertTrue(result)

    def test_register_no_surname_edge(self):
        result = test_register_case.test_register_no_surname(driver_edge())
        self.assertTrue(result)

    def test_register_blank_form_edge(self):
        result = test_register_case.test_register_blank_form(driver_edge())
        self.assertTrue(result)

    def test_register_wrong_email_edge(self):
        result = test_register_case.test_register_wrong_email(driver_edge())
        self.assertTrue(result)

    def test_register_wrong_postal_code_edge(self):
        result = test_register_case.test_register_wrong_postal_code(driver_edge())
        self.assertTrue(result)

    def test_register_wrong_address_edge(self):
        result = test_register_case.test_register_wrong_address(driver_edge())
        self.assertTrue(result)

    def test_register_no_password_confirmation_edge(self):
        result = test_register_case.test_register_no_password_confirmation(driver_edge())
        self.assertTrue(result)


class TestCzasNaButyRegister(unittest.TestCase):

    def test_newsletter_wrong_email_chrome(self):
        result = test_newsletter_case.test_newsletter_wrong_email(driver_chrome())
        self.assertTrue(result)

    def test_newsletter_no_terms_checkbox_chrome(self):
        result = test_newsletter_case.test_newsletter_no_terms_checkbox(driver_chrome())
        self.assertTrue(result)

    def test_newsletter_no_email_chrome(self):
        result = test_newsletter_case.test_newsletter_no_email(driver_chrome())
        self.assertTrue(result)

    def test_newsletter_wrong_email_firefox(self):
        result = test_newsletter_case.test_newsletter_wrong_email(driver_firefox())
        self.assertTrue(result)

    def test_newsletter_no_terms_checkbox_firefox(self):
        result = test_newsletter_case.test_newsletter_no_terms_checkbox(driver_firefox())
        self.assertTrue(result)

    def test_newsletter_no_email_firefox(self):
        result = test_newsletter_case.test_newsletter_no_email(driver_firefox())
        self.assertTrue(result)

    def test_newsletter_wrong_email_edge(self):
        result = test_newsletter_case.test_newsletter_wrong_email(driver_edge())
        self.assertTrue(result)

    def test_newsletter_no_terms_checkbox_edge(self):
        result = test_newsletter_case.test_newsletter_no_terms_checkbox(driver_edge())
        self.assertTrue(result)

    def test_newsletter_no_email_edge(self):
        result = test_newsletter_case.test_newsletter_no_email(driver_edge())
        self.assertTrue(result)


if __name__ == '__main__':
    tracemalloc.start()
    unittest.main()
