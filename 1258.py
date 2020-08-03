# 정수 n이 입력으로 들어오면 1부터 n까지의 합을 구하시오.

sum = 0

for i in range(1, int(input()) + 1, 1):
    sum = sum + i
print(sum)