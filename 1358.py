# 어떤 수 n을 입력받으면 다음과 같은 삼각형을 출력한다.

# 여기서 입력되는 n은 반드시 홀수이다.
# 5
#   *
#  ***
# *****



n = int(input())

for i in range(n - 2, -1, -1):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, (n - i * 2)):
        print('*', end='')
    for j in range(0, i):
        print(' ', end='')
    print()