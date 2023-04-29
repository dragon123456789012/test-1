#
a = int(input())
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):  # 100의 배수가 아니다 또는  400의 배수다
    print(1)
else:  # 4의 배수가 아니다!
    print(0)
