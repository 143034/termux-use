def  Interface():
    print("-"*50)
    print(" "*20)
    print("通讯录备份[1]     拨打电话[2]      闪光灯[3]")
    print("震动[4]           拍照[5]          查看ip[6]")
    opt = int(input("请选择功能:"))
    return opt



if __name__ == "__main__":
    Interface()
