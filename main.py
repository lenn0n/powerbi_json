from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/data")
def get_data():
  sample_data = [
    {"id": 1, "name": "Lennon", "sales": 450},
    {"id": 2, "name": "Kim", "sales": 1250},
    {"id": 3, "name": "Jury", "sales": 850},
  ]
  return JSONResponse(content=sample_data)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
