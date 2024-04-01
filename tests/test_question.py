from datetime import time
from time import sleep

import pytest
from selenium import webdriver
import allure
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
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка формы вопрос-ответ на главной странице')
    @pytest.mark.parametrize('locator,result,answer',
                             [
                                 (today_locator, today_result, today_answer),
                                 (extension_locator, extension_result, extension_answer),
                                 (charger_locator, charger_result, charger_answer),
                                 (cancel_locator, cancel_result, cancel_answer),
                                 (zamkadish_locator, zamkadish_result, zamkadish_answer),
                                 (time_locator, time_result, time_answer),
                                 (multipy_locator, multipy_result, multipy_answer),
                                 (price_locator, price_result, price_answer),
                             ]
                             )
    def test_param_question(self, locator, result, answer):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        questionpage.question_button_click(locator)
        assert questionpage.question_result_text(answer) == result, \
            f'ответ {result} не совпадает c тем, что показали пользователю'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
