from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class payment(BaseModel):
    account_number: str
    amount: float
    currency: str

class customer(BaseModel):
    name: str
    email: str  
    status: str | None = "active"

class account(BaseModel):
    account_number: str
    balance: float
    status: str | None = "active"
    

@app.post("/payments")
def create_payment(payment: payment):
    if payment.amount <= 0:
        return {"error": "Amount must be greater than zero"}
    return {
        "account_number": payment.account_number,
        "amount": payment.amount,
        "currency": payment.currency,
        "message": "Payment created successfully",  
        "status": "success"
    }





@app.get("/")
def home():
    return {"message": "Welcome to Banking API"}


@app.get("/account/{account_number}")
def get_account(account_number: str):
    return {
        "account_number": account_number,
        "balance": 10000,
        "status": "active"
    }

@app.get("/customer/{customer_id}")
def get_customer(customer_id: str):
    return {
        "customer_id": customer_id,
        "name": "sai",
        "email": "sai@example.com",
        "status": "active"
    }

@app.get("/payments")
def get_payments(status: str | None = None):
    return {
        "filter_status": status
    }

@app.post("/customer")
def create_customer(name: str, email: str):
    return {
        "name": name,
        "email": email,
        "message": "Customer created successfully"
    }

@app.patch("/account/{account_number}")
def update_account(account_number: str, balance: float):
    return {
        "account_number": account_number,
        "new_balance": balance,
        "message": "Account updated successfully"
    }

@app.delete("/customer/{customer_id}")
def delete_customer(customer_id: str):
    return {
        "customer_id": customer_id,
        "status": "deleted",
        "message": "Customer deleted successfully"
    }

@app.put("/payments/{payment_id}")
def update_payment(payment_id: str, payment: payment):  
    if payment.amount <= 0:
        return {"error": "Amount must be greater than zero"}
    return {
        "payment_id": payment_id,
        "account_number": payment.account_number,
        "amount": payment.amount,
        "currency": payment.currency,
        "message": "Payment updated successfully",  
        "status": "success"
    }
