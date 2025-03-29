import pytest
import allure
from classes_api import API
api = API('https://market-delivery.yandex.ru')


@pytest.mark.api
@pytest.mark.api_1
@allure.id('№1')
@allure.epic('Delivery. API')
@allure.title('Добавление товара в корзину')
def test_add_to_cart():
    with allure.step('Добавить в корзину товар "Мандарины вес" в кол-ве 1'):
        resp = api.add_to_cart()

    with allure.step('Проверить, что в теле ответа корректное'
                     ' название добавленного товара'):
        assert resp['cart']['items'][0]['name'] == 'Мандарины вес'

    with allure.step('Очистить корзину'):
        api.clear_cart()


@pytest.mark.api
@pytest.mark.api_2
@allure.id('№2')
@allure.epic('Delivery. API')
@allure.title('Изменение количества товара')
def test_change_quantity():
    with allure.step('Предусловие'):
        with allure.step('Очистить корзину'):
            api.clear_cart()
        with allure.step('Добавить товар в корзину в кол-ве 1'):
            req = api.add_to_cart()['id']

    with allure.step('Изменить количество добавленного товара на 5'):
        change = api.change_quantity(req)

    with allure.step('Проверить, что количество товара == 5'):
        assert change['cart']['items'][0]['quantity'] == 5

    with allure.step('Очистить корзину'):
        api.clear_cart()


@pytest.mark.api
@pytest.mark.api_3
@allure.id('№3')
@allure.epic('Delivery. API')
@allure.title('Очищение корзины')
def test_clear_cart():
    with allure.step('Предусловие'):
        with allure.step('Добавить товар в корзину'):
            api.add_to_cart()

    with allure.step('Очистить корзину'):
        resp = api.clear_cart()

    with allure.step('Проверить, что статус-код == 204'):
        assert resp == 204


@pytest.mark.api
@pytest.mark.api_4
@allure.id('№4')
@allure.epic('Delivery. API')
@allure.title('Изменение количества товара на большое значение')
def test_change_large_quantity():
    with allure.step('Предусловие'):
        with allure.step('Добавить товар в корзину'):
            req = api.add_to_cart()['id']

    with allure.step('Изменить количество на большое значение'):
        resp = api.change_quantity(req, 99999)

    with allure.step('Очистить корзину'):
        api.clear_cart()

    with allure.step('ПроверитЬ, что в ответе возвращается ошибка'):
        assert resp['err'] == ('Достигнуто максимальное число '
                               'одного айтема в корзине')


@pytest.mark.api
@pytest.mark.api_5
@allure.id('№5')
@allure.epic('Delivery. API')
@allure.title('Добавление в корзину товара в количестве 0')
def test_add_to_cart_zero():
    with allure.step('Добавить в корзину товар в количестве 0'):
        resp = api.add_to_cart(0)

    with allure.step('Проверить, что в ответе возвращается ошибка'):
        assert resp['err'] == 'Недопустимая операция'
