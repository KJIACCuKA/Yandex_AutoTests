import store_requests
import store_data

# DELETE /store/order/{orderId}

# Проверка, что можно удалить заказ
def test_delete_order():
    store_requests.place_an_order_for_a_pet(store_data.data)
    responce = store_requests.delete_purchase_order_in_store(store_data.data["id"])
    assert responce.status_code == 200
    assert responce.json()['code'] == 200
    assert responce.json()['type'] == 'unknown'
    assert responce.json()['message'] == f'{store_data.data["id"]}'

# Проверка, что нельзя удалить несуществующий заказ
def test_cant_delete_doesnt_exist_order():
    responce = store_requests.delete_purchase_order_in_store(4234234242)
    assert responce.status_code == 404
    assert responce.json()["code"] == 404
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == "Order Not Found"