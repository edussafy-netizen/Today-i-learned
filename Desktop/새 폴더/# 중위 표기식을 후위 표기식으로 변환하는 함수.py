# 중위 표기식을 후위 표기식으로 변환하는 함수
def infix_to_postfix(expression):
    # 연산자의 우선순위
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []  # 연산자를 저장할 스택
    postfix = []  # 후위 표기식을 저장할 리스트

    # 주어진 중위표기식을 한 번씩 순회하면서 우선순위에 따라서 출력한다.
    for ch in expression:
        if ch.isnumeric():  # 숫자이냐 ? 아니냐? 를 판별하는 함수
            postfix.append(ch)  # 후위표기식에 바로 추가한다!

        elif ch == '(':  # 여는 괄호 만나면, 무조건 스택에 집어넣는다.
            stack.append(ch)  

        elif ch == ')':  # 닫힌 괄호가 나오면, 여는 괄호를 만날 때가지 모든 연산자를 후위표기식에 추가한다!
            top_token = stack.pop()  # 제일 맨 위에 있는 스택 값을 뽑는다.
            while top_token != '(':  # 뽑은 그 친구가 여는 괄호가 아니라면, 또 뽑아
                postfix.append(top_token)  # 연산자가 나오면 뽑아서 후위표기식에 추가하고,
                top_token = stack.pop()  # 다시 뽑아 .
        else:  # 연산자인 경우 ( + , -, * , / )
            # 스택에서 가장 위에 있는 연산자가 본인보다 우선순위 같거나 높은 경우에는 , 먼저 계산되어야 하므로,,, 후위표기식에 먼저 추가해준다.
            # op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
            while stack and op_dict[stack[-1]] >= op_dict[ch]:
                postfix.append(stack.pop())
            stack.append(ch)
            
    while stack:  
        postfix.append(stack.pop())
    
    return ' '.join(postfix)  # 리스트를 문자열로 변환하여 반환

infix_expression = "3+(2*5)-8/4"
postfix_expression = infix_to_postfix(infix_expression)
print(f"후위 표기식: {postfix_expression}")
# 이건 새로운 업데이트 