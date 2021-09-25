 print("Nhập giá trị n: " ,end='')
n=int(đầu vào())
nếu n > 0:
    giaithua=1
    cho i trong phạm vi(1,n+1):
        giaithua=giaithua*i
    print(n,"giai thừa bằng:",giaithua)
khác:
    print("Vui lòng nhập n > 0")