from fastapi import FastAPI, HTTPE Exception
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    account_number: str
    amount: float
    currency: str   

@app.post("/payments")
def create_payment(payment: Payment):
    if payment.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")
    return {
        "account_number": payment.account_number,
        "amount": payment.amount,
        "currency": payment.currency,
        "message": "Payment created successfully",  
        "status": "success"
    }
