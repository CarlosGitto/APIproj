import requests

"""Make a POST request with the following values"""

url2 = 'http://127.0.0.1:8000/services/date-fmt/'
data2 = '{"date":"2020-01-01T00:00:00", "days":2}'

date_request = requests.post(url=url2, data=data2)

if __name__ == "__main__":
    print(date_request.json())