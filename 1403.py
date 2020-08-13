# k개의 숫자를 입력받고 그 숫자들을 두번 출력하시오.

# 입력 예) 
# 2
# 5 7
# 출력 예)
# 5
# 7
# 5
# 7

num = int(input())

nums = list(map(int, input().split()))

for j in range(2):
    for i in range(0, num, 1):
        print(nums[i])