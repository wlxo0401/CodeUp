# n이 입력되면 다음과 같은 삼각형을 출력하시오.

# 예)

# n 이 5 이면

# *
# **
# ***
# ****
# *****


num = int(input())
for i in range(1, num + 1, 1):
    for j in range(1, i + 1, 1):
        print("*",end="")
    print("")