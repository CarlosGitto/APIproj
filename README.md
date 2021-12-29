# Hello World API

## Introduction
The task is to develop an http API that will teach you the basics of building web services. The project must be completed twice using two seperate http frameworks in python: Flask and Fastapi. The job is to develop basic functions that conduct specific tasks the are listed below and expose these services through http locally. Both servers must use the same shared service functions, the code must implement proper seperation of concerns and seperate the service layer from the http layer. The server must receive requests and respond to request using JSON with specific endpoints corresponding to unique individual service functions.

## Description
This is a project that contains two apis, one develop with FastAPI framework and another with Flask framework.
Both of them can offer same services trough the same functions and paths.

Also contains an html and a javascript file that their only propouse is to connect and test the services from both apis.

## Requirements
Please be sure to have `python 3.10.0` to run this project and read the `requirements.txt` or just do
```
python -m pip install -r ./requirements.txt
```
to proceed.

##  Get Started

## Step 1 

Inside the shell located at `/clientcode` directory run 
```
python run.py <port[Optional]>
 ```
`default port` -> [8888]

This serve the index.html file locally.


## Step 2 - Select the server you would like to use:


#### FastAPI

To star the service go to `/fastapi_proj/app` and run
```
python -m main
```
This will start the services in
host: 127.0.0.1
port: 8000

#### Flask
To star the service go to `/flask_proj` and run

```
python -m main
```
This will start the services in
host: 127.0.0.1
port: 5000


## Step 3 - Send requests or curls
 There are 3 ways of send requests in this project

### First way - By web submit
```
Fill the empty spaces on the web serve in STEP 1 and make a submit on the web page that is locally running
```
### Second way - By using request library
 Make a request using request library from python:

 Using a shell go to the directory:

    flask_proj/requests <-or-> fastapi_proj/requests

 Make sure that you have modified the default values in `data` variable on `calc_request.py` and `date_request.py`
 inside the directory.

 Then run the following command:
```
python -m calc_request

or

python -m date_request
```

### Third way - By using curl command

### For calculator service:
Open a CLI and run 
 ```
 curl -X 'POST' 'http://127.0.0.1:5000/services/calculator' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"arg1": <arg1>, "arg2": <arg2>, "op_type": <op_type>}'
```
First Value -> [arg1] -> `real number`

Second Value -> [arg2] -> `real number`

Operation between -> [op_type] ->`("sum", "mult", "div", "diff")`

### For date_calculator service
Open a CLI and run 
 ```
 curl -X 'POST' 'http://127.0.0.1:5000/services/date-fmt' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"date": <date>, "days": <days>}'
```
Date Value -> [date] -> `isoformat`

Days Value -> [days] -> `float`


## Step 4 - testing
You can make a test of the apis by using `pytest`.
In a shell go to the directory
```
/flask_proj
or
/fastapi_proj
```
Then run
```
python -m pytest
```
## To know more about the specific services go to the readme files inside the projects

