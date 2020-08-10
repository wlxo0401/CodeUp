# 두 수를 거꾸로 출력하기..

# 세 수를 거꾸로 출력하기...

# 이런 문제들은 쉽게 풀 수 있었다.

# 이번에는 데이터의 개수가 n개가 들어오고, n개의 데이터를 거꾸로 출력하는 프로그램을 작성하시오.




num = int(input())

nums = list(map(int, input().split(" ")))

nums2 = list(reversed(nums))

for i in range(0, num, 1):
    print(nums2[i], end=" ")
print()

