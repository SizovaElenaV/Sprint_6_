from selenium.webdriver.common.by import By


class MainPage:
    question_block = (By.CLASS_NAME, "accordion")
    header_buttons = (By.CLASS_NAME, "Header_Nav__AGCXC")
    roadmap_block = (By.CLASS_NAME, 'Home_RoadMap__2tal_')

    def __init__(self, driver):
        self.driver = driver

    def question_button_click(self, locator_inside):
        elem = self.driver.find_element(*self.question_block).find_element(*locator_inside)
        self.driver.execute_script("arguments[0].click()", elem)
        return elem.get_attribute('aria-controls')

    def order_header_button_click(self):
        elem = self.driver.find_element(*self.header_buttons).find_element(By.TAG_NAME, 'button')
        self.driver.execute_script("arguments[0].click()", elem)

    def order_roadmap_button_click(self):
        elem = self.driver.find_element(*self.roadmap_block).find_element(By.TAG_NAME, 'button')
        self.driver.execute_script("arguments[0].click()", elem)

    def question_result_text(self, locator_inside):
        return self.driver.find_element(*self.question_block).find_element(*locator_inside).find_element(By.TAG_NAME,
                                                                                             'p').text


class OrderPage:
    name_locator = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_locator = (By.XPATH, "//input[@placeholder='* Фамилия']")
    area_locator = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_locator = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_locator = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    continue_locator = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    samokat_locator = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    dzen_locator = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver):
        self.driver = driver

    def order_fill_form(self, name, surname, area, metro, phone):
        self.order_set_name(name)
        self.order_set_surname(surname)
        self.order_set_area(area)
        self.order_set_metro(metro)
        self.order_set_phone(phone)

    def order_set_name(self, name):
        self.driver.find_element(*self.name_locator).send_keys(name)

    def order_set_surname(self, surname):
        self.driver.find_element(*self.surname_locator).send_keys(surname)

    def order_set_area(self, area):
        self.driver.find_element(*self.area_locator).send_keys(area)

    def order_set_metro(self, metro):
        self.driver.find_element(*self.metro_locator).send_keys(metro)
        self.driver.find_element(
            *(By.CLASS_NAME, 'select-search__select')).find_element(
            *(By.XPATH, "//li[@data-index='0']")).find_element(
            *(By.TAG_NAME, 'button')).click()

    def order_set_phone(self, phone):
        self.driver.find_element(*self.phone_locator).send_keys(phone)

    def order_continue_button_click(self):
        self.driver.find_element(*self.continue_locator).click()

    def order_samokat_button_click(self):
        self.driver.find_element(*self.samokat_locator).click()

    def order_dzen_button_click(self):
        self.driver.find_element(*self.dzen_locator).click()


class OrderFinalPage:
    date_locator = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rent_button_locator = (By.CLASS_NAME, "Dropdown-arrow")
    color_black_locator = (By.ID, 'black')
    color_grey_locator = (By.ID, 'grey')
    comment_locator = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    orderbutton_locator = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    popupbutton_locator = (By.XPATH, f"//button[contains(text(), 'Да')]")

    def __init__(self, driver):
        self.driver = driver

    def orderfinal_fill_form(self, date, rent, comment, black=True):
        self.orderfinal_set_date(date)
        self.orderfinal_set_rent(rent)
        if black:
            self.orderfinal_set_black()
        else:
            self.orderfinal_set_grey()
        self.orderfinal_set_comment(comment)

    def orderfinal_set_date(self, date):
        self.driver.find_element(*self.date_locator).send_keys(date)

    def orderfinal_set_rent(self, rent):
        self.driver.find_element(*self.rent_button_locator).click()
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{rent}')]").click()

    def orderfinal_set_black(self):
        self.driver.find_element(*self.color_black_locator).click()

    def orderfinal_set_grey(self):
        self.driver.find_element(*self.color_grey_locator).click()

    def orderfinal_set_comment(self, comment):
        self.driver.find_element(*self.comment_locator).send_keys(comment)

    def orderfinal_button_click(self):
        self.driver.find_element(*self.orderbutton_locator).click()

    def orderfinal_popupbutton_click(self):
        self.driver.find_element(*self.popupbutton_locator).click()
