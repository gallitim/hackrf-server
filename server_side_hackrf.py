import asyncio
import websockets
import subprocess

async def serve(websocket, path):
    global q_list
    q = asyncio.queue(maxsize=0)
    q_list.append(q)
    while True:
      msg = await queue.get()
      await websocket.send(json.dumps(msg))

start_server = websockets.serve(serve, "127.0.0.1", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
