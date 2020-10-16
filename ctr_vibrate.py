import time
from others import vibrate



def ctr_vibrate():
    print('---------------------------------')
    print('震动一下[1]   震动好几下[2]')

    dat = int(input("请输入选择:"))
    if dat == 1:
        vibrate('1000')
    else:
        while True:

            vibrate('1000')
    print('--------------------------------')
