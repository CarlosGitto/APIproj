from typing import Dict
from fastapi import FastAPI

from datetime import timedelta

from starlette.responses import RedirectResponse

from . import schemas

from .functions.analizer import analize_func

from fastapi.middleware.cors import CORSMiddleware

from fastapi import HTTPException

app = FastAPI(title="FastAPI Project",
              description="Hello World con FastAPI")

origins = [
    "http://localhost:8000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return RedirectResponse(url="/docs")


@app.post("/services/calculator/")
async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
    """Take two values and a operation type, and return the result"""
    try:
        operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
    except ValueError:
        return HTTPException(422, "Bad input")
    return {"resul": operation_resul}



@app.post("/services/date-fmt")
async def date_calculator(op_input: schemas.ServiceDate) -> Dict:
    """Take a date and a number of days and return the date with them"""


    date_inp = {"date": op_input.date, "days": op_input.days}
    days_inp = date_inp["days"]
    date_outp = date_inp["date"]+ timedelta(days=days_inp)

    return {"date": date_outp}

