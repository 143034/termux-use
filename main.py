import os
import time
from face import Interface

from call import Call_tel

from telecop import Telcop

from ctr_torch import torch_ctr
from ctr_vibrate import ctr_vibrate
from ip_catch import ctr_ip

from camera_catch import ctr_camera
if __name__ == "__main__":
    while True:

        opt = Interface()
        if opt == 1:
            #os.system(f"termux-tts-speak -e 'com.xiaomi.mibrain.speech' '通录备份'")
            Telcop()
        elif opt ==2:
            #os.system(f"termux-tts-speak -e 'com.xiaomi.mibrain.speech' '拨打电话'")
            Call_tel()
        elif opt ==3:
            torch_ctr()
        elif opt == 4:
            ctr_vibrate()
        elif opt == 5:
            ctr_camera()
        elif opt == 6:
            ctr_ip()

