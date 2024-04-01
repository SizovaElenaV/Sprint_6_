import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    header_buttons = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']")
    roadmap_block = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")

    @allure.step('Нажатие на конпку вопроса')
    def question_button_click(self, locator_inside):
        self.js_click(locator_inside)

    @allure.step('Нажатие на кнопку заказа в заголовке страницы')
    def order_header_button_click(self):
        self.js_click(self.header_buttons)

    @allure.step('Нажатие на кнопку заказа в середине страницы')
    def order_roadmap_button_click(self):
        self.js_click(self.roadmap_block)

    @allure.step('Проверка текста ответа на вопрос')
    def question_result_text(self, locator_inside):
        return self.get_text(locator_inside)
