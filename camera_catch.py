from others import camera_photo
import os


def ctr_camera():
    print('----------开始拍照------------')
    os.system(f"rm -rf ./conf/camer*")
    print("前置[1]   后置[2]")
    dat = int(input("请输入选择:"))
    if dat == 1:

        camera_photo(1,'./conf/camera.jpg',0)
    else:
        camera_photo(0,'./conf/camera_la.jpg',0)

    print('----------拍照结束------------')
