#https://www.acmicpc.net/problem/11899
#https://www.acmicpc.net/source/81515378

def main():
    s = list(input())
    answer = 0
    stack = []
    while s:
        c = s.pop()
        if c == '(':
            if stack == []:
                answer += 1
            else:
                stack.pop()
        else:
            stack.append('(')
    answer += len(stack)
    print(answer)

if __name__ == "__main__":
    main()
