from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.note import note
app=FastAPI()

app.mount("/static",StaticFiles(directory = "static"),name="static") #introduces this folder to the page

app.include_router(note)
 