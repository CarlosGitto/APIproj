from typing import Dict
from fastapi import FastAPI

from datetime import timedelta

from starlette.responses import RedirectResponse

from . import schemas

from .functions.analizer import analize_func

app = FastAPI(title="FastAPI Project",
              description="Hello World con FastAPI")


@app.get("/")
async def main():
    return RedirectResponse(url="/docs")


@app.post("/services/calculator/")
async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
    """Take two values and a operation type, and return the result"""
    
    operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
    return {"result": operation_resul}



@app.post("/services/date-fmt")
async def calculator(op_input: schemas.ServiceDate) -> Dict:
    """Take a date and a number of days and return the date with them"""

    date_inp = {"date": op_input.date, "days": op_input.days}
    days_inp = date_inp["days"]
    date_outp = date_inp["date"]+ timedelta(days=days_inp)

    return {"date": date_outp}

