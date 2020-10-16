import os
import json
import time

def Call_tel():
    temp = ""
    os.system(f"rm -rf ./conf/call_conf.json")
    ustr = ""
    with open("./conf/telcop.json","r") as f:
        date = json.load(f)
        f.close()
    for i in date:
        ustr += i["name"] + ","
        temp += i["number"] + ","
   # print(temp)

    os.system(f"termux-dialog sheet -v '%s' >> ./conf/call_conf.json"%(ustr))
    with open("./conf/call_conf.json","r") as f:
        opt = json.load(f)
        print(opt["text"])
        f.close()
    for i in date:

        if opt["text"] == i["name"]:
            a = i["number"]
            if a[3] == " ":
                ret = " "
                b = a.split()
                for t in b:
                    ret += t
            else:
                ret = " "
                c = a.split("-")
                for u in c:
                    ret += u
                



                
            os.system(f"termux-telephony-call %s"%(ret))

if __name__ == "__main__":
    Call_tel()
