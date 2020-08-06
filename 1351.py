# 구구단


a, b = map(int, input().split(" "))

for i in range(a, b + 1, 1):
    for j in range(1, 10, 1):
        print("{}*{}={}".format(i, j, i * j))
