from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/data")
def get_data():
  sample_data = [
    {"id": 1, "name": "Lennon", "sales": 450},
    {"id": 2, "name": "Kim", "sales": 1250},
    {"id": 3, "name": "Jury", "sales": 850},
  ]
  return JSONResponse(content=sample_data)
