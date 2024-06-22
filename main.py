from fastapi import FastAPI
from os import environ as env
from src.driver_connect import driver_connect

app = FastAPI()

@app.get("/")
def index():
    return {"details":f"Hello,My special number is = {env['SPECIAL_NUM']}"}

@app.get('/test')
def test_page():
    thing = 'test'
    url = "https://iatse15.unionimpact.com/login"
    def test_scrape():
        driver = driver_connect()
        driver.get(url)
        driver.close()
    test_scrape()    
        

    return {"content":thing}
