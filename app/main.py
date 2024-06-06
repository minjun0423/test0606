from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "427a53796b6d696e37344f6451594a"

@app.get("/")
def read_root():
    return {"message": "서울시 지하철 실시간 도착 정보 API. /subway/{station} 경로를 통해 검색하세요."}

@app.get("/subway/{station}")
def get_subway_info(station: str):
    url = f"http://swopenAPI.seoul.go.kr/api/subway/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
    response = requests.get(url)
    data = response.json()

    if 'errorMessage' in data:
        return {"error": data['errorMessage']['message']}

    results = []
    for item in data['realtimeArrivalList']:
        result = {
            '열차번호': item['trainNo'],
            '지하철호선ID': item['subwayId'],
            '첫번째도착메세지': item['arvlMsg2'],
            '두번째도착메세지': item['arvlMsg3']
        }
        results.append(result)

    return results