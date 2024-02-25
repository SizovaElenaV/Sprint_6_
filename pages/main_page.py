import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    question_block = (By.CLASS_NAME, "accordion")
    header_buttons = (By.CLASS_NAME, "Header_Nav__AGCXC")
    roadmap_block = (By.CLASS_NAME, 'Home_RoadMap__2tal_')
    locator_tag_name_p = (By.TAG_NAME, 'p')
    button_tag = (By.TAG_NAME, 'button')

    @allure.step('Нажатие на конпку вопроса')
    def question_button_click(self, locator_inside):
        elem = self.find_element(self.question_block).find_element(*locator_inside)
        self.execute_script("arguments[0].click()", elem)
        return self.get_attribute(elem, 'aria-controls')

    @allure.step('Нажатие на кнопку заказа в заголовке страницы')
    def order_header_button_click(self):
        elem = self.find_element(self.header_buttons).find_element(*self.button_tag)
        self.execute_script("arguments[0].click()", elem)

    @allure.step('Нажатие на кнопку заказа в середине страницы')
    def order_roadmap_button_click(self):
        elem = self.find_element(self.roadmap_block).find_element(By.TAG_NAME, 'button')
        self.execute_script("arguments[0].click()", elem)

    @allure.step('Проверка текста ответа на вопрос')
    def question_result_text(self, locator_inside):
        return self.get_text(self.find_element(self.question_block).find_element(*locator_inside)
                             .find_element(*self.locator_tag_name_p))

