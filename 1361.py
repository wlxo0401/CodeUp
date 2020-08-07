# 내 문제집에 추가
# n이 입력되면 n층의 별 계단을 출력하시오.

# 예) n= 5인 경우,

# **
#  **
#   **
#    **
#     **


num = int(input())


for i in range(0, num, 1):
    for j in range(0, i, 1):
        print(" ",end="")
    print("**")