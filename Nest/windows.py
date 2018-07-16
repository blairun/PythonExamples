# alert when outside temp crosses indor nest temp


import http.client

conn = http.client.HTTPSConnection("developer-api.nest.com")

headers = {
    'content-type': "application/json",
    'authorization': "Bearer c.OTYIGjtBz9UZW0l9RcvRGft5sCdLXhJcJ79qtvkJtCz5zktTtbCsDSYRmcK2bVAIRcuiLKRGg8fnISuLaKMCYhnyKO8vVXcxQNYsiyYUYiyulLhr66fEJ0Eqwf3J3otnrVjoARuG4awnNwjl",
    'cache-control': "no-cache",
    'postman-token': "5f2774a4-86e7-1874-9229-5c5549c031e9"
    }

conn.request("GET", "/devices/thermostats/1J-5oJnNxJqtgPREmLCicMrSiXEikx2Y/ambient_temperature_f", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

###################

import requests

url = "https://developer-api.nest.com/devices/thermostats/1J-5oJnNxJqtgPREmLCicMrSiXEikx2Y/ambient_temperature_f"

headers = {
    'content-type': "application/json",
    'authorization': "Bearer c.OTYIGjtBz9UZW0l9RcvRGft5sCdLXhJcJ79qtvkJtCz5zktTtbCsDSYRmcK2bVAIRcuiLKRGg8fnISuLaKMCYhnyKO8vVXcxQNYsiyYUYiyulLhr66fEJ0Eqwf3J3otnrVjoARuG4awnNwjl",
    'cache-control': "no-cache",
    'postman-token': "ddff0dd1-33e7-1f93-7fa5-26c83d3de623"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)