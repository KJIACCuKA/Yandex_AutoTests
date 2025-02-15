user_body = {
  "id": 1,
  "username": "GarryPotter",
  "firstName": "Garry",
  "lastName": "Potter",
  "email": "iamamagic@mail.ru",
  "password": "123",
  "phone": "934",
  "userStatus": 0
}

user_body_for_change = {
  "id": 12,
  "username": "FirstSecond",
  "firstName": "First",
  "lastName": "Second",
  "email": "firstsecond@mail.ru",
  "password": "123",
  "phone": "12",
  "userStatus": 0
}

user_body_for_delete = {
  "id": 10,
  "username": "GarryPotterDelete",
  "firstName": "Garry",
  "lastName": "Potter",
  "email": "iamamagic@mail.ru",
  "password": "123",
  "phone": "934",
  "userStatus": 0
}

user_body_without_params = {

}

changed_user_body = {
  "id": 12,
  "username": "FirstSecond",
  "firstName": "Optimus",
  "lastName": "Prime",
  "email": "autobots@mail.ru",
  "password": "1234",
  "phone": "100",
  "userStatus": 1
}

list_of_users = [
  {
    "id": 3,
    "username": "Megatron",
    "firstName": "Mega",
    "lastName": "tron",
    "email": "decepticons@mail.ru",
    "password": "123",
    "phone": "101",
    "userStatus": 0
  },
  {
    "id": 4,
    "username": "BumbleBee",
    "firstName": "Bumble",
    "lastName": "Bee",
    "email": "autobot@mail.ru",
    "password": "123",
    "phone": "102",
    "userStatus": 0
  }
]

headers = {
    "Content-Type": "application/json"
}