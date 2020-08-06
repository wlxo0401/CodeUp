# 길이 n이 입력되면 다음과 같은 사각형을 출력한다.

# 예)

# n이 5일때

# *****
# *   *
# *   *
# *   *
# *****


num = int(input())

for i in range(1, num + 1, 1):
    if i == 1 or i == num:
        for j in range(0, num, 1):
            print("*",end="")
        print()
    else:
        for j in range(1, num + 1, 1):
            if j == 1 or j == num:
                print("*",end="")
            else:
                print(" ",end="")
        print()