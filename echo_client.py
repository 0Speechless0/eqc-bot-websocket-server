import websocket

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://127.0.0.1:5001/websocket")
    print("Sending 'Hello, World'...")
    ws.send("Hello, World")
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print(f"Received '{result}'")
    ws.close()
