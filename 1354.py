# 길이 n이 입력되면 역삼각형을 출력한다.

# 예)

# n이 5이면

# *****
# ****
# ***
# **
# *

num = int(input())
for i in range(0, num, 1):
    for j in range(num-i):
        print("*",end="")
    print()