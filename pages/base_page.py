from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def execute_script(self, script, element):
        return self.driver.execute_script(script, element)

    def js_click(self, elem):
        return self.driver.execute_script("arguments[0].click()", elem)


    def click_element(self, element):
        return element.click()

    def get_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def get_text(self, element):
        return element.text

    def send_keys(self, element, data):
        element.send_keys(data)

    def click(self, element):
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def windows_count(self):
        return len(self.driver.window_handles)

    def wait_untill_url_to_be(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    def get_page_source(self):
        return self.driver.page_source


