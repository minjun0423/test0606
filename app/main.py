from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

API_KEY = "427a53796b6d696e37344f6451594a"  # 서울시 오픈API 키
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

@app.get("/")
def read_root():
    return {"message": "Welcome to Seoul Subway API"}

@app.get("/subway/{station}")
def get_real_time_arrival_info(station: str):
    result = requests.get("{BASE_URL}/{API_KEY}/json/realtimeStationArrival/0/5/{station}")
    return result