from pydantic import errors


from fastapi import FastAPI, HTTPException

def divide(a: int, b: int) -> int or str:
    """
    Take 2(two) arguments and return the product between them
    """
    if b != 0:
        return a/b
    else:
        return "Error detected, you can't use 0 as divider"