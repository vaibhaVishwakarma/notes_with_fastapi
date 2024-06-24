def noteEntity(item)->dict:

    return {"_id":str(item["id"]) ,
             "title":str(item["title"]) ,
              "desc":str(item["desc"]) ,
               "important":item["important"], }

def notesEntity(items)->list:
    return [noteEntity(item) for item in items]