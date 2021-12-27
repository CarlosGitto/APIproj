import requests

"""Make a POST request with the following values"""

url1 = 'http://127.0.0.1:5000/services/calculator/'
data1 = {"a":2, "b":4, "op_type": "sum"}

calculator_request = requests.post(url=url1, json= data1)

print(calculator_request.json())