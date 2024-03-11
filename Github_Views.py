import requests

url = "https://camo.githubusercontent.com/e56208901fe7ccdea417df2de33c29abe38b94d6041981e667ae714126e4fa15/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d616b6164656570657368266c6162656c3d50726f66696c65253230566965777326636f6c6f723d6c6967687467726579267374796c653d666f722d7468652d6261646765"
for _ in range(100):  # number of views you want to add
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to access {url}")
    else:
        print(f"{_+1} views added")
