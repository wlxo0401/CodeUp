# 길이 n이 입력되면 길이가 n인 사각형을 출력하시오.

# 단, 사각형은 * 모양으로 채운다.

# 4
# ****
# ****
# ****
# ****

num = int(input())

for i in range(0, num, 1):
    for i in range(0, num, 1):
        print("*",end="")
    print()