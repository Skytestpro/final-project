from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UI:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def get_page(self):
        '''
        Открыть браузер на странице магазина "Пятерочка"
        и дождаться ее загрузки
        '''
        self.driver.get(
            'https://market-delivery.yandex.ru/retail/paterocka/'
            'catalog/1033?placeSlug=pyatyorochka_pvtm6')
        self.driver.implicitly_wait(30)

    def add_address(self):
        '''
        Добавление адреса доставки
        '''
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div/'
                                 'header/div/div/div[1]/div[2]'
                                 '/div[2]/div/button/span/span').click()

        address = self.driver.find_element(
            By.CSS_SELECTOR, 'input[data-testid="address-input"]')

        address.send_keys('Бирюлёвская д. 44/6', Keys.ENTER)

        self.driver.find_element(By.XPATH,
                                 '/html/body/div[3]/div/div/div/div/'
                                 'div[1]/div[2]/button').click()
        waiter = WebDriverWait(self.driver, 40, 0.1)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                             '.f18sb35s'),
                                             'Бирюлёвская улица'))

    def add_product(self):
        '''
        Добавление товара "Мандарины вес"
        (первое добавление)
        '''
        self.driver.find_element(
            By.XPATH,
            '//*[@id="menu-item-container____-32870106096"]'
            '/div/div[3]/button').click()

    def add_product_2(self):
        '''
        Добавление второго товара "Мандарины вес"
        '''
        self.driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div/div/div[1]/div/div/div/aside[2]'
            '/div/div/div[2]/div[2]/div/div[3]/div/button[2]').click()

    def remove_product(self):
        '''
        Очищение корзины через "-"
        '''
        delete_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div/div/div[1]/div/div/div/aside[2]'
            '/div/div/div[2]/div[2]/div/div[3]/div/button[1]')
        delete_button.click()

    def clear_cart(self):
        '''
        Очищение корзины с помощью кнопки "Очистить"
        '''
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="cart-clear-button"]').click()
        self.driver.find_element(
            By.XPATH,
            '/html/body/div[3]/div/div/div/div/div/div/button[2]').click()
        waiter = WebDriverWait(self.driver, 40, 0.1)
        waiter.until(
                    EC.text_to_be_present_in_element(
                                                    (By.CSS_SELECTOR,
                                                     '.NewCartEmpty_title'),
                                                     'В вашей корзине \nпока '
                                                     'пусто'))

    def next_button(self):
        '''
        Нажатие на кнопку "Далее"
        '''
        self.driver.find_element(
            By.CSS_SELECTOR,
            '[data-testid="desktop-cart-price-button"]').click()

    def shopping_cart(self) -> str:
        '''
        Поиск товара "Мандарины вес" в корзине
        '''
        item = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div/aside[2]'
            '/div/div/div[2]/div[2]/div/button').text
        return item

    def empty_cart(self) -> str:
        '''
        Текст пустой корзины
        '''
        empty_cart = self.driver.find_element(By.CSS_SELECTOR,
                                              '.NewCartEmpty_title').text
        return empty_cart

    def quantity(self) -> str:
        '''
        Количество товаров
        '''
        quantity = self.driver.find_element(
            By.CSS_SELECTOR, '[data-testid="item-quantity"]').text
        return quantity

    def auth(self) -> str:
        '''
        Текст "Введите номер телефона на странице авторизации
        '''
        auth = self.driver.find_element(By.CSS_SELECTOR,
                                        '.passp-add-account-page-title').text
        return auth
