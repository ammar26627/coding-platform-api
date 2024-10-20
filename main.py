from fastapi import FastAPI
from enum import Enum
 
# Create a FastAPI application
app = FastAPI()
 
class Model(str,Enum):
 name="name"
 pas="qere"


# Define a route at the root web address ("/")
@app.get("/getitems/{itemid}")
def read_root(itemid : Model):
    if itemid == Model.name:
        return {"itemid": Model.name}
    else:
       return{'itemid':Model.pas}
    
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]