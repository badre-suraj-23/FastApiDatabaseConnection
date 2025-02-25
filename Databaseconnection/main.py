from fastapi import FastAPI,Depends,HTTPException
from database import  Base,SessionLocal,engine
from models import Users
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.responses import JSONResponse


Base.metadata.create_all(bind=engine) # This line Connect Your Models into Database, 

def get_db(): 
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""  This class Schema Used to Tables Data Convert into Json Format Or Any Other Format
  As per Your Requirement """
class UserScheema(BaseModel): # get Method Schema
    id:int
    name:str
    email:str
    class config:
        orm_mode = True 

#------------⬇ Post class Method  Schema ⬇ -----------------
class UserCreatSchema(UserScheema):
    password:str

app=FastAPI()
#------------⬇  Retrive method(get) ⬇ -------------------
@app.get("/users",response_model=list[UserCreatSchema]) 
def get_users(db:Session=Depends(get_db)):
    return db.query(Users).all() # This line Create databasese query and Fetch All Models

#---------------⬇  Create Method(post) ⬇ ------------------
@app.post("/users",response_model=UserScheema) # post Method Create a User
def post_Create_users(user:UserCreatSchema,db:Session=Depends(get_db)):
    u = Users(name=user.name,email=user.email,password=user.password)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

#---------------⬇  Update Method(put) ⬇ -----------------
@app.put("/users/{user_id}",response_model=UserScheema)
def update_user(user_id:int,user:UserScheema,db:Session=Depends(get_db)):
    try:
        u=db.query(Users).filter(Users.id==user_id).first()
        u.name == user.name
        u.email == user.email
        db.add(u)
        db.commit()
        return u
    except:
        return HTTPException(status_code=404,detail="user not found!")
    
#-----------⬇ Delete Method ⬇ -------------------------------
@app.delete("users/{user_id}",response_class=JSONResponse)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Users).filter(Users.id==user_id).first
        db.delete
        return{f"user of id {user_id} has been deleted":True}
    except:
        return HTTPException(status_code=404,detail="user not found!")




