import requests
import json
import time
import os

url = "https://discord.com/api/v9/guilds/355164847652077568/roles/1120033388842192997"
# Retrieve the value of the 'TOKEN' environment variable
array_string = os.getenv('AUTHORIZATION_TOKENS')
tokens_array = array_string.split(',')
using_token_enumerator = 0

decimal_colors = [
    16711680,  # Красный (Red)
    65280,     # Зеленый (Green)
    255,       # Синий (Blue)
    16776960,  # Желтый (Yellow)
    16711935,  # Пурпурный (Purple)
    65535,     # Белый (White)
    8421504,   # Серый (Gray)
    16777215   # Черный (Black)
]
color_enumerator = 0


def change_too_many_requests_response(color_change_response, token_enumerator):
    if color_change_response.status_code == 429:
        token_enumerator += 1
        if token_enumerator == len(tokens_array):
            token_enumerator = 0
        print(f'Changed to using token: {token_enumerator}')
    return token_enumerator


while True:
    headers = {
        'authority': 'discord.com',
        'authorization': f'{tokens_array[using_token_enumerator]}',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json'
    }

    carousel_color_change_payload = json.dumps({
        "name": "Carousel",
        "permissions": "0",
        "color": decimal_colors[color_enumerator],
        "hoist": False,
        "mentionable": False,
        "icon": None,
        "unicode_emoji": None
    })
    demokrat_color_change_payload = json.dumps({
        "name": "DEMOCRAT",
        "permissions": "8804682432511",
        "color": decimal_colors[color_enumerator],
        "hoist": False,
        "mentionable": False,
        "icon": None,
        "unicode_emoji": None
    })

    carousel_color_change_response = requests.request("PATCH", url, headers=headers, data=carousel_color_change_payload)
    carousel_operation_success = carousel_color_change_response.status_code == 200
    color_changed_string = 'Carousel color changed' if carousel_operation_success else 'Carousel color not changed'
    print(f'{color_changed_string}. Status code: {carousel_color_change_response.status_code}')  # Print the response status code
    using_token_enumerator = change_too_many_requests_response(carousel_color_change_response, using_token_enumerator)
    time.sleep(0.5)

    democrat_color_change_response = requests.request("PATCH", url, headers=headers, data=carousel_color_change_payload)
    carousel_operation_success = carousel_color_change_response.status_code == 200
    color_changed_string = 'Democrat color changed' if carousel_operation_success else 'Democrat color not changed'
    print(f'{color_changed_string}. Status code: {carousel_color_change_response.status_code}')
    using_token_enumerator = change_too_many_requests_response(carousel_color_change_response, using_token_enumerator)
    time.sleep(0.5)

    operation_success = carousel_operation_success * carousel_operation_success

    if operation_success:
        color_enumerator += 1
    if color_enumerator == len(decimal_colors):
        color_enumerator = 0
