from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Hello Root!"}

@app.get("/Home")
def home():
    return{"message": "Home!"}