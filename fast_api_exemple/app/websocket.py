from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    # ______________________
    async def send_files(self, data: bytes, websocket: WebSocket):
        await websocket.send_bytes(data)

    # ______________________
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
