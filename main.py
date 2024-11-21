from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

class DataRequest(BaseModel):
    data: List[str]

@app.post("/bfhl")
async def process_data(request: DataRequest):
    data = request.data
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    return {
        "is_success": True,
        "numbers": numbers,
        "alphabets": alphabets,
    }

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}
