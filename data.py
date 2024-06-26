from selenium.webdriver.common.by import By

popup_order_data = [
        ('Щупик', 'Левченко', 'Ул.Красноземских', 'Комсомольская', '+79056743212', '04.02.2024', 'сутки', 'TTC'),
        ('Любитель', 'Самокатов', 'Ул.САМОКАТЫЫ', 'Скобелевская', '+79099943212', '05.02.2024', 'семеро суток',
         'БЫСТРЕЕ!!! Хочу кататься очень.')]

price_locator = (By.ID, 'accordion__heading-0')
price_result = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
price_answer = (By.XPATH, "//div[@id='accordion__panel-0']/p")

multipy_locator = (By.ID, 'accordion__heading-1')
multipy_result = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто '
                  'сделать несколько заказов — один за другим.')
multipy_answer = (By.XPATH, "//div[@id='accordion__panel-1']/p")


time_locator = (By.ID, 'accordion__heading-2')
time_result = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени '
               'аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
               '20:30, суточная аренда закончится 9 мая в 20:30.')
time_answer = (By.XPATH, "//div[@id='accordion__panel-2']/p")


today_locator = (By.ID, 'accordion__heading-3')
today_result = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
today_answer = (By.XPATH, "//div[@id='accordion__panel-3']/p")

extension_locator = (By.ID, 'accordion__heading-4')
extension_result = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру '
                    '1010.')
extension_answer = (By.XPATH, "//div[@id='accordion__panel-4']/p")


charger_locator = (By.ID, 'accordion__heading-5')
charger_result = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                  'кататься без передышек и во сне. Зарядка не понадобится.')
charger_answer = (By.XPATH, "//div[@id='accordion__panel-5']/p")


cancel_locator = (By.ID, 'accordion__heading-6')
cancel_result = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же '
                 'свои.')
cancel_answer = (By.XPATH, "//div[@id='accordion__panel-6']/p")


zamkadish_locator = (By.ID, 'accordion__heading-7')
zamkadish_result = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
zamkadish_answer = (By.XPATH, "//div[@id='accordion__panel-7']/p")
