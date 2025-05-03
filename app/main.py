from fastapi import FastAPI
from app.exchange import covert_currency

# Create a FASTAPI INSTANCE 
app = FastAPI()

# FastAPI handles JSON serialization/deserialization 
# use built-in python and pydantic types 
@app.get("/convert")
def convert(from_currency: str, to_currency: str, amount: float):
    result = convert_currency(from_currency, to_currency, amount)
    return{"converted_amount": result}

    