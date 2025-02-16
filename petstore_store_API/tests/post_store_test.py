import store_requests
import store_data

# POST /store/order

# Проверка, что заказ создается
def test_place_an_order_for_a_pet():
    responce = store_requests.place_an_order_for_a_pet(store_data.data)
    assert responce.status_code == 200
    assert responce.json() != None
    assert responce.json()['id'] == store_data.data['id']
    assert responce.json()['petId'] == store_data.data['petId']
    assert responce.json()['quantity'] == store_data.data['quantity']
    assert responce.json()['status'] == store_data.data['status']
    assert responce.json()['complete'] == store_data.data['complete']

# Проверка, что заказ создается без id в теле
def test_place_an_order_withot_id_for_a_pet():
    responce = store_requests.place_an_order_for_a_pet(store_data.data_without_id)
    assert responce.status_code == 200
    assert responce.json() != None
    assert responce.json()['id'] != None
    assert responce.json()['petId'] == store_data.data_without_id['petId']
    assert responce.json()['quantity'] == store_data.data_without_id['quantity']
    assert responce.json()['status'] == store_data.data_without_id['status']
    assert responce.json()['complete'] == store_data.data_without_id['complete']

# Проверка, что заказ создается без body
def test_place_an_order_withot_body():
    responce = store_requests.place_an_order_for_a_pet(store_data.store_data_without_body)
    assert responce.status_code == 200
    assert responce.json() != None
    assert responce.json()['id'] != None
    assert responce.json()['complete'] == False