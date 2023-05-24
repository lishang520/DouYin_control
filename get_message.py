import asyncio,json
import websockets
import asyncio
import redis

list_name = 'douyin'
# key_list = ('w', 's', 'a', 'd', 'j', 'k', 'u', 'i', 'z', 'x', 'f', 'enter', 'shift', 'backspace')
key_list = ('w', 's', 'a', 'd')  #接收的指令白名单

def init_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r


async def process():

    async with websockets.connect("ws://127.0.0.1:8888/",ping_interval=None) as ws:  #ping_interval=None 是为了防止sockets断开
        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=30)
                # print('Received: ' + message)
                # print(message)
                message = json.loads(message)
                # print(  message )

                if message.get("Type") == 1:
                    Data = json.loads(message.get("Data"))
                    speak_message = Data.get("Content")
                    list_str = list(speak_message)
                    print("弹幕拆分:", list_str)
                    for char in list_str:
                        if char.lower() in key_list:
                            print('推送队列：', char.lower())
                            r = init_redis()

                            char_l = char.lower()

                            r.rpush(list_name,char_l)

            except asyncio.TimeoutError as e:
                continue
            except websockets.exceptions.ConnectionClosed as e:
                print('连接已经关闭')
                print(e)
                continue

asyncio.run(process())


