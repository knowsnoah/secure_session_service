from fastapi import FastAPI

app = FastAPI(title="secure session service")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

