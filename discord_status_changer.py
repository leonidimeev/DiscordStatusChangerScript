# -*- coding: UTF-8 -*-
import json
import requests
from timeloop import Timeloop
from datetime import timedelta, datetime
from sys import argv
import os
import time

script_mode = argv
print(script_mode[1])

tl_status_icon_changer = Timeloop()

url = "https://discord.com/api/v9/users/@me/settings"
status_text_set = ["waiting for ban", "waiting for ban.", "waiting for ban..", "waiting for ban..."]

loading_points = ["", ".", "..", "..."]

# Retrieve the value of the 'TOKEN' environment variable
token = os.getenv('AUTHORIZATION_TOKEN')


headers = {
    'authority': 'discord.com',
    'authorization': f'{token}',
    'content-type': 'application/json',
}

# region status_icon_changer
status_set = ["online", "idle", "dnd"]
status_selector = 0
@tl_status_icon_changer.job(interval=timedelta(seconds=0.1))
def status_change():
    global status_selector, default_switcher
    payload = json.dumps({
        "status": status_set[status_selector]
    })
    response = requests.request("PATCH", url, headers=headers, data=payload)
    status_selector += 1
    if status_selector == 3:
        status_selector = 0


# endregion


# region default with ticker
tl = Timeloop()
text_selector = 0
default_switcher = 0
ticker_selector = 0
default_switcher_counter = 0
ticker_set = ["⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀T",
              "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀TH",
              "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀THE",
              "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀THE ",
              "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀THE E",
              "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀THE EN",
              "⠀⠀⠀⠀⠀⠀⠀⠀⠀THE END",
              "⠀⠀⠀⠀⠀⠀⠀⠀THE END ",
              "⠀⠀⠀⠀⠀⠀⠀THE END O",
              "⠀⠀⠀⠀⠀⠀THE END OF",
              "⠀⠀⠀⠀⠀THE END OF ",
              "⠀⠀⠀⠀THE END OF T",
              "⠀⠀⠀THE END OF TH",
              "⠀⠀THE END OF THE",
              "⠀THE END OF THE W",
              "THE END OF THE WO",
              "HE END OF THE WOR",
              "E END OF THE WORL",
              " END OF THE WORLD",
              "END OF THE WORLD ",
              "ND OF THE WORLD I",
              "D OF THE WORLD IS",
              " OF THE WORLD IS ",
              "OF THE WORLD IS N",
              "F THE WORLD IS NE",
              " THE WORLD IS NEA",
              "THE WORLD IS NEAR",
              "HE WORLD IS NEAR ",
              "E WORLD IS NEAR  ",
              " WORLD IS NEAR   ",
              "WORLD IS NEAR    ",
              "ORLD IS NEAR     ",
              "RLD IS NEAR      ",
              "LD IS NEAR       ",
              "D IS NEAR        ",
              " IS NEAR         ",
              "IS NEAR          ",
              "S NEAR           ",
              " NEAR            ",
              "NEAR             ",
              "EAR              ",
              "AR               ",
              "R                ",
              "                 "]

@tl.job(interval=timedelta(seconds=0.5))
def tl_status_text_change():
    global text_selector, default_switcher, ticker_selector, default_switcher_counter
    if default_switcher == 0:
        payload = json.dumps({
            "custom_status": {
                "text": datetime.now().strftime("%H:%M:%S") + ' ' + status_text_set[text_selector],
                "expires_at": '2023-03-15T20:21:03.000Z',
                "status": status_set[status_selector]
            }
        })
        text_selector += 1
        if text_selector == 4:
            text_selector = 0
            default_switcher_counter += 1
        if default_switcher_counter == 10:
            default_switcher = 1
            default_switcher_counter = 0
    else:
        payload = json.dumps({
            "custom_status": {
                "text": ticker_set[ticker_selector],
                "expires_at": '2023-03-15T20:21:03.000Z'
            }
        })
        ticker_selector += 1
        if ticker_selector == len(ticker_set):
            ticker_selector = 0
            default_switcher = 0

    requests.request("PATCH", url, headers=headers, data=payload)
# endregion


# region poop
status_smoke_away_selector = 0
status_smoke_away_timer = 0
tl_poop = Timeloop()
@tl_poop.job(interval=timedelta(seconds=0.5))
def tl_poop_status_text_change():
    global text_selector, status_smoke_away_selector, status_smoke_away_timer
    payload = json.dumps({
        "custom_status": {
            "text": 'Pooping ' + '[' + str(status_smoke_away_timer // 60) + ':' + str(
                status_smoke_away_timer % 60) + '] ' + loading_points[status_smoke_away_selector],
            "expires_at": '2023-03-15T20:21:03.000Z',
            "status": status_set[status_selector]
        }
    })
    requests.request("PATCH", url, headers=headers, data=payload)
    status_smoke_away_timer += 1
    status_smoke_away_selector += 1
    if status_smoke_away_selector == 4:
        status_smoke_away_selector = 0
    text_selector += 1
    if text_selector == 4:
        text_selector = 0
# endregion



if __name__ == "__main__":
    tl_status_icon_changer.start(block=False)
    if script_mode[1] == "smoke":
        tl_poop.start(block=True)
    else:
        tl.start(block=True)
