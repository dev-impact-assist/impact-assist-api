from fastapi import FastAPI
from os import environ as env
from src.helper_functions.driver_connect import driver_connect

from selenium.webdriver.common.by import By

app = FastAPI()

@app.get("/")
def index():
    return {"details":f"Hello,My special number is = {env['SPECIAL_NUM']}"}

my_pass= env['MY_PASS']
@app.get('/test')
def test_page():
    thing = 'test'
    url = "https://iatse15.unionimpact.com/login"
    def test_scrape():
        driver = driver_connect(True)
        driver.get(url)
        page_data = driver.page_source.encode("utf-8")
        print(page_data)
        driver.close()
        return page_data
    # test_scrape()    
        

    return {"content":test_scrape()}


