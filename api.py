import requests
from requests import Response

response: Response = requests.get('https://reqres.in/api/users/2')

print(response.json())
