# Important Note
# Install fastapi and uvicorn by pip install
# Run the file (API server) by command "uvicorn fastapi_example:app --reload"
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Code to access item infromation from database
    return {"item_id": item_id}

@app.get("/")
def index():
    return "API is working!"