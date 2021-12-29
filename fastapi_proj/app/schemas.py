from pydantic import BaseModel
import datetime

"""Establishes the input format"""

class ServiceCalculator(BaseModel):
    arg1 : int
    arg2 : int
    op_type : str

class ServiceDate(BaseModel):
    date : datetime.datetime
    days : float