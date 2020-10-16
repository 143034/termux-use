from others import torch
import time

def torch_ctr():
    print('------------------------')
    print('开[1]  关[2]  闪烁[3]')
    dat = int(input("请输入选择:"))
    if dat == 1:
        torch("on")
    elif dat == 2:
        torch("off")
    else:
        while True:
            torch("on")
            time.sleep(1)
            torch('off')

    print('-------------------------')
