from re import template
import time
from fastapi import APIRouter, Request,Form
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from fastapi.templating import Jinja2Templates
from schemas.note import noteEntity , notesEntity
from datetime import datetime
from bson.objectid import ObjectId


note = APIRouter() 
templates = Jinja2Templates(directory = "templates")

async def docFetch():
    startTime = time.time()  
    docs = conn.notes.notes.find()
    newDocs:list=[]
    for doc in docs:
        print(doc)
        newDocs.append({"id":str(doc["_id"]) ,
                         "title":str(doc["title"]),
                         "desc":str(doc["desc"]),
                         "important":doc["important"],
                         })
    print(f"time taken to fetch DOCS : {round(time.time()-startTime,2)} sec")
    print(f"Fetch Succesfull \t \t \t \t \t \t ✅✅✅ {str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}")
    return newDocs[::-1]

@note.get("/",response_class = HTMLResponse)
async def read_item(request : Request):
    
    newDocs = await docFetch()
    if(len(newDocs)==0):return templates.TemplateResponse("index.html" , {"request": request})
    return templates.TemplateResponse("index.html",{"request":request , "documents":newDocs})


@note.post("/")
async def create_item(request:Request):
    form = await request.form()
    #print(form)
    form = dict(form)
    form["important"] = False if "important" in list(form.keys()) else True
    #print(form)
    note = conn.notes.notes.insert_one(form)
    if(note.acknowledged==True): return templates.TemplateResponse("index.html",{"request":request , "documents":docFetch() , "status" : True})
    return templates.TemplateResponse("index.html",{"request":request , "documents":docFetch()})



@note.post("/delete")
async def delete_item(request:Request,button_id: dict ):
    check =conn.notes.notes.delete_one({"_id":ObjectId(button_id["id"])})
    print("unssuccful deleteing the document❌" if not check else "deleted successfuly✅")
    print(button_id["id"])
    return templates.TemplateResponse("index.html",{"request":request , "documents":docFetch()})