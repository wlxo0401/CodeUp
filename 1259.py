# 1부터 n까지의 수 중 짝수의 합을 구하시오.

sum = 0

for i in range(1, int(input()) + 1, 1):
    if (i % 2) == 0:
        sum = sum + i
print(sum)