import allure
from selenium.webdriver.common.by import By

from base_page import BasePage


class MainPage(BasePage):
    question_block = (By.CLASS_NAME, "accordion")
    header_buttons = (By.CLASS_NAME, "Header_Nav__AGCXC")
    roadmap_block = (By.CLASS_NAME, 'Home_RoadMap__2tal_')
    locator_tag_name_p = (By.TAG_NAME, 'p')

    @allure.step('Нажатие на конпку вопроса')
    def question_button_click(self, locator_inside):
        elem = self.find_element(self.find_element(self.driver, self.question_block), locator_inside)
        self.execute_script(self.driver, "arguments[0].click()", elem)
        return self.get_attribute(elem, 'aria-controls')

    @allure.step('Нажатие на кнопку заказа в заголовке страницы')
    def order_header_button_click(self):
        elem = self.find_element(self.find_element(self.driver, self.header_buttons), (By.TAG_NAME, 'button'))
        self.execute_script(self.driver, "arguments[0].click()", elem)

    @allure.step('Нажатие на кнопку заказа в середине страницы')
    def order_roadmap_button_click(self):
        elem = self.find_element(self.find_element(self.driver, self.roadmap_block), (By.TAG_NAME, 'button'))
        self.execute_script(self.driver, "arguments[0].click()", elem)

    @allure.step('Проверка текста ответа на вопрос')
    def question_result_text(self, locator_inside):
        return self.get_text(
            self.find_element(self.find_element(self.find_element(self.driver, self.question_block), locator_inside),
                              self.locator_tag_name_p))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


