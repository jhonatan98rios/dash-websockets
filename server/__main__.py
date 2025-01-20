from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

# Store active WebSocket connections
connected_clients: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the WebSocket connection
    await websocket.accept()
    # Add the client's WebSocket to the connected_clients list
    connected_clients.append(websocket)
    try:
        while True:
            # Receive a message from the client
            data = await websocket.receive_text()
            # Broadcast the message to all connected clients except the sender
            for client in connected_clients:
                if client != websocket:
                    await client.send_text(data)
    except WebSocketDisconnect:
        # Remove the client from the list when the connection closes
        connected_clients.remove(websocket)
        print("Client disconnected")
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)