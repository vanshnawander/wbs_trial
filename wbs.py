from typing import Optional
from fastapi import  FastAPI , Response , status, HTTPException,Request,Form
from fastapi.params import Body
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="html")

app.mount("/static", StaticFiles(directory="html"), name="static")

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("Signin.html",{"request": request})

@app.post("/submit")
def login_check(request:Request,username:str=Form(...),password:str=Form(...)):
    print(username,password)
    return templates.TemplateResponse("index1.html",{"request": request})

@app.get("/register")
async def register(request:Request):
    return templates.TemplateResponse("Signup.html",{"request": request})

@app.post("/registration")
def create_post(request:Request,fullname: str=Form(...),
    email: str =Form(...),
    college : str=Form(...),
    domain: str=Form(...),
    year:  str =Form(...),
    dob : str =Form(...),
    address : str =Form(...),
    username: str =Form(...),
    password: str =Form(...),
    cpassword: str =Form(...)):

    return templates.TemplateResponse("Signin.html",{"request": request})