import os
import subprocess

# Install dependencies at runtime
subprocess.run(["pip", "install", "fastapi", "uvicorn"])

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "DCR API running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
    
