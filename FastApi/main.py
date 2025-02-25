from fastapi import FastAPI,Query,Form,File,UploadFile,HTTPException,Depends
from typing import Optional,List
from enum import Enum
from pydantic import BaseModel

class ModelName(str, Enum):
    Suraj = "suraj"
    mayur = "mayur"
    sanket = "sanket"

class Item(BaseModel):
    name: str
    description: str
    salary: float
    location: float 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":'Suraj' "World"}


@app.get("/suraj")
def read_root():
    return {"Hello":"I Am  a python Developer"}

#--------⬇ How to Create Path parameter ⬇------------

@app.get("/item{Item}")
def path_func(Item):
    var_name = {"path variable" :Item}
    return(var_name)

#--------------⬇ How to Create Query parameter ⬇----------

@app.get("/qr")
def query_func(
    name: str | None = Query(default=None, max_length=25) ,
    roll_no: str | None = Query(default=None, max_length=3) ,
    extra_info: str | None = Query(default=None, max_length=50) 
):
    return {"name": name, "roll_no":roll_no, "extra_info": extra_info}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.sanket:
        return {"model_name": model_name, "message":"i am electrical eng"}

    if model_name.value == "mayur":
        return {"model_name": model_name, "message": "Thank You For Visit Repo"}
    
    else:
     return {"model_name": model_name, "message": "Python Developer"}

#----------⬇ How to Create request body ⬇------------

@app.post("/items/")
async def create_item(item: Item):
    return item

#----------⬇ form data ⬇---------------------------

@app.post("/form/data")
async def form_data(username:str=Form(),password:int=Form()):
    return {"username":username ,"password":password}

#------------⬇ file uploads ⬇-------------------
@app.post("/file/data")
async def file_bytes_len(file:bytes=File()):
    return {"file":len(file)}

@app.post("/file/upload")
async def file_upload(file:UploadFile):
    return {"file_name":file.filename,"file_content":file.content_type}

@app.post("/file/upload")
async def file_upload(file:UploadFile):
    return {"file_name":file.filename,"file_content":file.content_type}

@app.post("/formdata/filedata")
async def formdat_upload_file(file1:UploadFile,file2:bytes=File(),name:str=Form()):
    return {"file_name":file1.filename,"file_bytes":len(file2),"name":name}

#------------⬇ How to Handle Http exception ⬇--------------

items = [1,2,3,4,5]
@app.post("/error/handlig")
async def handle_error(item:int):
    if item not in items:
        return HTTPException(status_code=404,detail="Item Not Found Please Enter Valid Input")
    return{"value":item}

#---------⬇ How to Create Dependency injection ⬇-----------

# Create Dependency injection With function
async def common_param(q: str | None = None, skip: int = 0, limit: int = 10):
   return {"q":q,"skip":skip,"limit":limit}

class common_param: # Create Dependency injection With Class
   def __init__(self,q: str=10, skip: int = 10, limit: int = 10):
      self.q = q
      self.skip = skip
      self.limit =limit

@app.get("/")
async def read_items(commons:dict = Depends(common_param)):
   res = {}
   return commons.q+commons.skip+commons.limit+commons


@app.get("/items")
async def read_items(commons:dict = Depends(common_param)):
   return commons

@app.get("/users")
async def get_users(commons:dict = Depends(common_param)):
   return commons

# -----------------⬇ Database sqlite Connection ⬇-------------------------

from database import Base, engine, SessionLocal
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from sqlalchemy.orm import Session

# -----------------⬇ Database sqlite onection ⬇-------------------------

#-----------⬇ Models ⬇------------ 
class User(Base): 
    __tablename__ = "users"  
    id = Column(Integer, primary_key=True, index=True)  
    email = Column(String, unique=True, index=True)  
    is_active = Column(Boolean, default=True) 

#-------------⬇  Schema ⬇ ---------
class UserSchema(BaseModel):
    id:int 
    email:str 
    is_active:bool

class config:
    orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine) 

@app.post("/users",response_model=UserSchema)
def index(user:UserSchema,db:Session=Depends(get_db)):
    u=User(email =user.email,is_active=user.is_active,id=user.id)
    db.add(u)
    db.commit()
    return u
#-----------⬇ db work to put data into db ⬇ ---------

@app.get("/users",response_model=List[UserSchema])
def index(db:Session=Depends(get_db)):
    return db.query(User).all()

