from stack.list_stack import ListStack


def evaluate(p):
    s = ListStack()
    digit_previously = False # 숫자인 경우 이전 문자가 숫자인지 파악하기 위함

    for i in range(len(p)):
        char = p[i] # i 번 문자

        # 문자에서 가능한 경우의 수가 3가지 1. 숫자 2. 연산자 3. 빈칸
        if char.isdigit(): # char 가 숫자이면 True
            if digit_previously: # 이전에 숫자로 받은 경우
                tmp = s.pop()
                tmp = 10 * tmp + ord(char) - ord('0') # asci 코드 값을 빼면 해당 숫자와 같은 숫자가 나온다.
                s.push(tmp)
            else: # 첫 번째 숫자인 경우
                tmp = ord(char) - ord('0')
                s.push(tmp)
                digit_previously = True
        elif is_operation(char): # char 가 연산자 기호인 경우
            s.push(operation(s.pop(), s.pop(), char))
            digit_previously = False
        else: # 공백인 경우
            digit_previously = False

    return s.pop()

def evaluate_split(postfix):
    s = ListStack()
    postfix_list = postfix.split(' ')

    for char in postfix_list:
        if char.isdigit():
            s.push(int(char))
        elif is_operation(char):
            s.push(operation(s.pop(), s.pop(), char))

    return s.pop()


def is_operation(char) -> bool:
    return char == '+' or char == '-' or char == '*' or char == '/'

def operation(after:int, before:int, operator_char:str) -> int:
    return {'+': before + after, '-': before - after, '*': before * after, '/': before / after}[operator_char]

def main():
    postfix = "700 3 47 + 6 * - 4 /" # 후위 표현식
    print("input : ", postfix)
    answer = evaluate(postfix)
    print("answer: ", answer)

    answer_split = evaluate_split(postfix)
    print("answer_split: ", answer_split)

if __name__ == '__main__':
    main()