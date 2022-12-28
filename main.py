import sql_functions as func 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Coffee": "&Friends"}

@app.get("/all")
def get_all_shops():
    return func.all_shops()
