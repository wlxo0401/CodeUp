# 팩토리얼(!)은 다음과 같이 정의된다.

# n! = n * (n-1) * (n-2) * ... * 2 * 1

# 즉, 5! = 5 * 4 * 3 * 2 * 1 = 120 이다.

# n이 입력되면 n!의 값을 출력하시오.

# 자연수 n이 입력된다. (n <= 12)

a = int(input())

sum = 1
for i in range(0, a, 1):
    sum = sum * (a-i)
print(sum)