import socketio
import asyncio

sio_client = socketio.AsyncClient()

@sio_client.event
async def connect():
    print('cleinte: connectado')

@sio_client.event
async def disconnect():
    print('cleinte: desconectado')

async def main():
  await sio_client.connect(url='http://127.0.0.1:8000', socketio_path='sio/sockets')
  await sio_client.disconnect()

asyncio.run(main())
