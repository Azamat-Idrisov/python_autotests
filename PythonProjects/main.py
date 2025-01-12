import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '801c0873eb2f1442594209a3ff3a65a0'
HEADER = {'Content-Type':'Application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_response = {
    "pokemon_id": "185451",
    "name": "Машка",
    "photo_id": 5
}
body_caught = {
    "pokemon_id": "185451"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

id = response_create.json()['id']
print(id)



response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_response)
print(response.text)




response_caught = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_caught)
print(response_caught.text)