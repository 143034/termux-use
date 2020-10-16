import os
import time



def os_run(tem,flag):
    if flag == 0:

        os.system(f"%s"%(tem))
    else:
#        print(tem)
        temp = tem.split('-')[1].split()[1]
#        print(temp)
        os.system(f"rm -rf ./conf/%s.json"%(temp))
        os.system(f"%s >> ./conf/%s.json"%(tem,temp))
#电量
def battery(flag):
    os_run("termux-battery-status",flag)
#摄像头信息
def Camera_info(flag):
    os_run("termux-camera-info",flag)
#无线电信息
def Cellinfo(flag):
    os_run("termux-telephony-cellinfo",flag)

#运营商信息
def deviceinfo(flag):
    os_run("termux-telephony-deviceinfo",flag)


#wifi连接信息


def connectioninfo(flag):
    os_run("termux-wifi-connectioninfo",flag)


#WiFi 扫描信息


def scaninfo(flag):
    os_run("termux-wifi-scaninfo",flag)

#调整屏幕亮度

def brightness(tem,flag):

    os_run("termux-brightness  %s"%(tem),flag)

#拍摄照片
def camera_photo(opt,address,flag):
    os_run("termux-camera-photo -c %s %s"%(opt,address),flag)

    

#查看接切板内容

def clipboard_get(flag):
    os_run("termux-clipboard-get",flag)




#设置新的剪贴板内容

def clipboard_set(message,flag):
    os_run("termux-clipboard-set %s"%(message),flag)

#指纹传感器

def fingerprint(flag):
    os_run("termux-fingerprint",flag)

def media(address):

    os_run("termux-media-player play %s"%(address),0)


def torch(opt):
    os_run("termux-torch %s"%(opt),0)
def vibrate(opt):
    os_run("termux-vibrate -d %s"%(opt),0)

def tts_speak(message):
    os_run("termux-tts-speak -e 'com.xiaomi.speech'  %s"%(message),0)


def confirm(title,content,flag):
    os_run("termux-dialog confirm -i %s -t %s"%(content,title),flag)

def checkbox(title,content,flag):
    os_run("termux-dialog checkbox -v %s -t %s"%(title,content),flag)

def counter(value,title,flag):
    os_run("termux-dialog counter -r %s -t %s"%(value,title),flag)

def date(title,flag):
    os_run("termux-dialog date -d 'yyyy-MM-dd' -t %s"%(title),flag)

def radio(title,value,flag):
    os_run("termux-dialog radio -v %s -t %s"%(value,title),flag)

def sheet(value,flag):
    os_run("termux-dialog sheet -v %s"%(value),flag)
def spinner(title,value,flag):
    os_run("termux-dialog spinner -v %s -t %s"%(value,title),flag)
def text(title,value,flag):
    os_run("termux-dialog text -i %s -t %s"%(value,title),flag)
def time_choose(title,flag):
    os_run("termux-dialog time -t %s"%(title),flag)
if __name__ == "__main__":

    connectioninfo(0)


    
