import petstore_docs
import user_data
import requests

user_path = '/v2/user'

# Создаем пользователя
def create_user(body):
    return requests.post(petstore_docs.petstore_docs_url + user_path, json=body, headers=user_data.headers)

# Создаем нескольких пользователей
def create_list_of_users(body):
    return requests.post(petstore_docs.petstore_docs_url + user_path + '/createWithList', json=body, headers=user_data.headers)


# Проверяем наличие пользователя
def get_user(username):
    return requests.get(petstore_docs.petstore_docs_url + user_path + '/' + username)


# Авторизация пользователя
def user_login(username, password):
    return requests.get(petstore_docs.petstore_docs_url + user_path + '/login?username=' + username + '&' + 'password=' + password)


# Изменяем данные пользователя
def change_user_data(changed_body, username):
    create_user(user_data.user_body_for_change)
    return requests.put(petstore_docs.petstore_docs_url + user_path + '/' + username, json=changed_body, headers=user_data.headers)

# Удаляем пользователя
def delete_user(username):
    return requests.delete(petstore_docs.petstore_docs_url + user_path + '/' + username)
