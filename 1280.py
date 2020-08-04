# 두 자연수 a, b 사이의 구간에 대해서

# 홀수는 더하고 짝수는 빼는 식을 보여준 후 결과를 출력하시오.

# 단, 결과가 양수이면 +를 붙이지 않는다.

# 예)

# a = 5, b=10 일 경우, +5-6+7-8+9-10=-3

# a = 6, b=9 일 경우, -6+7-8+9=2

a, b = map(int, input().split(" "))
sum = 0
for i in range(a, b + 1, 1):
    if i % 2 != 0:
        print("+{}".format(i), end="")
        sum = sum + i
    elif i % 2 == 0:
        print("-{}".format(i), end="")
        sum = sum - i
print("={}".format(sum))