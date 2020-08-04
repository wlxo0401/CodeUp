# 두 자연수 a, b 사이의 구간에 대해서

# 홀수는 더하고 짝수는 뺀다음의 합을 출력하시오.

# 예)

# a = 5, b=10 일 경우, 5 - 6 + 7 - 8 + 9 - 10 = -3

# 두 자연수 a, b를 입력 받는다. 

# (반드시 a가 b보다 같거나 작게 입력된다.)

a, b = map(int, input().split(" "))
sum = 0
for i in range(a, b + 1, 1):
    if i % 2 != 0:
        sum = sum + i
    elif i % 2 == 0:
        sum = sum - i
print(sum)