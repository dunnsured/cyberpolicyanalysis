from fastapi import FastAPI

app = FastAPI(title="Cyber Insurance Analyzer")

@app.get("/")
async def root():
    return {"message": "Cyber Insurance Analyzer API"}