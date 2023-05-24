import redis
import time

loop_sec = 0.5
list_name = 'douyin'

def init_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r

if __name__ == '__main__':
    r = init_redis()
    print("开始监听弹幕消息, loop_sec =", loop_sec)
    while True:
        time.sleep(loop_sec)
        print("等待执行的指令：", r.lrange(list_name, 0, -1))