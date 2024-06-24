from dotenv import load_dotenv
load_dotenv() #loades .\.env file 
from urllib.parse import quote_plus
from pydantic import BaseModel
from fastapi import FastAPI , Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates  
from pymongo import MongoClient
import os
import time
app = FastAPI()
#not need getenv now works porperly
def uriFetch(user:str , pwd:str):
    uriParts=[f"mongodb+srv://{os.getenv(user)}:{os.getenv(pwd)}" ,"mongoyt.sckuliy.mongodb.net" ]
    return f"{quote_plus(uriParts[0])}@{uriParts[1]}" #quote_plus is kindof nessesary to implemen
startTime=time.time()
conn = MongoClient(str(os.getenv("uri")))
print(f"it took {round(time.time() - startTime ,2 )} sec to establish connection to DB")
app.mount("/static",StaticFiles(directory = "static"),name="static") #inroduces this folder to the page
templates = Jinja2Templates(directory = "templates")




