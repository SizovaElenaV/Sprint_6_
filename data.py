from selenium.webdriver.common.by import By

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



