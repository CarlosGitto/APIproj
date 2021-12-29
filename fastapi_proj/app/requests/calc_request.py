import requests

"""Make a POST request with the following values"""

url = 'http://127.0.0.1:8000/services/calculator/'
data = '{"arg1":2, "arg2":4, "op_type": "sum"}'

calculator_request = requests.post(url=url, data= data)


if __name__ == "__main__":
    print(calculator_request.json())