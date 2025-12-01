from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/api/sensors")
def sensors():
    return ["V1", "V2"]

@app.get("/api/weather/current")
def weather():
    return {"temp": 25}

@app.get("/api/irrigation/status")
def status():
    return {"status": "ok"}

@app.websocket("/ws/sensors/live")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_text("pong")

