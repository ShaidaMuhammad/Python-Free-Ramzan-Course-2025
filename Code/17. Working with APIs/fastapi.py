from fastapi import FastAPI  

app = FastAPI()  

@app.get("/items/{item_id}")  
def read_item(item_id: int):
    # Code to access item infromation from database
    return {"item_id": item_id} 
