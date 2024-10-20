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