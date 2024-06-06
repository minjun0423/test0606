from fastapi import FastAPI#, HTTPException
#import requests

app = FastAPI()

API_KEY = "427a53796b6d696e37344f6451594a"  # 서울시 오픈API 키
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

@app.get("/")
def read_root():
    return {"message": "Welcome to Seoul Subway API"}
"""
@app.get("/subway/{station}")
def get_arrivalinfo(station: str):
    try:
        url = f"{BASE_URL}/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json() #JSON 형식 변환 데이터
        
        processed_data = [] # 데이터 가공
        for arrival_info in data["realtimeArrivalList"]:
            station = arrival_info["statnNm"]
            train_line = arrival_info["trainLineNm"] #도착지 방면
            arvlMsg2 = arrival_info["arvlMsg2"] #첫번째도착메세지, (도착, 출발 , 진입 등)
            arvlMsg3 = arrival_info["arvlMsg3"] #두번째도착메세지, (종합운동장 도착, 12분 후 (광명사거리) 등)
            updownline = arrival_info["updnLine"]
            barvlDt = arrival_info["barvlDt"]
            btrainNo = arrival_info["btrainNo"]
            subwayId = arrival_info["subwayId"]
            #ordkey = arrival_info["ordkey"]

            processed_data.append({
                "열차번호": btrainNo,
                "호선": subwayId,
                "상하행선구분": updownline,
                "지하철 위치": arvlMsg3,
                "지하철 도착까지": arvlMsg2
            })
        return [station] + processed_data
    
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))"""