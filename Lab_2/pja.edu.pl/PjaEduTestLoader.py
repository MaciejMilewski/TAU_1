from selenium import webdriver
import unittest
from PjaEduTestSuite import test_language_change_case, test_search_case, test_department_news_case
import tracemalloc


def driver_chrome():
    return webdriver.Chrome(executable_path="drivers/chromedriver.exe")


def driver_firefox():
    return webdriver.Firefox(executable_path="drivers/geckodriver.exe")


def driver_edge():
    return webdriver.Edge(executable_path="drivers/msedgedriver.exe")


class TestPjaEduLanguageChange(unittest.TestCase):
    pass
    def test_en_language_change_chrome(self):
        result = test_language_change_case.test_en_language_change((driver_chrome()))
        self.assertTrue(result)

    def test_ru_language_change_chrome(self):
        result = test_language_change_case.test_ru_language_change((driver_chrome()))
        self.assertTrue(result)

    def test_pl_language_change_chrome(self):
        result = test_language_change_case.test_pl_language_change((driver_chrome()))
        self.assertTrue(result)

    # def test_en_language_change_firefox(self):
    #     result = test_language_change_case.test_en_language_change((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_ru_language_change_firefox(self):
    #     result = test_language_change_case.test_ru_language_change((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_pl_language_change_firefox(self):
    #     result = test_language_change_case.test_pl_language_change((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_en_language_change_edge(self):
    #     result = test_language_change_case.test_en_language_change((driver_edge()))
    #     self.assertTrue(result)
    #
    # def test_ru_language_change_edge(self):
    #     result = test_language_change_case.test_ru_language_change((driver_edge()))
    #     self.assertTrue(result)
    #
    # def test_pl_language_change_edge(self):
    #     result = test_language_change_case.test_pl_language_change((driver_edge()))
    #     self.assertTrue(result)


class TestPjaEduSearch(unittest.TestCase):

    def test_find_hackathon_using_search_chrome(self):
        result = test_search_case.test_find_hackathon_using_search((driver_chrome()))
        self.assertTrue(result)

    def test_find_library_info_using_search_chrome(self):
        result = test_search_case.test_find_library_info_using_search((driver_chrome()))
        self.assertTrue(result)

    def test_find_japan_exchange_info_using_search_chrome(self):
        result = test_search_case.test_find_japan_exchange_info_using_search((driver_chrome()))
        self.assertTrue(result)

    # def test_find_hackathon_using_search_firefox(self):
    #     result = test_search_case.test_find_hackathon_using_search((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_find_library_info_using_search_firefox(self):
    #     result = test_search_case.test_find_library_info_using_search((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_find_japan_exchange_info_using_search_firefox(self):
    #     result = test_search_case.test_find_japan_exchange_info_using_search((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_find_hackathon_using_search_edge(self):
    #     result = test_search_case.test_find_hackathon_using_search((driver_edge()))
    #     self.assertTrue(result)
    #
    # def test_find_library_info_using_search_edge(self):
    #     result = test_search_case.test_find_library_info_using_search((driver_edge()))
    #     self.assertTrue(result)
    #
    # def test_find_japan_exchange_info_using_search_edge(self):
    #     result = test_search_case.test_find_japan_exchange_info_using_search((driver_edge()))
    #     self.assertTrue(result)


class TestPjaEduDepartmentNews(unittest.TestCase):
    def test_check_computer_science_article_chrome(self):
        result = test_department_news_case.test_check_computer_science_article((driver_chrome()))
        self.assertTrue(result)

    def test_check_interior_design_article_chrome(self):
        result = test_department_news_case.test_check_interior_design_article((driver_chrome()))
        self.assertTrue(result)

    def test_check_new_media_arts_article_chrome(self):
        result = test_department_news_case.test_check_new_media_arts_article((driver_chrome()))
        self.assertTrue(result)

    # def test_check_computer_science_article_firefox(self):
    #     result = test_department_news_case.test_check_computer_science_article((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_check_interior_design_article_firefox(self):
    #     result = test_department_news_case.test_check_interior_design_article((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_check_new_media_arts_article_firefox(self):
    #     result = test_department_news_case.test_check_new_media_arts_article((driver_firefox()))
    #     self.assertTrue(result)
    #
    # def test_check_computer_science_article_edge(self):
    #     result = test_department_news_case.test_check_computer_science_article((driver_edge()))
    #     self.assertTrue(result)
    #
    # def test_check_interior_design_article_edge(self):
    #     result = test_department_news_case.test_check_interior_design_article((driver_edge()))
    #     self.assertTrue(result)
    #
    # def test_check_new_media_arts_article_edge(self):
    #     result = test_department_news_case.test_check_new_media_arts_article((driver_edge()))
    #     self.assertTrue(result)


if __name__ == '__main__':
    tracemalloc.start()
    unittest.main()
