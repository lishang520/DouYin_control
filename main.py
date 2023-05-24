import os,time

if __name__ == '__main__':
    print("[+]正在启动相关程序，请等待...")
    os.system('WssBarrageService.exe')
    time.sleep(3)
    os.system("start cmd /k ; python3 get_message.py")
    time.sleep(2)
    os.system("start cmd /k ; python3 consumer.py")
