from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"hello root!1"}

@app.get("/home")
def home():
    return {"message":"home!"}
