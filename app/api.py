from fastapi import APIRouter, WebSocket, WebSocketDisconnect, UploadFile, File
from fastapi.responses import HTMLResponse
from app.templates.html import html
from app.save_files import download_files
from app.websocket import ConnectionManager

chat_router = APIRouter()
manager = ConnectionManager()


@chat_router.get("/")
async def get():
    return HTMLResponse(html)


@chat_router.post("/send_file")
async def save_file(img: list[UploadFile] = File(...)):
    await download_files(img)


@chat_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    await manager.broadcast(f'Client #{client_id} has entered the chat')
    try:
        while True:
            data = await websocket.receive_text()
            data_bytes = await websocket.receive_bytes()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            # ______________________
            await manager.send_files(data_bytes, websocket)
            # ______________________
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f'Client #{client_id} has left the chat')
