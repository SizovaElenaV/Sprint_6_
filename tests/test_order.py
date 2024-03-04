import pytest
from selenium import webdriver
import allure
from pages import OrderPage
from pages import MainPage
from data import *


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка кнопки заказа в заголовке страницы')
    def test_header_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        orderpage = MainPage(self.driver)
        orderpage.order_header_button_click()
        orderpage.wait_untill_url_to_be('https://qa-scooter.praktikum-services.ru/order')

        assert orderpage.get_current_url() == 'https://qa-scooter.praktikum-services.ru/order', \
            'редирект не был завершен успешно'

    @allure.title('Проверка кнопки заказа в карточке страницы')
    def test_roadmap_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        orderpage = MainPage(self.driver)
        orderpage.order_roadmap_button_click()
        orderpage.wait_untill_url_to_be('https://qa-scooter.praktikum-services.ru/order')

        assert orderpage.get_current_url() == 'https://qa-scooter.praktikum-services.ru/order', \
            'редирект не был завершен успешно'

    @allure.title('Проверка заполнения заказа в форме заказа')
    @pytest.mark.parametrize('name,surname,area,metro,phone,date,rent,comment',
                             popup_order_data)
    def test_popup_order(self, name, surname, area, metro, phone, date, rent, comment):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order/')
        order_page = OrderPage(self.driver)
        order_page.order_fill_form(name, surname, area, metro, phone)
        order_page.order_continue_button_click()

        order_page.orderfinal_fill_form(date, rent, comment)
        order_page.orderfinal_button_click()
        order_page.orderfinal_popupbutton_click()
        assert 'Заказ оформлен' in order_page.get_page_source(), 'Заказ не оформлен'


    @allure.title('Проверка кнопки перехода на главную страницу')
    def test_samokat_button_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order/')
        order_page = OrderPage(self.driver)
        order_page.order_samokat_button_click()
        assert order_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка кнопки перехода на дзен')
    def test_dzen_button_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order/')
        order_page = OrderPage(self.driver)
        order_page.order_dzen_button_click()
        assert order_page.windows_count() == 2, "Новая вкладка не открылась"
        order_page.switch()
        order_page.wait_untill_url_to_be('https://dzen.ru/?yredirect=true')
        assert order_page.get_current_url() == 'https://dzen.ru/?yredirect=true', 'Целевая аудитория Дзена потерялась'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

