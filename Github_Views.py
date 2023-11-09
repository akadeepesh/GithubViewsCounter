# import webbrowser
# import time
# import pyautogui as pg
# for i in range(101):
#     webbrowser.open('https://github.com/akadeepesh')
#     time.sleep(0.5)
#     if i%10==0:
#         for j in range(10):
#             pg.hotkey('ctrl', 'w')
import requests

url = 'https://camo.githubusercontent.com/30d8742078eeef247f0ed65c2a45cc9e55d7970cc5b038ad7b1551eaa6c72be2/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d616b6164656570657368266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174'
for _ in range(10):  # number of views you want to add
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Failed to access {url}')
