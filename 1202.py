# 재호는 이번 시험에 받은 성적이 궁금했다.

# 점수가 입력되면 등급을 출력하시오.

# 등급)

#  90점 이상 : A

# 80점 이상 : B

# 70점 이상 : C

# 60점 이상 : D

# 60점 미만 : F

jum = int(input())

if 90 <= jum:
    print("A") 
elif 80 <= jum < 90:
    print("B")
elif 70 <= jum < 80:
    print("C")
elif 60 <= jum < 70:
    print("D")
elif jum < 60:
    print("F")