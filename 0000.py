

sq = 10
n = 21
index = 0
a=[]
for i in range(0, 30):
    a.append(0)

# 2부터 제곱근 + 1 까지 반복
for i in range(2, sq+1):
    # 입력 받은 수를 i로 나누어 나머지가 0이 나올
    while n % i == 0:
        n /= i
        a[index] = i
        index += 1
        print(i)
        print(a)