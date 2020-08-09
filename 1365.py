num = int(input())

for i in range(0, num, 1):
    print("*", end="")
print()

for i in range(1, num - 1, 1):
    for j in range(0, num, 1):
        if (j == 0) or (j == i) or (j == num-1) or (j == num-i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(0, num, 1):
    print("*", end="")
print()
