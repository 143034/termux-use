import os
import time
def Telcop():
    os.system(f"rm -rf ./conf/telcop.json")
    print("---------------开始备份----------------")
    os.system(f"termux-contact-list >> ./conf/telcop.json")
    print("-------------  备份成功----------------")

if __name__ == "__main__":
    Telcop()
    

