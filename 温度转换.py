#TempConvert.py
TempStr=input("请输入带有温度表示符号的温度值")
if TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])+32
    print("转换后的温度为{:.2f}F".format(F))
elif TempStr[-1] in ["F","f"]:
    c=(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度为{:.2f}C".format(C))
else:
    print("输入有误")