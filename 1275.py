# 어떤 수 n과 k가 있다.

# n과 k의 관계는 다음과 같다.

# nk

# nk는 n을 k번 곱한 것을 말한다.

# 입력으로 n과 k가 주어지면 결과를 출력한다.

# 예)

# 52 = 25

# 24 = 16

a, b = map(int, input().split(" "))
sum = 1
for i in range(1, b + 1, 1):
    sum = sum * a
print(sum)


