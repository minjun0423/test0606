from fastapi import FastAPI, HTTPException
#import requests

app = FastAPI()

API_KEY = "427a53796b6d696e37344f6451594a"  # 서울시 오픈API 키
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

@app.get("/")
def read_root():
    return {"message": "Welcome to Seoul Subway API"}

@app.get("/subway/{station}")
def get_arrivalinfo(station: str, api_key: str = API_KEY, base_url: str = BASE_URL):
    url = f"{base_url}/{api_key}/json/realtimeStationArrival/0/5/{station}"
    result = requests.get(url)
    return result.json()