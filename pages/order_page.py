import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class OrderPage(BasePage):
    name_locator = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_locator = (By.XPATH, "//input[@placeholder='* Фамилия']")
    area_locator = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_locator = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_locator = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    continue_locator = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    samokat_locator = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    dzen_locator = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    metro_search = (By.CLASS_NAME, 'select-search__select')
    metro_index = (By.XPATH, "//li[@data-index='0']")
    metro_button = (By.TAG_NAME, 'button')

    date_locator = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rent_button_locator = (By.CLASS_NAME, "Dropdown-arrow")
    color_black_locator = (By.ID, 'black')
    color_grey_locator = (By.ID, 'grey')
    comment_locator = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    orderbutton_locator = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    popupbutton_locator = (By.XPATH, f"//button[contains(text(), 'Да')]")

    @allure.step('Заполняем первую форму')
    def order_fill_form(self, name, surname, area, metro, phone):
        self.order_set_name(name)
        self.order_set_surname(surname)
        self.order_set_area(area)
        self.order_set_metro(metro)
        self.order_set_phone(phone)

    @allure.step('Заполнение Имени в Поле Формы Ордера')
    def order_set_name(self, name):
        self.send_keys(self.find_element(self.name_locator), name)

    @allure.step('Заполнение Фамилии в Поле Формы Ордера')
    def order_set_surname(self, surname):
        self.send_keys(self.find_element(self.surname_locator), surname)

    @allure.step('Заполнение Города в Поле Формы Ордера')
    def order_set_area(self, area):
        self.send_keys(self.find_element(self.area_locator), area)

    @allure.step('Заполнение Метро в Поле Формы Ордера')
    def order_set_metro(self, metro):
        self.send_keys(self.find_element(self.metro_locator), metro)
        self.click(self.find_element(self.metro_search).find_element(*self.metro_index).find_element(*self.metro_button))

    @allure.step('Заполнение Телефона в Поле Формы Ордера')
    def order_set_phone(self, phone):
        self.send_keys(self.find_element(self.phone_locator), phone)

    @allure.step('Переход на вторую стадию заполнения формы')
    def order_continue_button_click(self):
        self.js_click(self.find_element(self.continue_locator))

    @allure.step('Нажатие на кнопку самокат')
    def order_samokat_button_click(self):
        self.click(self.find_element(self.samokat_locator))

    @allure.step('Нажатие на кнопку Яндекс в заголовке страницы')
    def order_dzen_button_click(self):
        self.click(self.find_element(self.dzen_locator))

    @allure.step('Заполнение второй части формы')
    def orderfinal_fill_form(self, date, rent, comment, black=True):
        self.orderfinal_set_date(date)
        self.orderfinal_set_rent(rent)
        if black:
            self.orderfinal_set_black()
        else:
            self.orderfinal_set_grey()
        self.orderfinal_set_comment(comment)

    @allure.step('Заполнение Даты в Поле 2-ой Формы Ордера')
    def orderfinal_set_date(self, date):
        self.send_keys(self.find_element(self.date_locator), date)

    @allure.step('Заполнение Аренды в Поле 2-ой Формы Ордера')
    def orderfinal_set_rent(self, rent):
        self.click(self.find_element(self.rent_button_locator))
        self.click(self.find_element(self._rent_locator(rent)))

    @allure.step('Выбор черного цвета в поле цвета 2-ой Формы Ордера')
    def orderfinal_set_black(self):
        self.click(self.find_element(self.color_black_locator))

    @allure.step('Выбор серого цвета в поле цвета 2-ой Формы Ордера')
    def orderfinal_set_grey(self):
        self.click(self.find_element(self.color_grey_locator))

    @allure.step('Заполнение Коммента в Поле 2-ой Формы Ордера')
    def orderfinal_set_comment(self, comment):
        self.send_keys(self.find_element(self.comment_locator), comment)

    @allure.step('Нажатии кнопки потверждения заявки')
    def orderfinal_button_click(self):
        self.click(self.find_element(self.orderbutton_locator))

    @allure.step('Нажатие нкопки на Попаппе')
    def orderfinal_popupbutton_click(self):
        self.click(self.find_element(self.popupbutton_locator))

    def _rent_locator(self, rent):
        return (By.XPATH, f"//*[contains(text(), '{rent}')]")

