import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages import MainPage, OrderPage, OrderFinalPage


class TestQuestion:
    """
    Стоить обратить внимание на то,
    что в задании явно указано требование для каждого вопроса использовать отдельную функцию,
    поэтому такое размножение похожих функций
    """
    driver = None

    price_locator = (By.ID, 'accordion__heading-0')
    price_result = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    multipy_locator = (By.ID, 'accordion__heading-1')
    multipy_result = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто '
                      'сделать несколько заказов — один за другим.')

    time_locator = (By.ID, 'accordion__heading-2')
    time_result = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени '
                   'аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
                   '20:30, суточная аренда закончится 9 мая в 20:30.')

    today_locator = (By.ID, 'accordion__heading-3')
    today_result = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    extension_locator = (By.ID, 'accordion__heading-4')
    extension_result = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру '
                        '1010.')

    charger_locator = (By.ID, 'accordion__heading-5')
    charger_result = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                      'кататься без передышек и во сне. Зарядка не понадобится.')

    cancel_locator = (By.ID, 'accordion__heading-6')
    cancel_result = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же '
                     'свои.')

    zamkadish_locator = (By.ID, 'accordion__heading-7')
    zamkadish_result = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Edge()

    def test_price_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(self.price_locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == self.price_result, \
            f'ответ {self.price_result} не совпадает c тем, что показали пользователю'

    def test_multipy_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(self.multipy_locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == self.multipy_result, \
            f'ответ {self.multipy_result} не совпадает c тем, что показали пользователю'

    def test_time_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(self.time_locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == self.time_result, \
            f'ответ {self.time_result} не совпадает c тем, что показали пользователю'

    def test_today_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(self.today_locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == self.today_result, \
            f'ответ {self.today_result} не совпадает c тем, что показали пользователю'

    def test_extension_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(self.extension_locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == self.extension_result, \
            f'ответ {self.extension_result} не совпадает c тем, что показали пользователю'

    def test_charger_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(self.charger_locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == self.charger_result, \
            f'ответ {self.charger_result} не совпадает c тем, что показали пользователю'

    def test_cancel_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(self.cancel_locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == self.cancel_result, \
            f'ответ {self.cancel_result} не совпадает c тем, что показали пользователю'

    def test_zamkadish_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questionpage = MainPage(self.driver)
        text_id = questionpage.question_button_click(self.zamkadish_locator)
        assert questionpage.question_result_text(
            (By.ID, text_id)) == self.zamkadish_result, \
            f'ответ {self.zamkadish_result} не совпадает c тем, что показали пользователю'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


class TestOrder:
    driver = None
    popup_order_data = [
        ('Щупик', 'Левченко', 'Ул.Красноземских', 'Комсомольская', '+79056743212', '04.02.2024', 'сутки', 'TTC'),
        ('Любитель', 'Самокатов', 'Ул.САМОКАТЫЫ', 'Скобелевская', '+79099943212', '05.02.2024', 'семеро суток',
         'БЫСТРЕЕ!!! Хочу кататься очень.')]

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Edge()

    def test_header_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        orderpage = MainPage(self.driver)
        orderpage.order_header_button_click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be('https://qa-scooter.praktikum-services.ru/order'))

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order', \
            'редирект не был завершен успешно'

    def test_roadmap_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        orderpage = MainPage(self.driver)
        orderpage.order_roadmap_button_click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be('https://qa-scooter.praktikum-services.ru/order'))

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order', \
            'редирект не был завершен успешно'

    @pytest.mark.parametrize('name,surname,area,metro,phone,date,rent,comment',
                             popup_order_data)
    def test_popup_order(self, name, surname, area, metro, phone, date, rent, comment):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order/')
        order_page = OrderPage(self.driver)
        order_page.order_fill_form(name, surname, area, metro, phone)
        order_page.order_continue_button_click()

        orderfinal_page = OrderFinalPage(self.driver)
        orderfinal_page.orderfinal_fill_form(date, rent, comment)
        orderfinal_page.orderfinal_button_click()
        orderfinal_page.orderfinal_popupbutton_click()
        assert 'Заказ оформлен' in self.driver.page_source, 'Заказ не оформлен'

    #   В Google после нажатия кнопки "да" ничего не происходит, поэтому я не могу рассмотреть позитивный сценарий

    def test_samokat_button_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order/')
        order_page = OrderPage(self.driver)
        order_page.order_samokat_button_click()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_dzen_button_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order/')
        order_page = OrderPage(self.driver)
        order_page.order_dzen_button_click()
        assert len(self.driver.window_handles) == 2, "Новая вкладка не открылась"
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'))
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true', 'Целевая аудитория Дзена потерялась'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
