**Маркет Деливери** - это онлайн-сервис доставки еды, позволяющий пользователям заказывать блюда из различных ресторанов и кафе, а также продукты из супермаркетов и магазинов  
[Ссылка на тест-план финального проекта](https://kskschi.yonote.ru/share/98a1217b-a69d-4d4a-b6df-b49cdaaf5947)  
  
Автоматизировано 5 API-тестов на основе коллекции в Postman и 5 UI-тестов на основе функционального чек-листа (позитив)  
classes_api.py - классы api-тестов  
classes_ui.py - классы ui-тестов  
test_api.py - api-тесты  
test_ui.py - ui-тесты  
  
**Cookie в classes_api.py** 
Перед запуском api-тестов нужно заполнить словарь cookie в методе cookie  
Для того, чтобы найти нужное значение, необходимо перейти на [сайт](https://market-delivery.yandex.ru/retail/paterocka/catalog/1033?placeSlug=pyatyorochka_pvtm6) и скопировать значение Cookie из Request Headers. **Авторизовываться не нужно**  
  
**Пример шагов**
1. Открыть сайт по [ссылке](https://market-delivery.yandex.ru/retail/paterocka/catalog/1033?placeSlug=pyatyorochka_pvtm6)
2. Открыть DevTools, вкладка Network
3. Добавить любой товар в корзину и найти этот запрос в DevTools
4. В Request Headers найти ключ Cookie
5. Скопировать значение ключа Cookie
  

**Команды для запуска:**  
**Все тесты** - pytest  
**Только API** - pytest -m api  
**Только UI** - pytest -m ui  
  
Чтобы запустить только один тест, нужно добавить к команде _№теста  
**Пример:** Нужно запустить третий UI-тест. Команда: pytest -m ui_3  
*Все маркеры обозначены в файле pytest.ini*
  
**Команды Allure:**  
**Запуск тестов и создание папки results:** pytest --alluredir=./results  
**Генерация отчета в папке final-report:** allure generate results -o final-report  
**Открыть отчет:** allure open final-report  
