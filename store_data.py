import json

store_data = '{ "id": 1, "petId": 1, "quantity": 1, "shipDate": "2025-02-15T18:31:32.287Z", "status": "placed", "complete": true}'

data = json.loads(store_data)