from fastapi import FastAPI
from os import environ as env

app = FastAPI()

@app.get("/")
def index():
    return {"details":f"Hello,My special number is = {env['SPECIAL_NUM']}"}

@app.get('/test')
def test_page():
    return {"content":"This is the test end point"}
