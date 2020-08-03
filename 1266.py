# 수의 개수  n이 주어지고, 그 다음 줄에 무작위로 n개의 정수가 입력된다.

# n개의 수의 합을 출력하시오.

a = int(input())
b = list(map(int, input().split(" ")))

sum = 0 
for i in range(0, a, 1):
    sum = sum + b[i]
print(sum)