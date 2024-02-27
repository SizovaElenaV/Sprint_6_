import pytest
from selenium import webdriver

from pages import MainPage

from data import *


class TestQuestion:
    """
    Стоить обратить внимание на то,
    что в задании явно указано требование для каждого вопроса использовать отдельную функцию,
    поэтому такое размножение похожих функций
    ........................................................................................
    """
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Edge()

    @pytest.mark.parametrize('locator,result',
                             [
                                 (today_locator, today_result),
                                 (extension_locator, extension_result),
                                 (charger_locator, charger_result),
                                 (cancel_locator, cancel_result),
                                 (zamkadish_locator, zamkadish_result),
                                 (time_locator, time_result),
                                 (multipy_locator, multipy_result),
                                 (price_locator, price_result),
                              ]
                             )
    def test_param_question(self, locator, result):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == result, \
            f'ответ {result} не совпадает c тем, что показали пользователю'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

