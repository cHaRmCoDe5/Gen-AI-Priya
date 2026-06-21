from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import math
import uvicorn
import webbrowser
import threading
import time

app = FastAPI(
    title="Calculator API",
    description="A simple and powerful calculator built with FastAPI",
    version="1.0.0"
)

# Pydantic Models
class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str

class MultiNumberRequest(BaseModel):
    numbers: List[float]
    operation: str

class CalculatorResponse(BaseModel):
    result: float
    operation: str
    message: Optional[str] = None


@app.on_event("startup")
async def startup_event():
    print("\n" + "="*70)
    print("🚀 CALCULATOR API IS RUNNING SUCCESSFULLY!")
    print("="*70)
    print("📍 Local URL: http://127.0.0.1:8000")
    print("📚 API Documentation: http://127.0.0.1:8000/docs")
    print("="*70)
    
    # Auto open browser after a small delay
    def open_browser():
        time.sleep(1.5)  # Give server time to fully start
        webbrowser.open("http://127.0.0.1:8000/docs")
        print("🌐 Browser opened automatically to API Docs! ✅")
    
    threading.Thread(target=open_browser, daemon=True).start()


# ==================== Calculator Endpoints ====================

@app.post("/calculate", response_model=CalculatorResponse)
async def calculate(data: CalculationRequest):
    try:
        ops = {
            "add": lambda x, y: x + y,
            "subtract": lambda x, y: x - y,
            "multiply": lambda x, y: x * y,
            "divide": lambda x, y: x / y if y != 0 else None,
            "power": lambda x, y: x ** y,
            "modulo": lambda x, y: x % y if y != 0 else None,
        }
        
        if data.operation not in ops:
            raise HTTPException(status_code=400, detail="Invalid operation")
        
        result = ops[data.operation](data.num1, data.num2)
        if result is None:
            raise HTTPException(status_code=400, detail="Cannot divide or modulo by zero")
        
        return CalculatorResponse(result=result, operation=data.operation, message="Success")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/calculate/multi", response_model=CalculatorResponse)
async def calculate_multi(data: MultiNumberRequest):
    if not data.numbers:
        raise HTTPException(status_code=400, detail="Numbers list cannot be empty")
    
    try:
        ops = {
            "sum": sum,
            "average": lambda x: sum(x)/len(x),
            "max": max,
            "min": min,
            "product": math.prod
        }
        result = ops[data.operation](data.numbers)
        return CalculatorResponse(
            result=result, 
            operation=data.operation, 
            message=f"Success with {len(data.numbers)} numbers"
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid operation")


# Simple GET routes
@app.get("/add/{a}/{b}")
async def add(a: float, b: float):
    return {"operation": "add", "result": a + b}

@app.get("/subtract/{a}/{b}")
async def subtract(a: float, b: float):
    return {"operation": "subtract", "result": a - b}

@app.get("/multiply/{a}/{b}")
async def multiply(a: float, b: float):
    return {"operation": "multiply", "result": a * b}

@app.get("/divide/{a}/{b}")
async def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"operation": "divide", "result": a / b}


@app.get("/")
async def read_root():
    return {
        "message": "Welcome to Calculator API! 🚀",
        "docs": "http://127.0.0.1:8000/docs"
    }


# Run the app
if __name__ == "__main__":
    uvicorn.run("first_api:app", host="127.0.0.1", port=8000, reload=True)