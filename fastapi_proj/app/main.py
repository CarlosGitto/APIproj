from typing import Dict
from fastapi import FastAPI

from datetime import timedelta

from starlette.responses import RedirectResponse

import schemas

from functions.analizer import analize_func

from fastapi.middleware.cors import CORSMiddleware

from fastapi import HTTPException

import uvicorn

app = FastAPI(title="FastAPI Project",
              description="Hello World con FastAPI")

# origins = [
#     "http://localhost:8000",
#     "http://localhost:8080",
#     "http://localhost:8888"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")

async def main():
    return RedirectResponse(url="/docs")


@app.post("/services/calculator/")
async def calculator(op_input: schemas.ServiceCalculator) -> Dict:
    """
    Take a json input with 3 values:
    arg1, agr2 and operation_type
    then return the result in a json format
    """
    try:
        operation_resul = analize_func({"a": op_input.arg1, "b":op_input.arg2, "op_type": op_input.op_type})
    except ValueError:
        return HTTPException(422, "Bad input")
    return {"resul": operation_resul}



@app.post("/services/date-fmt")
async def date_calculator(op_input: schemas.ServiceDate) -> Dict:
    """
    Take a date isoformat
    and a number of days and return 
    the date with them
    """
    date_inp = {"date": op_input.date, "days": op_input.days}
    days_inp = date_inp["days"]
    date_outp = date_inp["date"]+ timedelta(days=days_inp)

    return {"date": date_outp}

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", host="127.0.0.1", port=8000, reload=True)