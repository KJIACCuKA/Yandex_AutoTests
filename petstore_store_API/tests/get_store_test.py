import store_requests
import store_data

# GET /store/inventory

# Проверка, что запрос возвращает инвентарь питомцев по статусу
def test_return_pet_inventories_by_status():
    responce = store_requests.return_pet_inventories_by_status()
    assert responce.status_code == 200
    assert responce.json() != None

# GET /store/order/{orderId}

# Проверка, что запрос находит заказ по id
def test_find_purchase_order_by_id():
    store_requests.place_an_order_for_a_pet(store_data.data)
    responce = store_requests.find_purchase_order_in_store(1)
    assert responce.status_code == 200
    assert responce.json() != None
    assert responce.json()['id'] == store_data.data['id']
    assert responce.json()['petId'] == store_data.data['petId']
    assert responce.json()['quantity'] == store_data.data['quantity']
    assert responce.json()['status'] == store_data.data['status']
    assert responce.json()['complete'] == store_data.data['complete']

# Проверка, что запрос не найдет заказ по несуществующему id
def test_find_purchase_order_by_doesnt_exist_id():
    responce = store_requests.find_purchase_order_in_store(10)
    assert responce.status_code == 404
    assert responce.json()['code'] == 1
    assert responce.json()['type'] == 'error'
    assert responce.json()['message'] == "Order not found"

# Так как в документации есть граничные значения для id заказа (1-10), то необходимо добавить следующие проверки (ниже)

# Проверка, что запрос не найдет заказ по id = 0
def test_find_purchase_order_by_zero_id():
    responce = store_requests.find_purchase_order_in_store(0)
    assert responce.status_code == 404
    assert responce.json()['code'] == 1
    assert responce.json()['type'] == 'error'
    assert responce.json()['message'] == "Order not found"

# Проверка, что запрос не найдет заказ по id = 11
def test_find_purchase_order_by_zero_id():
    responce = store_requests.find_purchase_order_in_store(11)
    assert responce.status_code == 404
    assert responce.json()['code'] == 1
    assert responce.json()['type'] == 'error'
    assert responce.json()['message'] == "Order not found"