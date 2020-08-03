# 자연수 N이 주어지면 N의 약수를 오름차순으로 모두 출력하시오.


a = int(input())

for i in range(1, a + 1, 1):
    if a % i == 0:
        print(i,end=" ")
print()