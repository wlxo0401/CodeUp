# 계산기 1에서 두 피연산자에 대한 연산만 다루었다.

# 이번에는 식을 입력하면 차례대로 계산하여 출력하는 계산기를 만들어보자.

# 단, 우선순위는 따지지 않고 왼쪽에서 부터 차례대로 계산하고, 모든 계산은 정수형 계산으로 처리한다.

# 째 줄에 정수와 사칙연산기호가 식으로 입력된다.

# (정수는 int 범위, 괄호 없이 +,-,*,/) 

# 식의 마지막엔 =가 입력된다.

# 왼쪽부터 차례대로 연산한 결과를 출력한다.(우선순위x)

# 3+3-3*3/3=

# 3

# 식을 입력 받는다.
expression = input()
# 결과
result = 0
# 부호
symbol = ''

lastNumber = 0
lsatSymbol = ''
lastIndex = 0
isFirst = True
# 글자 수 만큼 반복문을 돌린다.
for i in range(0, len(expression)):
    # 식 i 번째 글자가 식이면 이프문 작동한다.
    if expression[i] in ('+', '-', '*', '/', '='):
        # 식 i 번째 글자를 넣는다.
        symbol = expression[i]
        # 넘버 변수에 마지막 숫자 자리에서 i번재까지 수를 저장한다.
        number = int(expression[lastIndex:i])
        # 넘버에 저장했으니 마지막 숫자 자리 이동
        lastIndex = i+1
        # 처음 이라면 작동한다.
        if isFirst:
            # 한번만 실행하기 위해서 플래그 신호용
            isFirst = False
            # 결과에 넘버를 더함으로 첫 숫자 입력
            result += int(number)
            # 전 숫자를 기억하기 위함
            lastNumber = number
            # 전 심볼을 기억하기 위함
            lsatSymbol = symbol
            # 진행
            continue

        if lsatSymbol == '+':
            result += number
            result = int(result)
        elif lsatSymbol == '-':
            result -= number
            result = int(result)
        elif lsatSymbol == '*':
            result *= number
            result = int(result)
        elif lsatSymbol == '/':
            result /= number
            result = int(result)

        lsatSymbol = symbol
print(int(result))
