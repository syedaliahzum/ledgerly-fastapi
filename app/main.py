from collections import defaultdict
from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Ledgerly", version="1.0.0")
transactions: list[dict] = []

class TransactionInput(BaseModel):
    amount: float = Field(gt=0)
    category: str = Field(min_length=2, max_length=40)
    kind: str = Field(pattern="^(income|expense)$")
    occurred_on: date
    note: str = Field(default="", max_length=160)

@app.get("/health")
def health(): return {"status": "ok", "service": "ledgerly"}

@app.post("/transactions", status_code=201)
def create_transaction(payload: TransactionInput):
    entry = {"id": len(transactions) + 1, **payload.model_dump(mode="json")}
    transactions.append(entry)
    return entry

@app.get("/transactions")
def list_transactions(): return transactions

@app.get("/analytics/monthly")
def monthly_analytics():
    by_category = defaultdict(float)
    for item in transactions:
        if item["kind"] == "expense": by_category[item["category"]] += item["amount"]
    income = sum(item["amount"] for item in transactions if item["kind"] == "income")
    expenses = sum(by_category.values())
    return {"income": income, "expenses": expenses, "balance": income - expenses, "spending_by_category": by_category}
