import requests
import json
import time
import os

url = "https://discord.com/api/v9/users/@me"
# Retrieve the value of the 'TOKEN' environment variable
token = os.getenv('AUTHORIZATION_TOKEN')

headers = {
  'authority': 'discord.com',
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'authorization': f'{token}',
  'content-type': 'application/json',
  'cookie': '__dcfduid=dc1a8a00708911ecab0f1d4e3b5337ad; __sdcfduid=dc1a8a01708911ecab0f1d4e3b5337ad8e330703bdde082d674c54b028699cac3da9c174047cedbb16e04d4221f3a08f; _ga_XXP2R74F46=GS1.2.1686665568.1.1.1686665634.0.0.0; _gcl_au=1.1.1672655597.1686807504; _ga=GA1.1.1750049057.1686664106; __cfruid=75027cd53ec6d80e4aae1dea0fd70141d69b27bf-1687106453; locale=ru; _ga_Q149DFWHT7=GS1.1.1687106454.2.0.1687106454.0.0.0; OptanonConsent=isIABGlobal=false&datestamp=Mon+Jun+19+2023+01%3A40%3A54+GMT%2B0900+(%D0%AF%D0%BA%D1%83%D1%82%D1%81%D0%BA%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
  'origin': 'https://discord.com',
  'referer': 'https://discord.com/channels/355164847652077568/355164847652077569',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'x-debug-options': 'bugReporterEnabled',
  'x-discord-locale': 'ru',
  'x-discord-timezone': 'Asia/Yakutsk',
  'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InJ1LVJVIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyMDY1NzYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
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
    time.sleep(1)