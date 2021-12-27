import requests

"""Make a POST request with the following values"""

url1 = 'http://127.0.0.1:5000/services/date-fmt/'
data1 = {"date":"2020-01-01T00:00:00", "days":2}

calculator_request = requests.post(url=url1, json= data1)

print(calculator_request.json())