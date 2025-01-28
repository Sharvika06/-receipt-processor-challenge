from fastapi import FastAPI, HTTPException
from models import Receipt
from utils import calculate_points
from database import receipts_db
import uuid

app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt processor that calculates points based on receipt data.",
    version="1.0.0",
    openapi_url="/openapi.json"
)
#Post request
@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    receipts_db[receipt_id] = {"receipt": receipt, "points": points}
    return {"id": receipt_id}

#Get request with Id as parameter
@app.get("/receipts/{id}/points")
def get_points(id: str):
    if id not in receipts_db:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")
    return {"points": receipts_db[id]["points"]}
