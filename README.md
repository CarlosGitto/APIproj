# Hello World API

### Instructions
Your task is to develop an http API that will teach you the basics of building web services.
The project you conduct must be completed twice using two seperate http frameworks in python: flask and fastapi.
Your job is to develop basic functions that conduct specific tasks the are listed below and expose these services through http locally.
Both servers must use the same shared service functions, your code must implement proper seperation of concerns and seperate your service layer from your http layer.
The server must receive requests and respond to request using `JSON` with specific endpoints corresponding to unique individual service functions.

In order to test your API and make sure it works you should write bash scripts that use curl to talk to your API, and python scripts that use the request  library.
Once your app is fully developed you should add unit tests to each endpoint and develop them using the pytest framework.

You are encouraged to read the documentation and also research the best practices used for both Flask and Fastapi when you develop your server.

### Service 1 - Calculator
Create an endpoint at `/services/calculator` that is able to sum, divide, multiply, and subtract two numbers. The incoming JSON must have the following format.
```
{"a":1, "b":2, "operation":"mul" }
```

The output must have the following format:
```
{"result":2}
```

### Service 2 - Date calculator
Create an endpoint at `/services/date-fmt` that is able to take in a json with a ISO formatted date and a days parameter and will return an ISO formatted date with the original date + days.
Input JSON
```
{"date":"2020-01-01T00:00:00", "days":2}
```

The output must have the following format:
```
{"date":"2020-01-03T00:00:00"}
```

Use curl and the python requests library to carefull craft HTTP requests that you can use to talk to and debug your server.



Some helpful links
1. https://refactoring.guru/refactoring
2. https://12factor.net/
3. https://www.restapitutorial.com/
4. https://fastapi.tiangolo.com/
5. https://flask.palletsprojects.com/en/2.0.x/