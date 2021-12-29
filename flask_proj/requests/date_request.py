import requests

"""Make a POST request with the following values"""

url = 'http://127.0.0.1:5000/services/date-fmt/'
data = {"date":"2020-01-01T00:00:00", "days":2}

calculator_request = requests.post(url=url, json= data)


if __name__ == "__main__":
    print(calculator_request.json())