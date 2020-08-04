# 자연수 a, b 사이의 구간에 대해서 홀수는 더하고 짝수는 빼는 식을 보여준 후 결과를 출력하시오.

# 예)

# a=5, b=10 인 경우, 5-6+7-8+9-10=-3

# a=6, b=9 인 경우, -6+7-8+9=2

a, b = map(int, input().split(" "))
sum = 0
for i in range(a, b + 1, 1):
    if i % 2 != 0 and i == a:
        print("{}".format(i), end="")
        sum = sum + i
    elif i % 2 != 0:
        print("+{}".format(i), end="")
        sum = sum + i
    elif i % 2 == 0:
        print("-{}".format(i), end="")
        sum = sum - i
print("={}".format(sum))