h, m = input().split()
h = int(h)  # 시간
m = int(m)  # 분

# 45분을 당긴다!

# 그냥 45분을 뺀다
if m >= 45:
    print(h, m-45)
# 1시간을 까서~ 45를 빼야한다.
else:
    if h == 0:  # 현재 0시라면? 0시 44분 -> 23시 59분
        print(23, 15+m)
    else:  # 0시가 아니라면
        print(h-1, 15+m)

# 2번째 답
# h, m = input().split()
# h = int(h)  # 시간
# m = int(m)  # 분

# total = h * 60 + m - 45 + (24*60)

# print(total//60 % 24, total % 60)
# # h=0, m=0
