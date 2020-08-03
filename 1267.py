# 수의 개수 n이 주어지고, 그 다음 줄에 무작위로 n개의 자연수가 입력된다.

# 그 n개의 수 중에서 5의 배수만 골라 합을 출력하시오.

a = int(input())
b = list(map(int, input().split(" ")))

sum = 0 
for i in range(0, a, 1):
    if b[i] % 5 == 0:
        sum = sum + b[i]
print(sum)