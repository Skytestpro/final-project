from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from classes_ui import UI
import pytest
import allure


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.mark.ui
@pytest.mark.ui_1
@allure.id('№1')
@allure.epic('Delivery. UI')
@allure.title('Добавление товара "Мандарины вес" в корзину')
def test_add_product(driver):
    with allure.step('Открыть страницу с магазином'):
        ui = UI(driver)
        ui.get_page()

    with allure.step('Добавить адрес доставки'):
        ui.add_address()

    with allure.step('Добавить товар "Мандарины вес" в корзину'):
        ui.add_product()

    with allure.step('Проверить, что товар "Мандарины вес"'
                     ' добавлены в корзину'):
        assert ui.shopping_cart() in 'Мандарины вес'


@pytest.mark.ui
@pytest.mark.ui_2
@allure.id('№2')
@allure.epic('Delivery. UI')
@allure.title('Очищение корзины через "-"')
def test_remove_product(driver):
    with allure.step('Открыть страницу с магазином'):
        ui = UI(driver)
        ui.get_page()

    with allure.step('Добавить адрес доставки'):
        ui.add_address()

    with allure.step('Добавить товар "Мандарины вес" в корзину'):
        ui.add_product()

    with allure.step('Очистить корзину через "-"'):
        ui.remove_product()

    with allure.step('Проверить, что в корзине написано '
                     '"В вашей корзине пока пусто"'):
        assert ui.empty_cart() == 'В вашей корзине \nпока пусто'


@pytest.mark.ui
@pytest.mark.ui_3
@allure.id('№3')
@allure.epic('Delivery. UI')
@allure.title('Добавление товара "Мандарины вес" в кол-ве 2 и уменьшение на 1')
def test_add_two_remove_one(driver):
    with allure.step('Открыть страницу с магазином'):
        ui = UI(driver)
        ui.get_page()

    with allure.step('Добавить адрес доставки'):
        ui.add_address()

    with allure.step('Добавить товар "Мандарины вес" в корзину'):
        ui.add_product()

    with allure.step('Добавить товар "Мандарины вес" в корзину '
                     'второй раз через кнопку "+" в корзине'):
        ui.add_product_2()

    with allure.step('Удалить из корзины 1 шт товара "Мандарины вес" '
                     'через кнопку "-"'):
        ui.remove_product()

    with allure.step('Проверить, что количество товара == 1'):
        assert ui.quantity() == '1'


@pytest.mark.ui
@pytest.mark.ui_4
@allure.id('№4')
@allure.epic('Delivery. UI')
@allure.title('Очищение корзины через кнопку "Очистить"')
def test_clear_cart(driver):
    with allure.step('Открыть страницу с магазином'):
        ui = UI(driver)
        ui.get_page()

    with allure.step('Добавить адрес доставки'):
        ui.add_address()

    with allure.step('Добавить товар "Мандарины вес" в корзину'):
        ui.add_product()

    with allure.step('Очистить корзину через кнопку "Очистить"'):
        ui.clear_cart()

    with allure.step('Проверить, что корзина пуста'):
        assert ui.empty_cart() == 'В вашей корзине \nпока пусто'


@pytest.mark.ui
@pytest.mark.ui_5
@allure.id('№5')
@allure.epic('Delivery. UI')
@allure.title('Работоспособность кнопки "Далее" без авторизации')
def test_next_button(driver):
    with allure.step('Открыть страницу с магазином'):
        ui = UI(driver)
        ui.get_page()

    with allure.step('Добавить адрес доставки'):
        ui.add_address()

    with allure.step('Добавить товар "Мандарины вес" в корзину'):
        ui.add_product()

    with allure.step('Нажать на кнопку "Далее"'):
        ui.next_button()

    with allure.step('Проверить, что произошел переход '
                     'на страницу с авторизацией'):
        assert ui.auth() == 'Введите номер телефона'
