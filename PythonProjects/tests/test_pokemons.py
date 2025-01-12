import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '801c0873eb2f1442594209a3ff3a65a0'
HEADER = {'Content-Type':'Application/json', 'trainer_token':TOKEN} 
TRAINER_ID = '13866'
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}) 
    assert response.status_code == 200 

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}) 
    assert response_get.json()["data"][0]["trainer_name"] == 'Хелкард'

@pytest.mark.parametrize('key, value', [('trainer_name','Хелкард'),('id',f'{TRAINER_ID}')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value