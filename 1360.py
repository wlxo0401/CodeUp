# 길이 n
# 이 입력되면 다음과 같은 숫자 피라미드를 출력한다.

# 예) n
# 이 5
# 이면

# 5 5 5 5 5

# 4 4 4 4

# 3 3 3

# 2 2

# 1 

num = int(input())

for i in range(0, num, 1):
    for j in range(num - i, 0, -1):
        print(num-i,end=" ")
    print()