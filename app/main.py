from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "서울시 지하철 실시간 도착 정보 API. /subway/{station} 경로를 통해 검색하세요."}

