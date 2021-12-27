import requests

"""Make a POST request with the following values"""

url1 = 'http://127.0.0.1:8000/services/calculator/'
data1 = '{"arg1":2, "arg2":4, "op_type": "sum"}'

calculator_request = requests.post(url=url1, data= data1)


if __name__ == "__main__":
    print(calculator_request.json())