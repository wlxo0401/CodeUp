# 길이 n
# 이 입력되면 다음과 같은 숫자 피라미드를 출력한다.

# 예)

# n
# 이 5이면

# 1

# 1 2

# 1 2 3

# 1 2 3 4

# 1 2 3 4 5


num = int(input())

for i in range(1, num + 1, 1):
    for j in range(1, i + 1, 1):
        print(j, end=" ")
    print()