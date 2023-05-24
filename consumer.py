import pyautogui
import redis
import time

loop_sec = 0.2
press_sec = 0.5
list_name = 'douyin'
# key_list = ('w', 's', 'a', 'd', 'j', 'k', 'u', 'i', 'z', 'x', 'f', 'enter', 'shift', 'backspace','TAB')
key_list = ('w', 's', 'a', 'd')


def init_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r


def control(key_name):
    # print("key_name =", key_name)
    if key_name == None:
        # print("本次无指令发出")
        return
    key_name = key_name.lower()
    if key_name in key_list:
        # print("发出指令", key_name)
        print("\033[发出指令:{}\033[0m".format(key_name))
        pyautogui.keyDown(key_name)

        # if key_name == 'a' or key_name == 'd':a
        #     print("发出指令w")
        #     pyautogui.keyDown('w')

        time.sleep(press_sec)
        pyautogui.keyUp(key_name)

        # if key_name == 'a' or key_name == 'd':
        #     print("发出指令w")
        #     pyautogui.keyUp('w')

        print("结束指令", key_name)


if __name__ == '__main__':
    r = init_redis()
    print("开始监听弹幕消息, loop_sec =", loop_sec)
    while True:
        key_name = r.lpop(list_name)
        r.delete(list_name)
        control(key_name)
        time.sleep(loop_sec)
