# Hello World API

## Introduction
This project was created to improve the knowledge and basics from technologies like python, javascript,html and learn the principles of HTTP request bettween clien-server.

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
python -m http.server
 ```
to serve the index.html file locally.

## Step 2 - Select the server you would like to use:


#### FastAPI

To star the service go to `/fastapi_proj/app` and run
```
python -m main

This will start the services in
host: 127.0.0.1
port: 8000
```
#### Flask
To star the service go to `/flask_proj` and run

```
python -m main

This will start the services in
host: 127.0.0.1
port: 5000
```


### To know more about the specific services go to the readme files inside the projects