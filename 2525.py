# 입력부
h, m = input().split()
h = int(h)  # 시간
m = int(m)  # 분
gap = int(input())  # 요리 시간 <-분

# 1. 시를 분으로 바꾸고, 모두 더한다
mm = h * 60 + m + gap
# 2. 다시 시와 분으로 되돌린다.
print(mm//60 % 24, mm % 60)



