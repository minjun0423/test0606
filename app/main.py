from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# 서울시 지하철 실시간 도착정보 Open API 키
API_KEY = 'YOUR_API_KEY'

@app.get("/")
def read_root():
    return {"message": "서울시 지하철 실시간 도착 정보 API. /subway/{station} 경로를 통해 검색하세요."}

