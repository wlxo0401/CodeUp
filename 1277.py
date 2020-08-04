# 첫 줄에 데이터의 개수 N(N은 홀수)이 입력되고, 그 다음 줄에 N개의 데이터가 입력된다.

# 여기서 첫번째 데이터, 중간 데이터, 마지막 데이터를 출력하시오.

# 예) 

# 5

# 2 4 6 1 7

# 이면

# 2 6 7

# 이 출력된다.

# (첫번째 데이터 2,

# 중간 데이터 6,

# 마지막 데이터 7)

# 반복에 필요한 횟수
a = int(input())
# 리스트 안에 들어갈 수
b = list(map(int, input().split(" ")))

if a == 1:
    for i in range(0, 3, 1):
        print(b[0],end=" ")
elif a >=1:
    for i in range(0, a, 1):
        if i == 0:
            print(b[0], end=" ")
        elif i == ((a + 1) / 2) - 1:
            print(b[i], end=" ")
        elif i == a - 1:
            print(b[i])


