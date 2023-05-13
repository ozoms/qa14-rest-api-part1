import requests
from pytest_voluptuous import S
from requests import Response
from schemas import user
from voluptuous import Schema


def test_get_users():
    response: Response = requests.get('https://reqres.in/api/users/2')

    print(response.status_code)

    assert response.status_code == 200


def test_get_users_schema():
    response: Response = requests.get('https://reqres.in/api/users/2')

    assert S(user.single_user_schema) == response.json()
