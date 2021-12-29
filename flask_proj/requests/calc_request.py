import requests

"""Make a POST request with the following values"""

url = 'http://127.0.0.1:5000/services/calculator/'
data = {"a":2, "b":4, "op_type": "sum"}

calculator_request = requests.post(url=url, json= data)

if __name__ == "__main__":

    print(calculator_request.json())