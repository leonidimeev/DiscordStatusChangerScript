import requests
import json
import time
import os

url = "https://discord.com/api/v9/guilds/355164847652077568/roles/1120033388842192997"
# Retrieve the value of the 'TOKEN' environment variable
array_string = os.getenv('AUTHORIZATION_TOKENS')
tokens_array = array_string.split(',')
using_token_enumerator = 0

colors = [1752220, 1000220, 1750020, 2752220]
color_enumerator = 0

while True:
    headers = {
        'authority': 'discord.com',
        'authorization': f'{tokens_array[using_token_enumerator]}',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json'
    }

    # Color changer
    color_change_payload = json.dumps({
        "name": "Carousel",
        "permissions": "0",
        "color": colors[color_enumerator],
        "hoist": False,
        "mentionable": False,
        "icon": None,
        "unicode_emoji": None
    })
    color_change_response = requests.request("PATCH", url, headers=headers, data=color_change_payload)
    operation_success = color_change_response.status_code == 200
    color_changed_string = 'Color changed' if operation_success else 'Color not changed'
    print(f'{color_changed_string}. Status code: {color_change_response.status_code}')  # Print the response status code
    if operation_success:
        color_enumerator += 1
    if color_enumerator == len(colors):
        color_enumerator = 0

    if color_change_response.status_code == 429:
        using_token_enumerator += 1
        if using_token_enumerator == len(tokens_array):
            using_token_enumerator = 0
        print(f'Changed to using token: {using_token_enumerator}')

    # Delay
    time.sleep(0.5)