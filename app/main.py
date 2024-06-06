@app.get("/")
def read_root():
    return {"message": "Subway Info"}

@app.get("/subway/{station}")
def get_real_time_arrival_info(station: str):
    url = f"{BASE_URL}/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()  # JSON 형식 변환 데이터
        
        processed_data = []  # 데이터 가공
        for arrival_info in data.get("realtimeArrivalList", []):
            processed_data.append(ArrivalInfo(
                열차번호=arrival_info.get("btrainNo", ""),
                호선=arrival_info.get("subwayId", ""),
                상하행선구분=arrival_info.get("updnLine", ""),
                지하철_위치=arrival_info.get("arvlMsg3", ""),
                지하철_도착까지=arrival_info.get("arvlMsg2", "")
            ))
        return processed_data
    except Exception as e:
        return {"error": str(e)}
