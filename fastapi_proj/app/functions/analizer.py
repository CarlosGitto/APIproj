from .divide import divide
from .multiply import multiply
from .subtract import subtract
from .summ import summ
from typing import Dict
from fastapi import HTTPException
"""Analize an argument to know what must do"""

def analize_func(operation : Dict[int,str]) -> int:
    if operation["op_type"] == "mult":
        resul = multiply(a=operation["a"], b=operation["b"])
        return resul
    if operation["op_type"] == "sum":
        resul = summ(a=operation["a"], b=operation["b"])
        return resul
    if operation["op_type"] == "div":
        resul = divide(a=operation["a"], b=operation["b"])
        return resul
    if operation["op_type"] == "diff":
        resul = subtract(a=operation["a"], b=operation["b"])
        return resul
    else:
        raise HTTPException(status_code=400, detail="Invalid operation type header")