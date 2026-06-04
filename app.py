import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/fast")
async def fast_endpoint():
    return {"status": "success", "message": "optimized"}

@app.get("/api/heavy")
async def heavy_endpoint():
    start_time = time.time()
    
    total = 0
    for i in range(5_000_000):
        total += i ^ 2
        
    return {
        "status": "success", 
        "result": total,
        "duration": time.time() - start_time
    }