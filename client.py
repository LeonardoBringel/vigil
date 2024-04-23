import websockets
import asyncio
import psutil
import os

from time import sleep


SERVER_IP = '127.0.0.1'
SERVER_PORT = '8088'
REFRESH_RATE = 2


def get_computer_info():
    cpu_load = psutil.cpu_percent()
    dict(psutil.virtual_memory()._asdict())
    ram_load = psutil.virtual_memory().percent
    disk_load = psutil.disk_usage(r'/').percent
    return cpu_load, ram_load, disk_load


def draw_info_bar(title, load):
    use_bar = ''.join('▮' * int(load/10))
    free_bar = ''.join('▯' * (10 - int(load/10)))
    print(f'{title}: |{use_bar}{free_bar}| {load}%')


async def send_report():
    async with websockets.connect(f'ws://{SERVER_IP}:{SERVER_PORT}') as websocket:
        stats = get_computer_info()
        draw_info_bar('CPU ', stats[0])
        draw_info_bar('RAM ', stats[1])
        draw_info_bar('DISK', stats[2])
        await websocket.send(str(stats))


while True:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_report())

    sleep(REFRESH_RATE)
    os.system('clear')

