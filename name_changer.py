import requests
import json
import time
import os

url = "https://discord.com/api/v9/guilds/355164847652077568/roles/1120033388842192997"
# Retrieve the value of the 'TOKEN' environment variable
token = os.getenv('AUTHORIZATION_TOKEN')

headers = {
    'authority': 'discord.com',
    'authorization': f'{token}',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json'
}

names = ['_biir', '_ikki', '_us', '_tuort', '_bies', '_alta', '_sette', '_agys', '_togus', '_emehegin tut ^^']
names_enumerator = 0

while True:
    # Name changer
    name_change_payload = json.dumps({
        "global_name": names[names_enumerator]
    })

    name_change_response = requests.request("PATCH", url, headers=headers, data=name_change_payload)
    operation_success = name_change_response.status_code == 200
    name_changed_string = f'Name changed to {names[names_enumerator]}' if operation_success else 'Name not changed'
    print(f'{name_changed_string}. Status code: {name_change_response.status_code}')  # Print the response status code
    if operation_success:
        names_enumerator += 1
    if names_enumerator == len(names):
        names_enumerator = 0

    # Delay
    time.sleep(0.2)