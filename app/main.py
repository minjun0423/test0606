from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

API_KEY = "YOUR_API_KEY"  # 서울시 오픈API 키
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

@app.get("/")
def read_root():
    return {"message": "Welcome to Seoul Subway API"}

@app.get("/subway/{station}")
def get_real_time_arrival_info(station: str):
    try:
        url = f"{BASE_URL}/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()

        # 가공된 정보를 담을 리스트
        processed_data = []

        # 각 지하철 도착 정보를 가공
        for arrival_info in data["realtimeArrivalList"]:
            train_line = arrival_info["trainLineNm"]
            arrival_msg = arrival_info["arvlMsg2"]
            station_name = arrival_info["arvlMsg3"]

            # 가공된 정보를 리스트에 추가
            processed_data.append({"train_line": train_line, "arrival_msg": arrival_msg, "station_name": station_name})

        return processed_data
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
