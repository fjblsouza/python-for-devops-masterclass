import requests

def api_check():
    url = "http://172.10.10.1"
    response = requests.get(url)
    if response.status_code == 200:
        return "UP and running"
    else:
        return "DOWN and not running"

print(api_check())

 







