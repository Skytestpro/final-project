import requests


class API:

    def __init__(self, url):
        self.url = url

    def cookie(self) -> dict:
        '''
        Cookie
        '''
        cookie = {"Cookie": "cookie. подробнее в readme"}
        return cookie

    def add_to_cart(self, quantity=1) -> dict:
        '''
        Добавление товара "Мандарины вес" в корзину
        (по умолчанию добавляется 1 штука)
        '''
        body = {
                "item_id": "124afcb3-d766-4672-b6cf-adae1a2c3341",
                "quantity": quantity,
                "place_slug": "pyaterochka_mpkg5",
                "place_business": "shop"
                }
        resp = requests.post(
            f'{self.url}/api/v1/cart?longitude=37.663619770912874'
            '&latitude=55.586377732903735&screen=menu&shippingType='
            'delivery&autoTranslate=false',
            json=body, headers=self.cookie())
        return resp.json()

    def change_quantity(self, req_id: int, quantity=5) -> dict:
        '''
        Изменение количества товара в корзине (по умолчанию
        количество товаров после запроса - 5)
        '''
        body = {
                "quantity": quantity,
                "item_options": []
                }
        resp = requests.put(f'{self.url}/api/v1/cart/{req_id}?longitude'
                            '=37.663619770912874&latitude=55.5863777329037'
                            '35&screen=menu&shippingType=delivery&autoTr'
                            'anslate=false', json=body, headers=self.cookie())

        return resp.json()

    def clear_cart(self) -> int:
        '''
        Очистить корзину
        '''
        resp = requests.delete(
            f'{self.url}/api/v2/cart?longitude=37.663619770912874&'
            'latitude=55.586377732903735&screen=menu&shippingType=de'
            'livery&autoTranslate=false', headers=self.cookie())
        return resp.status_code
