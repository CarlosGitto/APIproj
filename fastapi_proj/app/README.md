## Introduction
This directory contains two services, one to make basic calculations and another to add a number of days to a given date

## First endpoint - Calculator
The endpoint at `/services/calculator` is able to sum, divide, multiply, and subtract two numbers. The incoming JSON must have the following format.
```
{"a":1, "b":2, "operation":"mul" }
```

The output will have the following format:
```
{"result":2}
```

## Second endpont - Date calculator
The endpoint at `/services/date-fmt` is able to take in a json with a ISO formatted date and a days parameter and will return an ISO formatted date with the original date + days.
Input JSON

```
{"date":"2020-01-01T00:00:00", "days":2}
```

The output will have the following format:
```
{"date":"2020-01-03T00:00:00"}
```

## Details

Both endpoint receive HTTP POST request only

