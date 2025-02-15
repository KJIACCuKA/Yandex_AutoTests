import petstore_docs
import user_data
import requests

user_path = '/v2/user'

# Создаем пользователя
def create_user(body):
    return requests.post(petstore_docs.petstore_docs_url + user_path, json=body, headers=user_data.headers)

responce = create_user(user_data.user_body)
print(responce.status_code)
print(responce.json())

# Создаем нескольких пользователей
def create_list_of_users(body):
    return requests.post(petstore_docs.petstore_docs_url + user_path + '/createWithList', json=body, headers=user_data.headers)

responce = create_list_of_users(user_data.list_of_users)
# print(responce.status_code)
# print(responce.json())

# Проверяем наличие пользователя
def get_user(username):
    return requests.get(petstore_docs.petstore_docs_url + user_path + '/' + username)

responce = get_user('GarryPotter')
print(responce.status_code)
print(responce.json())

# Авторизация пользователя
def user_login(username, password):
    return requests.get(petstore_docs.petstore_docs_url + user_path + '/login?username=' + username + '&' + 'password=' + password)

responce = user_login('GarryPotter', '123')
print(responce.status_code)
print(responce.json())

# Изменяем данные пользователя
# def change_user_data(body, username):
#     return requests.put(petstore_docs.petstore_docs_url + user_path + '/' + username, json=body, headers=user_data.headers)

# responce = change_user_data(user_data.changed_user_body, 'GarryPotter')
# print(responce.status_code)
# print(responce.json())

# # Проверяем, изменились ли данные
# responce = get_user('GarryPotter')
# print(responce.status_code)
# print(responce.json())

# # Удаляем пользователя
# def delete_user(username):
#     return requests.delete(petstore_docs.petstore_docs_url + user_path + '/' + username)

# responce = delete_user('GarryPotter')
# print(responce.status_code)
# print(responce.json())