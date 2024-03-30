from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict
#add cors
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:*",
    "http://localhost:3000",    
]

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")

def read_root():
    return {"Hello": "World"}

class URL(BaseModel):
    url: str

class Result(BaseModel):
    result: float

@app.post("/checkURL", response_model=Result)
def checkURL(URL: URL):
    url = URL.url
    result = predict(url)
    return {"result": result}